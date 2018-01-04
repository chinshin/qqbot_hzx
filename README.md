# qqbot_hzx v2.0
[TOC]
## 简介
基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)2.0版本


本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) 


环境：`Python 2.7`
库：`requests`&`json`&`sys`&`urllib3`&`time`&`copy`&`re`


##  更新记录


**2018.01.05更新**：QQbot更新，腾讯关闭了获取真实QQ号的接口。请立即更新qqbot：在终端中输入`pip install --upgrade qqbot`，并在`setting.py`中将groupid中的QQ群号换成QQ群昵称。


**2017.12.27更新**：口袋48数据格式更新，代码简化；增加了主文件`group.py`，可以对群内消息进行管理操作；优化了`setting.py`的结构，更具可观性。


**2017.12.16更新**：v2.0发布。模块化重构了整个项目，使之更简洁；根据摩点（微打赏）官方API重构了摩点（微打赏）查询，更加简洁高效；增加手动获取口袋48登录信息（token），token存活期为30天。

## 文件介绍


`start.py`  启动文件，包含关键字回复和定时任务


`koudai48.py` 启动文件2，包含口袋48查询的定时任务


`group.py` 启动文件3，包含QQ群扩展功能


`setting.py`  所有的参数设置


`modian.py`  摩点（微打赏）相关


`weibo.py`  新浪微博相关


`gettoken.py`  手动获取token（口袋48登录用）



##  安装和配置
  1.[qqbot安装](https://github.com/pandolia/qqbot#二安装方法):`pip install qqbot`
  
  2.运行一次qqbot：终端输入`qqbot`，运行，然后退出。
  
  3.[插件配置](https://github.com/pandolia/qqbot#插件的配置-pluginpath-和-plugins-)：将`qqbot_hzx/`下7个文件拷贝至` ~/.qqbot-tmp/plugins`

  4.修改`setting.py`中所有参数
  
  5.[修改配置文件](https://github.com/pandolia/qqbot#配置文件的使用方法)，将`start.py`以及`koudai48.py`以及`group.py`添加到需要加载的插件列表。在终端输入`qqbot -u somebody`来运行
  
  6.详细信息请阅读[qqbot说明文档](https://github.com/pandolia/qqbot/blob/master/README.MD)

##  功能
`start.py`：


  * 设置定时任务
    - 每分钟（可修改）查询指定微打赏项目，如果有人集资则返回信息
    - 每五分钟获取微博信息，如有更新则返回信息
    - 每天重启之前的信息提醒
  * 设置关键字回复
    - 回复“wds”或者“集资”：返回集资链接
    - 回复“wds20”或者“rank”：返回集资榜top20
    - 回复“欢迎新人”：返回安利信息
    - 等等


`setting.py`：


  * 设置播报的QQ群号
  * 设置摩点（微打赏）相关参数
    - pro_id即摩点项目网址后的数字
  * 设置口袋48相关参数
  * 微博相关参数
    - 设置方法可参考[nikochan.cc](http://www.nikochan.cc/2017/08/03/Crawlerweibonotloggin/)


`gettoken.py`：


  * 手动获取token


`koudai48.py`：


  * 查询制定成员口袋房间，返回新消息
  * 直播提醒


`modian.py`：


  * 摩点相关查询
    - 项目每笔集资
    - 金额榜／打卡榜
    - 总览


`weibo.py`：


  * 返回微博相关信息
    - 新微博（原创／转发）（带图／不带图）


`group.py`：


  * 群操作
    - 新成员欢迎
    - 被at操作
    - 关键词禁言
    - 查撤回