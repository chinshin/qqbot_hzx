# -*- coding: utf-8 -*-
import requests
import math
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def getdata():
	ajax_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6212622903&containerid=1076036212622903'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	form = {
	    'type': 'uid',
	    'value': 6212622903,
	    'pro_id': 1076036212622903
	}

	response = requests.post(ajax_url, form, headers=header).json()
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
	return str(datas['mblog']['text'])

def getretweetweibo():
	datas = getdata()
	return str(datas['mblog']['raw_text'])

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