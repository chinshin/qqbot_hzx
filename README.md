# qqbot_hzx v2.1
[TOC]
## 简介

**2018.02.12：不再维护，移至酷Q [chinshin/CQBot_hzx](https://github.com/chinshin/CQBot_hzx)**

基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)2.0版本


本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) 


环境：`Python 2.7` + `Python 3.5+`
库：`requests`&`json`&`sys`&`urllib3`&`time`&`copy`&`re`&`random`&`ConfigParser`&`os`


##  更新记录

**2018.02.12更新**：本项目已经稳定，不再开发，（随缘）维护。由于基于web QQ的qqbot稳定性不足，现开发平台移至酷Q，详情可见：[chinshin/CQBot_hzx](https://github.com/chinshin/CQBot_hzx)


**2018.02.05更新**：完善了python3版本，增加了对口袋偶像翻牌功能的识别;更新了部分口袋房间ID


**2018.01.20更新**：测试版：增加python3支持


增加了py3文件夹。

基于python3修改了原代码，使用python3环境的用户请使用py3文件夹下的文件。

注意，该版本只经过了简单功能测试，保证大部分功能可用，可能存在部分不兼容问题。如果出现问题，请在 [Issues](https://github.com/chinshin/qqbot_hzx/issues) 中反馈。

另外，发现本插件在Windows环境下存在不同形式的解码问题（UnicodeDecodeError）。


**2018.01.12更新**：摩点查询逻辑更新

```
代码改动：
start.py：
	1.引入time库；
	2.摩点查询逻辑由获取评论总数改为基于时间更新。
modian.py：
	1.引入time库；
	2.删除diff()和num()方法；
	3.增加newOrder(stamp, delay)方法，基于10位时间戳和查询时间段的查询逻辑。极大减少了request次数，更有效率。
```


**2018.01.10更新**：v2.1 更新

```
1.移除了gettoken.py这个手动获取token脚本，现在token获取为自动（需在setting.conf中设置用户名和密码）；
2.增加了roomID.conf和setting.conf两个配置文件。
	roomID.conf中包括了截止2018年1月9日所有能获取的现役成员房间号，该文件无需改动。
	此外，现在所有设置均在setting.conf中修改；
3.增加了v2.3.conf，这是qqbot的配置文件（卢静一般为~/.qqbot-tmp/v2.3.conf）仅供参考；
4.修改了koudai48.py，在定时任务中增加了查询失败后自动更新token的功能；
5.修改了setting.py，现在setting.py作用是从setting.conf中获取配置；
6.修改了start.py，现在start.py中的关键字回复只在setting.conf中指定的群中生效；
```
下一个版本目标是适配python3.5+环境


**2018.01.05更新**：QQbot更新，腾讯关闭了获取真实QQ号的接口。请立即更新qqbot：在终端中输入`pip install --upgrade qqbot`，并在`setting.py`中将groupid中的QQ群号换成QQ群昵称。


**2017.12.27更新**：口袋48数据格式更新，代码简化；增加了主文件`group.py`，可以对群内消息进行管理操作；优化了`setting.py`的结构，更具可观性。


**2017.12.16更新**：v2.0发布。模块化重构了整个项目，使之更简洁；根据摩点（微打赏）官方API重构了摩点（微打赏）查询，更加简洁高效；增加手动获取口袋48登录信息（token），token存活期为30天。

## 文件介绍


`start.py`  ***启动文件1***，包含关键字回复和定时任务


`koudai48.py` ***启动文件2***，包含口袋48查询的定时任务


`group.py` ***启动文件3***，包含QQ群扩展功能


`setting.py`  读取配置文件中的设置


`modian.py`  摩点（微打赏）相关


`weibo.py`  新浪微博相关


`roomID.conf`  包含所有成员名与房间号


`setting.conf`  配置文件


`v2.3.conf`  qqbot配置文件（仅供参考）



```
已删除：
gettoken.py  手动获取token（口袋48登录用）
```



##  安装和配置
  1.[qqbot安装](https://github.com/pandolia/qqbot#二安装方法):`pip install qqbot`
  
  2.运行一次qqbot：终端输入`qqbot`运行，然后在新终端中输入`qq stop`退出。
  
  3.[插件配置](https://github.com/pandolia/qqbot#插件的配置-pluginpath-和-plugins-)：将`qqbot_hzx/`下8个文件拷贝至` ~/.qqbot-tmp/plugins`

  4.修改`setting.conf`中所有参数
  
  5.[修改配置文件](https://github.com/pandolia/qqbot#配置文件的使用方法)，可以参考项目中的`v2.3.conf`。将`start.py`以及`koudai48.py`以及`group.py`添加到需要加载的插件列表。在终端输入`qqbot -u somebody`来运行
  
  6.详细信息请阅读[qqbot说明文档](https://github.com/pandolia/qqbot/blob/master/README.MD)

##  功能
`start.py`：


  * 设置定时任务
    - 每分钟（可修改）查询指定微打赏项目，如果有人集资则返回信息
    - 每五分钟获取微博信息，如有更新则返回信息
    - 每天重启之前的信息提醒
  * 设置关键字回复
    - 回复“wds”或者“集资”：返回集资链接
    - 回复“集资榜”或者“jzb”：返回集资榜top20
    - 回复“打卡榜”或者“dkb”：返回打卡榜top20
    - 回复“欢迎新人”：返回安利信息
    - 等等


`setting.conf`：


  * 设置小偶像名字（在roomID.conf中确认一下是否存在）以及队伍归属（snh bej gnz shy ckg中一项）
  * 设置摩点（微打赏）相关参数
    - pro_id即摩点项目网址后的数字
    - 摩点网项目网址
    - 摩点网项目名称
  * 设置口袋48相关参数
  	- 用户名：口袋48手机号
  	- 密码：口袋48密码
  	- 输入用户名和密码后，token会在qqbot运行后自动获取
  * QQ群设置
  	- QQ群名称
  	- 安利小偶像的信息
  	- 禁言词语（需设置成管理员），留空则不禁言
  * 微博相关参数
    - containerID和api_url
    - 设置方法可参考[nikochan.cc](http://www.nikochan.cc/2017/08/03/Crawlerweibonotloggin/)
  * 代理设置
	- 一般无需设置，只有频繁大量查询口袋48相关的时候必须设置


`koudai48.py`：


  * 查询制定成员口袋房间，返回新消息
  * 直播提醒
  * 查询失败则自动检查token并自动获取token


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