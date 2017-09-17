# -*- coding: utf-8 -*-
import wds
import wds20
import link
from qqbot import qqbotsched
import requests
import math
import json
import weibo

global commentNum
global firstcheck

global weiboid
global firstcheck_weibo

weiboid = ""
firstcheck_weibo = 1

commentNum = 0
firstcheck = 1
#关键字回复
def onQQMessage(bot, contact, member, content):
    if content == 'wds':
        bot.SendTo(contact, wds.start())
    elif content == "集资":
        bot.SendTo(contact, wds.start())
    elif content == 'wds20':
        bot.SendTo(contact, wds20.start())
    elif content == 'rank':
        bot.SendTo(contact, wds20.start())
    elif content == "独占":
        duzhan = "独占请集资" + '\n' + str(wds.start())
        bot.SendTo(contact, duzhan)
    elif content == "想39":
        xiang39 = "补档请看" + '\n' + "http://t.cn/RCbRLjZ"
        bot.SendTo(contact, xiang39)
    elif content == "剁椒鱼头":
        duojiaoyutou = "我们都爱剁椒鱼头"
        bot.SendTo(contact, duojiaoyutou)
    elif content == "欢迎新人":
        welcome = "欢迎聚聚加入BEJ48-黄子璇的应援群！" + '\n' + "大家可以叫子璇宝宝叁玖 ~" + '\n' + "叁玖是一只土生土长的北京姑娘，生日是5月20日，生在2002年的金牛座。" + '\n' + "九春三秋，只为遇见你。" + '\n' + "希望你我可以相知相识～" + '\n' + '\n' + "三分钟带你领略甜甜的叁玖" + '\n' + "首演unit《爱的魔法》：http://t.cn/RolMikW" + '\n' + '\n' + "出道以来第五场公演unit《爱的魔法》：http://t.cn/RCb8QBn" + '\n' + '\n' + "第四届总决选拉票公演：http://t.cn/RCb8gzH" + '\n' + '\n' + "更多补档内容请戳b站：BEJ48-黄子璇应援会 http://t.cn/RCbRLjZ" + '\n' + '\n' + "最后也请聚聚关注下叁玖的微博与超级话题吧" + '\n' + "@BEJ48-黄子璇：http://t.cn/RCbRiAe" + '\n' + "@BEJ48-黄子璇应援会：http://t.cn/RCbRNu1" + '\n' + "#黄子璇#超级话题：http://t.cn/RCbRQg2" + '\n' + '\n' + "让我们陪着这个刚出道不久的小孩子长大，看着她成为更好的人，一起给她最好的应援吧~（鞠躬）"
        bot.SendTo(contact, welcome)
    elif content == '39微博':
        bot.SendTo(contact, weibo.getscheme())

#定时任务。每五分钟获取一次微博数据，如果有新的微博，自动发送到群。
#可修改定时任务时间来提高查询频率，其他无需修改
@qqbotsched(hour='0-23', minute='0-59/3')
def mytask3(bot):
	global weiboid
	global firstcheck_weibo
	wbcontent = ""
	gl = bot.List('group', '606642799')
	if gl is not None:
	    for group in gl:
	        if (firstcheck_weibo == 1):
	            weiboid = weibo.checkid()
	            firstcheck_weibo = 0
	        checkwbid = weibo.checkid()
	        if (weiboid != checkwbid):
	            weiboid = checkwbid
	            retweet = weibo.checkretweet()
	            wbpic = weibo.checkpic()
	            wbscheme = weibo.getscheme()
	            if (retweet):
	                wbcontent = "小偶像刚刚[转发]了一条微博：" + '\n' + '\n' + weibo.getretweetweibo() + '\n'
	                wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
	            else:
	                wbcontent = "小偶像刚刚发了一条新微博：" + '\n' + '\n' + weibo.getweibo() + '\n'
	                if (wbpic):
	                    wbcontent = wbcontent + weibo.getpic()
	                wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
	            bot.SendTo(group, wbcontent)

#定时任务。qqbot每天定时重启前的提醒。
@qqbotsched(hour='22', minute='28')
def mytask2(bot):
	gl = bot.List('group', '606642799')
	if gl is not None:
	    for group in gl:
	        attention = "[attention]" + '\n' + "提醒89哥，废物机器人将在两分钟后重启"
	        bot.SendTo(group, attention)

#定时任务。每3分钟获取一次微打赏数据，如果有新的集资评论，自动发送到群。
#可修改定时任务时间来提高查询频率，其他无需修改
@qqbotsched(hour='0-23', minute='0-59/3')
def mytask(bot):
	global commentNum
	global firstcheck
	gl = bot.List('group', '606642799')
	if gl is not None:
	    for group in gl:
	        commentNum_new = checkNum()
	        if (firstcheck == 1):
	            commentNum = commentNum_new
	            firstcheck = 0
	        difference = commentNum_new - commentNum
	        if (difference):
	            commentNum = commentNum_new
	            bot.SendTo(group,return_comment(difference))

def checkNum():
	ajax_url = 'https://wds.modian.com/ajax_comment'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	form = {
	    'pageNum': 1,
	    'moxi_id': link.moxi_id(),
	    'pro_id': link.pro_id()
	}
	comment = []
	while True:
	    response = requests.post(ajax_url, form, headers=header).json()
	    if response['status'] == '-1':
	        break
	    datas = response['des']
	    for data in datas:
	        c_userinfo = data['c_userinfo']
	        comment.append((c_userinfo['nickname'] , data['pay_amount']))
	    form['pageNum'] += 1
	num = int(len(comment))
	return num

def return_comment(difference):
	wds_name = link.wds_name()
	wds_url = link.wds_url()
	ajax_url = 'https://wds.modian.com/ajax_comment'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	form = {
	    'pageNum': 1,
	    'moxi_id': link.moxi_id(),
	    'pro_id': link.pro_id()
	}
	comment = []
	result = ""
	total = 0.0
	while True:
	    response = requests.post(ajax_url, form, headers=header).json()
	    if response['status'] == '-1':
	        break
	    datas = response['des']
	    for data in datas:
	        c_userinfo = data['c_userinfo']
	        comment.append((c_userinfo['nickname'] , data['pay_amount']))
	    form['pageNum'] += 1
	#20170913update
	#增加了微打赏项目中的只评论无集资情况（如评论中出现垃圾广告）判断
	#只评论空集资导致集资额comment[i][1]返回null，无法转为float
	for i in range(0, int(difference)):
	    try:
	        try_supmoney = float(comment[i][1])
	    except Exception as e:
	        result = result + "微打赏被ID为：" + str(comment[i][0]) + " 的聚聚评论了" + '\n'
	    else:
	        result = result + "ID: " + str(comment[i][0]) + " 的聚聚刚刚在【" + wds_name + "】中支持了 ¥" + str(comment[i][1]) + '\n' + "感谢这位聚聚对" + link.idol_name() + "的支持" + '\n'
	for j in comment:
	    try:
	        total += float(j[1])
	    except Exception as e:
	        pass
	result = result + "【微打赏】：" + wds_url + '\n' + "目前集资总额：¥" + str(total)
	return result

