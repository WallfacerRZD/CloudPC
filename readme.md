# CloudPC

>一款基于flask的应用
>监听电脑的2333端口达到用手机或者其他设备远程控制电脑的目的
## 使用环境

> python2.7

## 依赖的python库
>flak
>openCV

## 当前版本功能
>1. 电脑定位
>2. 关机, 锁屏
>3. 执行cmd命令
>4. 摄像头快照
>5. 摄像头直播(具体实现请看[这里](https://blog.miguelgrinberg.com/post/video-streaming-with-flask))
>5. 桌面截屏

## 使用方法
1. 开启qq邮箱POP3/SMTP服务
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/0.JPG)
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/1.JPG)
- 根据提示发送短信
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/2.JPG)
- 复制授权码
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/3.JPG)

2. 填写配置文件(用utf-8无BOM模式保存)
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/4.JPG)

3. 有python2.7环境的运行listener.py,没有python环境的运行listener.exe

4. 在联网环境下,会有一封邮件发送到配置文件中的邮箱里,访问邮件中的地址即可


## 运行截图
- ![](https://github.com/WallfacerRZD/CloudPC/blob/master/pictures/5.JPG)
- 左右滑动页面,选择功能
## 注意事项
1. 由于插件原因,建议向右滑动选择功能
2. 如果发现点击按钮后没有反应,可能是登录过期,请刷新页面重新登录.也有可能是插件的BUG,请刷新页面
3. 总之如果出现BUG,请刷新一下哦...._(:3」∠)_
4. 欢迎提出issue!!(｡･ω･｡)
