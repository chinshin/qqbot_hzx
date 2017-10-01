# -*- coding: utf-8 -*-
import requests
import math
import json
import dr2dd
import copy
import sys

reload(sys)
sys.setdefaultencoding('utf8')

#global response
def init():
	#更改ajax_url
	ajax_url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076036212622903'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	#更改value&pro_id
	form = {
	    'containerid': 1076036212622903,
	}

	response = requests.post(ajax_url, form, headers=header).json()
	return response

def getdata(i):
	response = copy.copy(init())
	datas = response['cards'][i]
	return datas


def checkid(i):
	datas = getdata(i)
	return str(datas['mblog']['id'])

def checkretweet(i):
	datas = getdata(i)
	if datas['mblog'].get('retweeted_status') == None:
	    return False
	else:
	    return True

def getweibo(i):
	datas = getdata(i)
	r_weibo = str(datas['mblog']['text'])
	#20170917增加
	#微博内容去除html标记功能
	r2d_weibo = dr2dd.dr_to_dd(r_weibo)
	return r2d_weibo

def getretweetweibo(i):
	datas = getdata(i)
	r_retweeetweibo = str(datas['mblog']['raw_text'])
	#20170917增加
	#微博内容去除html标记功能
	r2d_retweeetweibo = dr2dd.dr_to_dd(r_retweeetweibo)
	return r2d_retweeetweibo

def checkpic(i):
	datas = getdata(i)
	if datas['mblog'].get('pics') == None:
	    return False
	else:
	    return True

def getpic(i):
	datas = getdata(i)
	picurl = ""
	picnum = 1
	for pic in datas['mblog']['pics']:
	    picurl = picurl + "微博配图" + str(picnum) + "：" +  str(pic['url']) + '\n'
	    picnum += 1
	return picurl

def getscheme(i):
	datas = getdata(i)
	return str(datas['scheme'])

def getidarray():
	weibo_id_array = []
	response = copy.copy(init())
	cards = response['cards']
	for card in cards:
	    try:
	        weibo_id = card['mblog']['id']
	    except Exception as e:
	        weibo_id_array.append("0")
	    else:
	        weibo_id_array.append(weibo_id)
	return weibo_id_array

#20170926
#现在查询新微博：返回前5个微博id（如果是微博广告位，id为0）
def get_5_idarray():
	weibo_id_array = []
	response = copy.copy(init())
	cards = response['cards']
	for i in range(0,5):
	    datas = cards[i]
	    try:
	        weibo_id = datas['mblog']['id']
	    except Exception as e:
	        weibo_id_array.append("0")
	    else:
	        weibo_id_array.append(weibo_id)
	return weibo_id_array










