# Coursera 视频无法播放

Coursera网站上的视频，由于墙的问题，dns解析出现问题，使用以下方法解决。（Mac系统解决方法在[这里](https://blog.csdn.net/neo_liukun/article/details/83614626)）

Windows系统：找到文件：`C:\Windows\System32\drivers\etc\hosts`，用管理员模式打开，在最后一行加上：`52.84.246.72 d3c33hcgiwev3.cloudfront.net`，保存即可。