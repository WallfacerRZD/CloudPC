# CloudPC

>一款基于flask的应用
>监听电脑的2333端口达到远程控制电脑的目的
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
![](0.jpg)
![](1.jpg)
根据提示发送短信
![](2.jpg)
复制授权码
![](3.jpg)

2. 填写配置文件
![](4.jpg)

3. 有python2.7环境的运行listener.py,没有python环境的运行listener.exe

4. 在联网环境下,会有一封邮件发送到配置文件中的邮箱里,访问邮件中的地址即可