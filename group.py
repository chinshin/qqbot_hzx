# -*- coding: utf-8 -*-
from qqbot import qqbotsched
from qqbot.utf8logger import INFO
from qqbot.utf8logger import WARN
import copy
import setting


groupid = str(setting.groupid())
global firstcheck
global chatdetail
chatdetail = []
firstcheck = True


# 新成员入群欢迎
@qqbotsched(hour='0-23', minute='0-59')
def task(bot):
    global firstcheck
    new_member = []
    # g is list
    g = bot.List('group', groupid)
    if firstcheck is True:
        bot.Update(g[0])
        firstcheck = False
    if g is None:
        WARN('向 QQ 服务器请求联系人列表和资料失败')
    elif not g:
        INFO('该联系人列表内没有和 cinfo 匹配的联系人')
    elif g:
        # group_* is object
        ml_old = copy.copy(bot.List(g[0]))
        # update group_member list
        if bot.Update(g[0]):
            ml_latest = copy.copy(bot.List(g[0]))
            if len(ml_latest) > len(ml_old):
                for mb in map(str, ml_latest):
                    if mb not in map(str, ml_old):
                        new_member.append(mb)
                for group in g:
                    msg = '欢迎'
                    if (len(ml_latest) - len(ml_old)) < len(new_member):
                        msg += str(len(ml_latest) - len(ml_old)) + '位新聚聚加入本群'
                    else:
                        for vl in new_member:
                            msg += '新' + str(vl)
                        msg += '加入本群'
                    bot.SendTo(group, msg)
                    bot.SendTo(group, setting.welcome())
                    new_member = []
        else:
            WARN('更新联系人列表和资料失败')


# 关键词触发
def onQQMessage(bot, contact, member, content):
    global chatdetail
    # 被at操作
    if '@ME' in content:
        bot.SendTo(contact, member.name + '我是废物机器人2.0，输入 help 可查看口令')
    #
    if contact.ctype == 'group':
        # shut up
        if setting.shutup():
            for shutup_keyword in setting.shutup():
                if shutup_keyword in content:
                    shutmember(bot, contact, member, content)
        #
        # 查撤回
        if contact.nick == groupid:
            chatdetail.append(content)
            if len(chatdetail) > 6:
                chatdetail = chatdetail[-6:]
            if content == '-查撤回':
                cd_msg = '最近五条聊天记录：\n'
                cd_num = 1
                for cd in chatdetail[-6:-1]:
                    cd_msg += '【第' + str(cd_num) + '条】' + cd + '\n'
                    cd_num += 1
                bot.SendTo(contact, cd_msg)


def shutmember(bot, contact, member, content):
    gl = bot.List('group', groupid)
    if gl:
        group = gl[0]
        membs = bot.List(group, member.name)
        if membs:
            bot.GroupShut(group, membs, 300)


#
