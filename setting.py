# -*- coding: utf-8 -*-


# 小偶像名字
def idol_name():
    idol_name = "黄子璇"
    return idol_name


# ----------------------摩点微打赏设置----------------------


# 微打赏名称
def wds_name():
    wds_name = "摩点（微打赏）项目未设置\n拿小樱花的测试一下"
    return wds_name


# 微打赏网址 建议使用短地址t.cn
def wds_url():
    wds_url = "摩点（微打赏）地址未设置"
    return wds_url


# 微打赏项目对应pro_id
def pro_id():
    pro_id = 10250
    return pro_id


# --------------------------------------------------------


# ----------------------口袋48设置----------------------


# # 口袋48:memberId
# # 黄子璇id:528331
# def memberId():
#     memberId = 528331
#     return memberId


# 口袋48:roomId
# 黄子璇roomId：9108720
def roomId():
    roomId = 9108720
    return roomId


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
    token = 'token填在这里'
    return token


# --------------------------------------------------------


# ----------------------qq群设置----------------------


# qq群号
def groupid():
    id = 'BEJ48-黄子璇应援会'
    return id


# 欢迎信息
def welcome():
    msg = "欢迎聚聚加入BEJ48-黄子璇的应援群！" + '\n' + "大家可以叫子璇宝宝叁玖 ~" + '\n' +\
        "叁玖是一只土生土长的北京姑娘，生日是5月20日，生在2002年的金牛座。" + '\n' + "九春三秋，只为遇见你。" +\
        '\n' + "希望你我可以相知相识～" + '\n' + '\n' + "三分钟带你领略甜甜的叁玖" + '\n' +\
        "首演unit《爱的魔法》：http://t.cn/RolMikW" + '\n' + '\n' +\
        "出道以来第五场公演unit《爱的魔法》：http://t.cn/RCb8QBn" + '\n' + '\n' +\
        "第四届总决选拉票公演：http://t.cn/RCb8gzH" + '\n' + '\n' +\
        "更多补档内容请戳b站：BEJ48-黄子璇应援会 http://t.cn/RCbRLjZ" + '\n' + '\n' +\
        "最后也请聚聚关注下叁玖的微博与超级话题吧" + '\n' + "@BEJ48-黄子璇：http://t.cn/RCbRiAe" +\
        '\n' + "@BEJ48-黄子璇应援会：http://t.cn/RCbRNu1" + '\n' +\
        "#黄子璇#超级话题：http://t.cn/RCbRQg2" + '\n' + '\n' +\
        "让我们陪着这个刚出道不久的小孩子长大，看着她成为更好的人，一起给她最好的应援吧~（鞠躬）"
    return msg


# 关键词触发
# 禁言关键词,留空则无禁言
def shutup():
    # 范例：wordlist = ['fuck', 'cao']
    wordlist = []
    return wordlist


# --------------------------------------------------------


# ----------------------微博设置----------------------


# 手机网页版微博地址
def weibo_url():
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076036212622903'
    return url


# weibo container id
def weibo_id():
    id = 1076036212622903
    return id


# --------------------------------------------------------
