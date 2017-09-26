# qqbot_hzx
基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)


本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) 


环境：`Python 2.7/3.4+ `&`requests`



  ##  更新
  
2017.09.18更新：新增`dr2dd.py`，现在`weibo.py`可以返回无html标签的微博内容了；改进了新微博识别方法，现在删微博后，旧微博不会被播报出来。


2017.09.16更新：增加了口袋48监控功能（直播+聚聚房间） 借鉴了 [billjyc/pocket48](https://github.com/billjyc/pocket48)


2017.09.08更新：增加了微博监控功能 借鉴了 [PYF0311/wds_Crawler](https://github.com/PYF0311/wds_Crawler)

  ## 介绍
`start.py`  启动文件，包含关键字回复和定时任务</br>
`wds.py`  返回集资名和集资链接</br>
`wds20.py`  返回集资榜TOP20</br>
`link.py`  修改集资名、集资链接等参数;口袋48相关参数


2017.09.08新增:</br>
`weibo.py`  返回新浪微博相关参数


2017.09.16新增:</br>
`koudai48.py` 启动文件2，包含口袋48查询的定时任务


2017.09.18新增:</br>
`dr2dd.py`  消去字符串中html标签

  ##  安装和配置
  1.[qqbot安装](https://github.com/pandolia/qqbot#二安装方法):`pip install qqbot`
  
  2.运行一次qqbot：终端输入`qqbot`，运行，然后退出。
  
  3.[插件配置](https://github.com/pandolia/qqbot#插件的配置-pluginpath-和-plugins-):
  将`qqbot_hzx/`下7个文件拷贝至` ~/.qqbot-tmp/plugins`
  
  4.[修改配置文件](https://github.com/pandolia/qqbot#配置文件的使用方法)，将`start.py`以及`koudai48.py`添加到需要加载的插件列表。在终端输入`qqbot -u somebody`来运行
  
  5.详细信息请阅读[qqbot说明文档](https://github.com/pandolia/qqbot/blob/master/README.MD)

  ##  功能
通过`start.py`：</br>
  * 设置定时任务
    * 每五分钟（可修改）查询指定微打赏项目，如果有人集资则返回信息
  * 设置关键字回复
    * 回复“wds”或者“集资”：返回集资链接
    * 回复“wds20”或者“rank”：返回集资榜top20
    * 回复“欢迎新人”：返回安利信息

通过`link.py`：</br>
  * 设置需要监控的微打赏信息
    * `wds_name`微打赏名称
    * `wds_url` 微打赏链接
    * `moxi_id` 微打赏moxi_id
    * `pro_id`  微打赏pro_id


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

