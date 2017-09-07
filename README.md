# qqbot_hzx
基于qqbot的QQ微打赏机器人(BEJ48-黄子璇)</br></br>
本项目是一个插件，依赖于: [pandolia/qqbot](https://github.com/pandolia/qqbot) </br></br>
环境：`Python 2.7/3.4+ `

  ## 介绍
`start.py`  启动文件，包含关键字回复和定时任务</br>
`wds.py`  返回集资名和集资链接</br>
`wds20.py`  返回集资榜TOP20</br>
`link.py`  修改集资名、集资链接等参数</br>

  ##  安装和配置
  1.[qqbot安装](https://github.com/pandolia/qqbot#二安装方法):`pip install qqbot`
  
  2.运行一次qqbot：终端输入`qqbot`，运行，然后退出。
  
  3.[插件配置](https://github.com/pandolia/qqbot#插件的配置-pluginpath-和-plugins-):
  将`qqbot_hzx/`下四个文件拷贝至` ~/.qqbot-tmp/plugins`
  
  4.[修改配置文件](https://github.com/pandolia/qqbot#配置文件的使用方法)，在终端输入`qqbot -u somebody`来运行
  
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
    
