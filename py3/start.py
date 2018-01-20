# -*- coding: utf-8 -*-
import setting
from qqbot import qqbotsched
import weibo
import copy
import modian
import time

# global commentNum
# global firstcheck

global weibo_id_array
global firstcheck_weibo

weibo_id_array = []
firstcheck_weibo = 1

# commentNum = 0
# firstcheck = 1

groupid = setting.groupid()


# 关键字回复
def onQQMessage(bot, contact, member, content):
    if contact.ctype == 'group' and contact.nick == groupid:
        if content == 'wds' or content == '集资' or content == 'jz' or content == '打卡' or content == 'dk':
            jz = ''
            jz = jz + setting.wds_name() + '\n' + setting.wds_url()
            bot.SendTo(contact, str(jz))
        elif content == 'wds20' or content == 'jz20' or content == 'rank' or content == '聚聚榜' or content == 'jzb' or content == '集资榜':
            bot.SendTo(contact, modian.rank(1))
        elif content == 'dkb' or content == '打卡榜' or content == 'dk20' or content == 'dakabang':
            bot.SendTo(contact, modian.rank(2))
        elif content == "独占":
            duzhan = "独占请集资" + '\n' + setting.wds_name() + '\n' + setting.wds_url()
            bot.SendTo(contact, duzhan)
        # elif content == "想39":
        #     xiang39 = "补档请看" + '\n' + "http://t.cn/RCbRLjZ"
        #     bot.SendTo(contact, xiang39)
        # elif content == "剁椒鱼头":
        #     duojiaoyutou = "我们都爱剁椒鱼头"
        #     bot.SendTo(contact, duojiaoyutou)
        elif content == "欢迎新人":
            welcome = setting.welcome()
            bot.SendTo(contact, welcome)
        elif content == "help":
            help = '''废物机器人口令帮助：\n“集资”或“打卡”：返回集资地址"\n“集资榜”或“jzb”：返回集资金额榜单\n“打卡榜”或“dkb”：返回打卡天数榜单\n'''
            bot.SendTo(contact, help)


# 定时任务。每五分钟获取一次微博数据，如果有新的微博，自动发送到群。
# 可修改定时任务时间来提高查询频率，其他无需修改
@qqbotsched(hour='0-23', minute='0-59/5')
def mytask3(bot):
    global weibo_id_array
    global firstcheck_weibo
    wbcontent = ""
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            idcount = -1
            if (firstcheck_weibo == 1):
                weibo_id_array = copy.copy(weibo.getidarray())
                firstcheck_weibo = 0
            checkwbid = copy.copy(weibo.get_5_idarray())
            if (firstcheck_weibo == 0):
                for cardid in checkwbid:
                    idcount += 1
                    if int(cardid) == 0:
                        continue
                    if cardid not in weibo_id_array:
                        weibo_id_array.append(cardid)
                        retweet = weibo.checkretweet(idcount)
                        wbpic = weibo.checkpic(idcount)
                        wbscheme = weibo.getscheme(idcount)
                        if (retweet):
                            wbcontent = "小偶像刚刚[转发]了一条微博：" + '\n' + '\n' + weibo.getretweetweibo(idcount) + '\n'
                            wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
                        else:
                            wbcontent = "小偶像刚刚发了一条新微博：" + '\n' + '\n' + weibo.getweibo(idcount) + '\n'
                            if (wbpic):
                                wbcontent = wbcontent + weibo.getpic(idcount)
                            wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
                        bot.SendTo(group, wbcontent)


# 定时任务。qqbot每天定时重启前的提醒。
@qqbotsched(hour='7', minute='58')
def mytask2(bot):
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            attention = "[attention]" + '\n' + "废物机器人将在两分钟后重启"
            bot.SendTo(group, attention)


# 定时任务。每1分钟获取一次微打赏数据，如果有新的集资评论，自动发送到群。
# 可修改定时任务时间来提高查询频率，其他无需修改
# 若修改了查询频率，一定要修改下方newOrder方法的第二个参数
@qqbotsched(hour='0-23', minute='0-59')
def mytask(bot):
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            # 获取当前unix时间（10位，单位为秒）
            stampTime = int(time.time())
            # 调用modian.py的newOrder方法
            # 第二个参数是查询时间段：60即查询当前时间前60s得新集资
            # 若修改了查询频率，则一定要修改第二个参数
            msgDict = modian.newOrder(stampTime, 60)
            # 返回了一个字典
            if msgDict:
                for msg in msgDict['msg']:
                    msg += msgDict['end']
                    bot.SendTo(group, msg)
            #
            # # 旧逻辑代码
            # modian_dict = modian.num().copy()
            # if modian_dict['status'] == 2:
            #     bot.SendTo(group, '摩点项目num查询失败')
            #     bot.SendTo(group, modian_dict['err_msg'])
            # elif modian_dict['status'] == 0:
            #     commentNum_new = modian_dict['sum']
            #     if firstcheck == 1:
            #         commentNum = commentNum_new
            #         firstcheck = 0
            #     difference = commentNum_new - commentNum
            #     if difference:
            #         commentNum = commentNum_new
            #         bot.SendTo(group, modian.diff(difference))
