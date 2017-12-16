# qqbot_hzx v2.0
[TOC]
## 简介
基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)2.0版本


本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) 


环境：`Python 2.7`
库：`requests`&`json`&`sys`&`urllib3`&`time`&`copy`&`re`


##  更新记录

<<<<<<< HEAD
=======
  ##  更新

2017.12.09更新：针对微博（m.weibo.com）返回数据格式改动作出更新


2017.10.19更新：针对微打赏网站数据改版进行了查询方法的更新，并将start.py中微打赏查询方法移动到了`wds.py`中。(tip：查询方法中的请求地址、form格式及参数、返回的数据均有变化)
>>>>>>> origin/master

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
  
<<<<<<< HEAD
  6.详细信息请阅读[qqbot说明文档](https://github.com/pandolia/qqbot/blob/master/README.MD)

##  功能
`start.py`：
=======
  5.详细信息请阅读[qqbot说明文档](https://github.com/pandolia/qqbot/blob/master/README.MD)
  
 6.[koudai48.py](https://github.com/chinshin/qqbot_hzx/blob/a2a810deeb91c20df5edfc0fa32590057e786027/koudai48.py#L111)中的token需手动设置，存活期为29天。


>>>>>>> origin/master


  * 设置定时任务
    - 每分钟（可修改）查询指定微打赏项目，如果有人集资则返回信息
    - 每五分钟获取微博信息，如有更新则返回信息
    - 每天重启之前的信息提醒
  * 设置关键字回复
<<<<<<< HEAD
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



=======
    * 回复“wds”或者“集资”：返回集资链接
    * 回复“wds20”或者“rank”：返回集资榜top20
    * 回复“欢迎新人”：返回安利信息

通过`link.py`：</br>
  * 设置需要监控的微打赏信息
    * `wds_name`微打赏名称
    * `wds_url` 微打赏链接
    * `moxi_id` 微打赏moxi_id
    * `pro_id`  微打赏pro_id


* 注意！20171019微打赏改版后`moxi_id`变更为`post_id`






    ### moxi_id&pro_id 查询方法（chrome为例）
    1.打开新标签页，右键“检查”，弹出界面
    
    2.点击第一行Network，然后点击第四行XHR
    
    3.在chrome地址栏中输入具体的微打赏项目地址，如https://wds.modian.com/show_weidashang_pro/7371
    
    4.向下浏览页面，直至在XHR下出现一个或多个ajax_comment
    
    5.单击任意一个ajax_comment，在右侧标签中选择Headers
    
    6.滚动headers下页面到最后Form Data，即可看到moxi_id和pro_id

2017.09.08新增:</br>
通过`weibo.py`：</br>
  * 设置需要监控的微博信息
    * `ajax_url` 
    * `value`
    * `pro_id`

设置方法可参考[nikochan.cc](http://www.nikochan.cc/2017/08/03/Crawlerweibonotloggin/)


2017.09.16新增:


通过`link.py`：
* 设置口袋48相关参数（抓包）
  * `roomId`
  * `memberId`
>>>>>>> origin/master

