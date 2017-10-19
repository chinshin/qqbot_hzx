# -*- coding: utf-8 -*-
import requests
import math
import json
import link
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re

#返回微打赏项目集资总榜top20



def start():
	#20171019 更新
	#新版ajax_url & form均有变化
	ajax_url = 'https://wds.modian.com/ajax/backer_ranking_list'
	form = {
	    'pro_id': link.pro_id(),
	    'type': 1,
	    'page': 1,
	    'page_size': 20
	}
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
	rank = []
	result = "---" + link.wds_name() + "·TOP20---" + '\n'
	no = 1
	total = 0.0
	while True:
	    response = requests.post(ajax_url, form, headers=header).json()
	    if response['status'] == -1:
	        break
	    html = response['data']['html']
	    form['page'] += 1
	    #正则匹配
	    res_rank = r"""<span class="suport_ran">(.*?)</span>.*?<span class="nickname">(.*?)</span>.*?<span class="money">.*?([0-9]+\.[0-9]{2}?).*?</span>"""
	    m_rank = re.findall(res_rank, html, re.S)
	    rank += m_rank
	for i in rank:
	    if no <21:
	        result = result + "【第" + str(no) + "名】ID：" + str(i[1]) + " 支持了" + str(i[2]) + "元" + '\n'
	    no += 1
	    total += float(i[2])
	result = result + "【微打赏】：" + link.wds_url() + '\n' + "目前集资总额：¥" + str(total)
	return result
