# -*- coding: utf-8 -*-
import link
from qqbot import qqbotsched
import requests
import math
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

global global_live_id
global msgidClient_array
global firstcheck_juju

global_live_id = "59bbfc740cf20e50ac3874d0"
msgidClient_array = []
firstcheck_juju = 0

#13位unix时间戳（ms）转为字符串时间
def stamp_to_str(timestamp):
    x = time.localtime(timestamp / 1000)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return time_str


#定时任务，每分钟执行一次
#查询口袋48直播
#成员id及小偶像name在link.py中设置
@qqbotsched(hour='0-23', minute='0-59')
def get_live(bot):
	global global_live_id
	#仅需修改播报的qq群号
	gl = bot.List('group', '606642799')
	if gl is not None:
	    for group in gl:
	        ajax_url = 'https://plive.48.cn/livesystem/api/live/v1/memberLivePage'
	        header = {
	            'Host' : 'plive.48.cn',
	            'app-type' : 'fans',
	            'Accept' : '*/*',
	            'version' :'4.1.8',
	            'os' : 'ios',
	            'Accept-Encoding' : 'gzip, deflate',
	            'Accept-Language' : 'zh-Hans-CN;q=1, ja-JP;q=0.9, zh-Hant-CN;q=0.8',
	            'imei'  :  '910FDAF8-E600-4ECD-A46F-7EFBACD1E5B6',
	            'User-Agent' : 'Mobile_Pocket',
	            'Content-Length' : '106',
	            'Connection' : 'keep-alive',
	            'Content-Type'  :  'application/json;charset=utf-8'
	        }
	        form = {
	            "type": 0,
	            "limit": 20,
	            "giftUpdTime": 1503766100000,
	            "memberId": 0,
	            "groupId": 0,
	            "lastTime": 0
	        }
	        try:
	            response = requests.post(ajax_url, data=json.dumps(form), headers=header, verify=False)
	        except Exception as e:
	            raise e
	            #print "获取直播列表失败"
	        res_json = response.json()
	        if 'liveList' in res_json['content'].keys():
	            live_list = res_json['content']['liveList']
	            #print "有直播 \n 当前直播人数：%d" % len(live_list)
	            message = ""
	            for live in live_list:
	                live_id = str(live['liveId'])
	                if int(live['memberId']) == link.memberId() and global_live_id != live_id:
	                    global_live_id = live_id
	                    live_starttime = stamp_to_str(live['startTime'])
	                    live_streampath = str(live['streamPath'])
	                    live_title = str(live['subTitle'])
	                    live_type = int(live['liveType'])
	                    live_url = 'https://h5.48.cn/2017appshare/memberLiveShare/index.html?id=%s' % str(live_id)
	                    if live_type == 1:
	                        message += "小偶像【%s】开视频直播啦 \n %s \n 开始时间：%s \n 直播地址：%s" % (link.idol_name(), live_title, live_starttime, live_url)
	                    if live_type == 2:
	                        message += "小偶像【%s】开电台啦 \n %s \n 开始时间：%s \n 电台地址：%s" % (link.idol_name(), live_title, live_starttime, live_url)
	                bot.SendTo(group, message)
	    



#定时任务，每分钟执行一次
#查询聚聚房间
#房间id在link.py中设置
@qqbotsched(hour='0-23', minute='0-59')
def get_juju(bot):
	global msgidClient_array
	global firstcheck_juju
	#仅需修改播报的qq群号
	gl = bot.List('group', '606642799')
	if gl is not None:
	    for group in gl:
	        ajax_url = 'https://pjuju.48.cn/imsystem/api/im/v1/member/room/message/chat'
	        header = {
	            'Host' : 'pjuju.48.cn',
	            'app-type' : 'fans',
	            'Accept' : '*/*',
	            'version' :'4.1.8',
	            'os' : 'ios',
	            'Accept-Encoding' : 'gzip, deflate',
	            'Accept-Language' : 'zh-Hans-CN;q=1, ja-JP;q=0.9, zh-Hant-CN;q=0.8',
	            'imei'  :  '910FDAF8-E600-4ECD-A46F-7EFBACD1E5B6',
	            'token'  :  '1gJprYYthZJR0Jv9lMKvvGpqeUpcscwzTSnrDthdqt57VJ/ZXhvi/Lq8hvJQ2/fUVqxq/ZDF/Dd2vMWuBlMO3/n3fRYliMBk',
	            'User-Agent' : 'Mobile_Pocket',
	            'Content-Length' : '85',
	            'Connection' : 'keep-alive',
	            'Content-Type'  :  'application/json;charset=utf-8'
	        }
	        form = {
	            "lastTime": 0,
	            "limit": 10,
	            "roomId": link.roomId()
	        }
	        response = requests.post(ajax_url, data=json.dumps(form), headers=header, verify=False).json()
	        datas = response['content']['data']
	        jujumsg = ""
	        if firstcheck_juju == 0:
	            for data in datas:
	                msgidClient_array.append(data['msgidClient'])
	            firstcheck_juju = 1
	        for data in datas:
	            if data['msgidClient'] in msgidClient_array:
	                continue
	            msgidClient_array.append(data['msgidClient'])
	            extInfo = json.loads(data['extInfo'])
	            if data['msgType'] == 0:
	                if 'text' in extInfo.keys():
	                    #print "普通消息"
	                    jujumsg = ('[%s]\n【口袋48房间消息】\n %s：%s\n' % (data['msgTimeStr'], extInfo['senderName'], extInfo['text'])) + jujumsg
	                elif 'messageText' in extInfo.keys():
	                    #print "翻牌"
	                    jujumsg = ('[%s]\n【口袋48房间翻牌】\n %s：%s\n 【被翻牌】%s：%s\n' % (data['msgTimeStr'], extInfo['senderName'], extInfo['messageText'], extInfo['faipaiName'], extInfo['faipaiContent'])) + jujumsg
	            elif data['msgType'] == 1:
	                bodys = json.loads(data['bodys'])
	                #print "图片消息"
	                if 'url' in bodys.keys():
	                    jujumsg = ('[%s]\n【口袋48房间图片】\n %s：%s\n' % (data['msgTimeStr'], extInfo['senderName'], bodys['url'])) + jujumsg
	            elif data['msgType'] == 2:
	                #print "语音消息"
	                if 'url' in bodys.keys():
	                    jujumsg = ('[%s]\n【口袋48房间语音】\n %s：%s\n' % (data['msgTimeStr'], extInfo['senderName'], bodys['url'])) + jujumsg
	        bot.SendTo(group, jujumsg)
	    
