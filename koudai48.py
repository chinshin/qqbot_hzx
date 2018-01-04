# -*- coding: utf-8 -*-
from qqbot import qqbotsched
import json
import time
import sys
import setting
from qqbot.utf8logger import WARN
import requests
import urllib3
reload(sys)
sys.setdefaultencoding('utf8')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

global msgTime_array
global firstcheck_juju

msgTime_array = []
firstcheck_juju = 0
groupid = setting.groupid()


# 13位unix时间戳（ms）转为字符串时间
def stamp_to_str(timestamp):
    x = time.localtime(timestamp / 1000)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return time_str


# 定时任务，每分钟执行一次
# 查询聚聚房间
# 房间id在setting.py中设置
@qqbotsched(hour='0-23', minute='0-59')
def get_juju(bot):
    global msgTime_array
    global firstcheck_juju
    # 仅需修改播报的qq群昵称
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            ajax_url = 'https://pjuju.48.cn/imsystem/api/im/v1/member/room/message/mainpage'
            header = {
                'Host': 'pjuju.48.cn',
                'version': '5.0.1',
                'os': 'android',
                'Accept-Encoding': 'gzip',
                'IMEI': '866716037825810',
                'User-Agent': 'Mobile_Pocket',
                'Content-Length': '67',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/json;charset=utf-8',
                'token': setting.token()
            }
            form = {
                "lastTime": 0,
                "limit": 10,
                "chatType": 0,
                "roomId": setting.roomId()
            }
            response = requests.post(
                ajax_url,
                data=json.dumps(form),
                headers=header,
                verify=False
            ).json()
            if response['status'] == 200:
                datas = response['content']['data']
                # first check
                if firstcheck_juju == 0:
                    for data in datas:
                        msgTime_array.append(data['msgTime'])
                    firstcheck_juju = 1
                #
                # 控制list长度
                msgTime_array = msgTime_array[-10:]
                #
                for data in datas:
                    msg = ''
                    # 判断重复
                    msgTime_array = sorted(msgTime_array)
                    if data['msgTime'] in msgTime_array or data['msgTime'] < msgTime_array[0]:
                        continue
                    else:
                        msgTime_array.append(data['msgTime'])
                    #
                    # 文字消息
                    extInfo = json.loads(data['extInfo'])
                    if data['msgType'] == 0:
                        if extInfo['messageObject'] == 'text':
                            msg = ('[%s]\n【口袋48房间消息】\n %s：%s' % (data['msgTimeStr'], extInfo['senderName'], extInfo['text']))
                        elif extInfo['messageObject'] == 'faipaiText':
                            # 20171221 16:38 黄子璇(roomid=9108720)发生err：翻牌信息未返回faipaiName
                            try:
                                msg = ('[%s]\n【口袋48房间翻牌】\n %s：%s\n 【被翻牌】%s：%s\n' % (data['msgTimeStr'], extInfo['senderName'], extInfo['messageText'], extInfo['faipaiName'], extInfo['faipaiContent']))
                            except:
                                msg = ('[%s]\n【口袋48房间翻牌】\n %s：%s\n 【被翻牌】%s\n' % (data['msgTimeStr'], extInfo['senderName'], extInfo['messageText'], extInfo['faipaiContent']))
                            #
                        elif extInfo['messageObject'] == 'live':
                            msg = ('小偶像开视频直播啦 \n 直播标题：%s \n 直播封面：%s \n开始时间：%s \n 直播地址：%s' % (extInfo['referenceContent'], 'https://source.48.cn' + extInfo['referencecoverImage'], data['msgTimeStr'], 'https://h5.48.cn/2017appshare/memberLiveShare/index.html?id=' + extInfo['referenceObjectId']))
                        elif extInfo['messageObject'] == 'diantai':
                            msg = ('小偶像开电台啦 \n 电台标题：%s \n 电台封面：%s \n开始时间：%s \n 电台地址：%s' % (extInfo['referenceContent'], 'https://source.48.cn' + extInfo['referencecoverImage'], data['msgTimeStr'], 'https://h5.48.cn/2017appshare/memberLiveShare/index.html?id=' + extInfo['referenceObjectId']))
                        else:
                            msg = '有未知格式的文字消息'
                            WARN('有未知格式的文字消息')
                            WARN(data)
                    # image
                    elif data['msgType'] == 1:
                        bodys = json.loads(data['bodys'])
                        msg = ('[%s]\n【口袋48房间图片】\n %s：%s' % (data['msgTimeStr'], extInfo['senderName'], bodys['url']))
                    # voice
                    elif data['msgType'] == 2:
                        bodys = json.loads(data['bodys'])
                        msg = ('[%s]\n【口袋48房间语音】\n %s：%s' % (data['msgTimeStr'], extInfo['senderName'], bodys['url']))
                    else:
                        msg = '有未知类型的消息'
                        WARN('有未知类型的消息')
                        WARN(data)
                    bot.SendTo(group, msg)
            else:
                WARN('获取口袋房间信息出错')
                WARN(response['message'])
