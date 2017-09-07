# -*- coding: utf-8 -*-
import link

#返回微打赏的地址+网址
def start():
	wds_name = link.wds_name()
	wds_url = link.wds_url()

	return (wds_name + "\n" + wds_url)
	pass