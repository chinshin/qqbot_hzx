# -*- coding: utf-8 -*-
import link
import requests
import math
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#消去https请求的不安全warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#引入正则
import re


#返回微打赏的地址+网址
def start():
	wds_name = link.wds_name()
	wds_url = link.wds_url()

	return (wds_name + "\n" + wds_url)
	pass


#请求头
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}


#
#获取comment数量
def checkNum():
	#获取wds项目页面
	wds_url = 'https://wds.modian.com/show_weidashang_pro/%d' % (link.pro_id())
	content = requests.get(wds_url, headers = header).text
	#正则匹配评论总数
	res_div = r'<div class="project-comment".*?>.*?<div class="s-t line1px">.*?<span>(.*?)</span>' 
	m_span =  re.findall(res_div,content,re.S)
	return int(m_span[0])
#


#
#获取评论列表
def return_comment(difference):
	ajax_url = 'https://wds.modian.com/ajax/comment_list'
	form = {
	    'page': 1,
	    'post_id': link.post_id(),
	    'pro_id': link.pro_id()
	}
	comment = []
	des = []
	result = ""
	total = 0
	while True:
	    response = requests.post(ajax_url, form, headers=header).json()
	    if response['status'] == -1:
	        break
	    html = response['data']['html']
	    form['page'] += 1
	    #对字典中返回的html进行正则匹配
	    #针对空评论无集资进行了优化
	    res_nick = r"""<span class="nick">(.*?)</span>.*?<div class="comment">.*?(<span class="nick_sup">.*?([0-9]+\,[0-9]+\.[0-9]+|[0-9]+\.[0-9]+|[0-9]+).*?|<span>(.*?))</span>.*?</div>"""
	    m_nick = re.findall(res_nick, html, re.S)
	    comment += m_nick
	for cmt in comment:
		#des为包含（支持者名称，支持的金额）的序列
	    des.append((cmt[0], cmt[2].replace(',','')))

	for i in range(0, int(difference)):
	    try:
	        try_supmoney = float(des[i][1])
	    except Exception as e:
	        result = result + "微打赏被ID为：" + str(des[i][0]) + " 的聚聚评论了" + '\n'
	    else:
	        result = result + "ID: " + str(des[i][0]) + " 的聚聚刚刚在【" + link.wds_name() + "】中支持了 ¥" + str(des[i][1]) + '\n' + "感谢这位聚聚对" + link.idol_name() + "的支持" + '\n'
	for j in des:
	    try:
	        total += float(j[1])
	    except Exception as e:
	        pass
	result = result + "【微打赏】：" + link.wds_url() + '\n' + "目前集资总额：¥" + str(total)
	return result

