主要包括 模块：
1. deploy 此模块 用于部署 本地页面
2. noteshare 此模块结合 source.json 可以生成有等待时延和等待动画的跳转页面
3. gindex 此模块结合 index和config.json 生成 index页面，并启动本地服务器
配置文件为index，---表示分隔符
eg:
title1
desp1
/articles/my_blog1
---
title2
desp2
/articles/my_blog2

可以设置 每页的item数量，markdown格式的css渲染，以及blog的title
