# -*- coding: utf-8 -*-


# qq群号
def groupid():
    id = 'QQ群号填这里'
    return id


# 微打赏名称
def wds_name():
    wds_name = "项目名称填在这里"
    return wds_name


# 微打赏网址 建议使用短地址t.cn
def wds_url():
    wds_url = "摩点（微打赏）地址填这里"
    return wds_url


# 微打赏项目对应pro_id
def pro_id():
    pro_id = 10285
    return pro_id


# 口袋48:memberId
# 黄子璇id:528331
def memberId():
    memberId = 528331
    return memberId


# 口袋48:roomId
# 黄子璇roomId：9108720
def roomId():
    roomId = 9108720
    return roomId


# 口袋48:小偶像名字
def idol_name():
    idol_name = "黄子璇"
    return idol_name


# 手机网页版微博地址
def weibo_url():
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076036212622903'
    return url


# weibo container id
def weibo_id():
    id = 1076036212622903
    return id


# 设置口袋48账号密码
def user(type):
    user = '口袋48用户名'
    password = '密码'
    if type == 1:
        return user
    elif type == 2:
        return password


# 手动运行gettoken.py手动获取token，然后填入下方
# token 存活时间为 30 天
def token():
    token = 'token填这里'
    return token
