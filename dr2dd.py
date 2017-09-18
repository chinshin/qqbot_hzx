# -*- coding: utf-8-*-
import re

#除去字符串中的html标签
def dr_to_dd(dr_str):
    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',dr_str)
    return str(dd)

