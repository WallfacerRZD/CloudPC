#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders


# 第三方 SMTP 服务
class Sender(object):
    def __init__(self, user, password):
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = user  # 用户名
        self.mail_pass = password  # 口令
        self.sender = user  # 发送人
        self.receivers = [user]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def send_text(self, header, msg, mode):
        message = MIMEText(msg, mode, "utf-8")
        message['From'] = Header("CloudPC", 'utf-8')
        message['To'] = Header("YOU", 'utf-8')
        message['Subject'] = Header(header, 'utf-8')
        smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"


if __name__ == "__main__":
    test = Sender()
    test.send_text("CloudPC", "test", "plain")
