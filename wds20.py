# -*- coding: utf-8 -*-
import requests
import math
import json
import sys
import link

#返回微打赏项目集资总榜top20
#无须修改

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def start():
	wds_name = link.wds_name()
	wds_url = link.wds_url()
	ajax_url = 'https://wds.modian.com/ajax_backer_list'
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

	form = {
	    'pro_id': link.pro_id(),
	    'type': 1,
	    'page': 1,
	    'pageSize': 20
	}
	rank = []
	result = "---" + wds_name + "·TOP20---" + '\n'
	no = 1
	total = 0.0
	while True:
	    response = requests.post(ajax_url, form, headers=header).json()
	    if response['status'] == '-1':
	        break
	    datas = response['data']
	    for data in datas:
	        rank.append((data['nickname'] , data['total_back_amount']))
	    form['page'] += 1
	for i in rank:
	    if no <21:
	        result = result + "【第" + str(no) + "名】ID：" + str(i[0]) + " 支持了" + str(i[1]) + "元" + '\n'
	    no += 1
	    total += float(i[1])
	result = result + "【微打赏】：" + wds_url + '\n' + "目前集资总额：¥" + str(total)
	print(result)
	return result
	pass
