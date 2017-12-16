# qqbot_hzx v2.0
[TOC]
## 简介
基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)2.0版本


本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) 


环境：`Python 2.7`
库：`requests`&`json`&`sys`&`urllib3`&`time`&`copy`&`re`


##  更新记录


**2017.12.16更新**：v2.0发布。模块化重构了整个项目，使之更简洁；根据摩点（微打赏）官方API重构了摩点（微打赏）查询，更加简洁高效；增加手动获取口袋48登录信息（token），token存活期为30天。

## 文件介绍


`start.py`  启动文件，包含关键字回复和定时任务


`koudai48.py` 启动文件2，包含口袋48查询的定时任务


`setting.py`  所有的参数设置


`modian.py`  摩点（微打赏）相关


`weibo.py`  新浪微博相关


`gettoken.py`  手动获取token（口袋48登录用）



##  安装和配置
  1.[qqbot安装](https://github.com/pandolia/qqbot#二安装方法):`pip install qqbot`
  
  2.运行一次qqbot：终端输入`qqbot`，运行，然后退出。
  
  3.[插件配置](https://github.com/pandolia/qqbot#插件的配置-pluginpath-和-plugins-)：将`qqbot_hzx/`下6个文件拷贝至` ~/.qqbot-tmp/plugins`

  4.修改`setting.py`中所有参数
  
  5.[修改配置文件](https://github.com/pandolia/qqbot#配置文件的使用方法)，将`start.py`以及`koudai48.py`添加到需要加载的插件列表。在终端输入`qqbot -u somebody`来运行
  
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




