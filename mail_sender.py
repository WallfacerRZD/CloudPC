#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1048058400@qq.com"    #用户名
mail_pass="tuhnimgbsntgbecg"   #口令


sender = '1048058400@qq.com'
receivers = ['1048058400@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def send(msg, mode, image_path=''):
        message = MIMEMultipart('alternative')
        message['From'] = Header("Mylaptop", 'utf-8')
        message['To'] = Header("Mr.Dong", 'utf-8')
        message['Subject'] = Header('桌面截图', 'utf-8').encode()
        message.attach(MIMEText(msg, mode, 'utf-8'))
        if image_path != '':
            with open(image_path, 'rb') as f:
                mime = MIMEBase('image', 'png', filename='screen.png')
                mime.add_header('Content-Disposition', 'attachment', filename='screen.png')
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                message.attach(mime)
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"

