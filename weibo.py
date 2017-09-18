# -*- coding: utf-8 -*-
import requests
import math
import json
import dr2dd
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getdata():
	#更改ajax_url
	ajax_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6212622903&containerid=1076036212622903'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	#更改value&pro_id
	form = {
	    'type': 'uid',
	    'value': 6212622903,
	    'pro_id': 1076036212622903
	}

	response = requests.post(ajax_url, form, headers=header).json()
	#更改0，如果有置顶微博，则0对应置顶微博，1有时对应微博推荐，根据实际情况修改
	datas = response['cards'][0]
	return datas

def checkid():
	datas = getdata()
	return str(datas['mblog']['id'])

def checkretweet():
	datas = getdata()
	if datas['mblog'].get('retweeted_status') == None:
	    return False
	else:
	    return True

def getweibo():
	datas = getdata()
	r_weibo = str(datas['mblog']['text'])
	#20170917增加
	#微博内容去除html标记功能
	r2d_weibo = dr2dd.dr_to_dd(r_weibo)
	return r2d_weibo

def getretweetweibo():
	datas = getdata()
	r_retweeetweibo = str(datas['mblog']['raw_text'])
	#20170917增加
	#微博内容去除html标记功能
	r2d_retweeetweibo = dr2dd.dr_to_dd(r_retweeetweibo)
	return r2d_retweeetweibo

def checkpic():
	datas = getdata()
	if datas['mblog'].get('pics') == None:
	    return False
	else:
	    return True

def getpic():
	datas = getdata()
	picurl = ""
	picnum = 1
	for pic in datas['mblog']['pics']:
	    picurl = picurl + "微博配图" + str(picnum) + "：" +  str(pic['url']) + '\n'
	    picnum += 1
	return picurl

def getscheme():
	datas = getdata()
	return str(datas['scheme'])

def getidarray():
	weibo_id_array = []
	ajax_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6212622903&containerid=1076036212622903'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
	form = {
	    'type': 'uid',
	    'value': 6212622903,
	    'pro_id': 1076036212622903
	}
	response = requests.post(ajax_url, form, headers=header).json()
	cards = response['cards']
	for card in cards:
	    try:
	        weibo_id = card['mblog']['id']
	    except Exception as e:
	        continue
	    else:
	        weibo_id_array.append(weibo_id)
	return weibo_id_array



