# -*- coding: utf-8 -*-
import setting
from qqbot import qqbotsched
import weibo
import copy
import modian

global commentNum
global firstcheck

global weibo_id_array
global firstcheck_weibo

weibo_id_array = []
firstcheck_weibo = 1

commentNum = 0
firstcheck = 1

groupid = setting.groupid()


# 关键字回复
def onQQMessage(bot, contact, member, content):
    if content == 'wds' or content == '集资' or content == 'jz' or content == '打卡' or content == 'dk':
        jz = ''
        jz = jz + setting.wds_name() + '\n' + setting.wds_url()
        bot.SendTo(contact, str(jz))
    elif content == 'wds20' or content == 'jz20' or content == 'rank' or content == '聚聚榜' or content == 'jzb':
        bot.SendTo(contact, modian.rank(1))
    elif content == 'dkb' or content == '打卡榜' or content == 'dk20' or content == 'dakabang':
        bot.SendTo(contact, modian.rank(2))
    elif content == "独占":
        duzhan = "独占请集资" + '\n' + setting.wds_name() + '\n' + setting.wds_url()
        bot.SendTo(contact, duzhan)
    elif content == "想39":
        xiang39 = "补档请看" + '\n' + "http://t.cn/RCbRLjZ"
        bot.SendTo(contact, xiang39)
    elif content == "剁椒鱼头":
        duojiaoyutou = "我们都爱剁椒鱼头"
        bot.SendTo(contact, duojiaoyutou)
    elif content == "欢迎新人":
        welcome = "欢迎聚聚加入BEJ48-黄子璇的应援群！" + '\n' + "大家可以叫子璇宝宝叁玖 ~" + '\n' +\
            "叁玖是一只土生土长的北京姑娘，生日是5月20日，生在2002年的金牛座。" + '\n' + "九春三秋，只为遇见你。" +\
            '\n' + "希望你我可以相知相识～" + '\n' + '\n' + "三分钟带你领略甜甜的叁玖" + '\n' +\
            "首演unit《爱的魔法》：http://t.cn/RolMikW" + '\n' + '\n' +\
            "出道以来第五场公演unit《爱的魔法》：http://t.cn/RCb8QBn" + '\n' + '\n' +\
            "第四届总决选拉票公演：http://t.cn/RCb8gzH" + '\n' + '\n' +\
            "更多补档内容请戳b站：BEJ48-黄子璇应援会 http://t.cn/RCbRLjZ" + '\n' + '\n' +\
            "最后也请聚聚关注下叁玖的微博与超级话题吧" + '\n' + "@BEJ48-黄子璇：http://t.cn/RCbRiAe" +\
            '\n' + "@BEJ48-黄子璇应援会：http://t.cn/RCbRNu1" + '\n' +\
            "#黄子璇#超级话题：http://t.cn/RCbRQg2" + '\n' + '\n' +\
            "让我们陪着这个刚出道不久的小孩子长大，看着她成为更好的人，一起给她最好的应援吧~（鞠躬）"
        bot.SendTo(contact, welcome)


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


# 定时任务。每3分钟获取一次微打赏数据，如果有新的集资评论，自动发送到群。
# 可修改定时任务时间来提高查询频率，其他无需修改
@qqbotsched(hour='0-23', minute='0-59')
def mytask(bot):
    global commentNum
    global firstcheck
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            modian_dict = modian.num().copy()
            if modian_dict['status'] == 2:
                bot.SendTo(group, '摩点项目num查询失败')
                bot.SendTo(group, modian_dict['err_msg'])
            elif modian_dict['status'] == 0:
                commentNum_new = modian_dict['sum']
                if firstcheck == 1:
                    commentNum = commentNum_new
                    firstcheck = 0
                difference = commentNum_new - commentNum
                if difference:
                    commentNum = commentNum_new
                    bot.SendTo(group, modian.diff(difference))
