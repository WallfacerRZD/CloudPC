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
    def __init__(self):
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "1048058400@qq.com"  # 用户名
        self.mail_pass = "tuhnimgbsntgbecg"  # 口令
        self.sender = '1048058400@qq.com'  # 发送人
        self.receivers = ['1048058400@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def send_image(self, header, msg, mode, image_path=''):
        message = MIMEMultipart('alternative')
        message['From'] = Header("Mylaptop", 'utf-8')
        message['To'] = Header("Mr.Dong", 'utf-8')
        message['Subject'] = Header(header, 'utf-8').encode()
        message.attach(MIMEText(msg, mode, 'utf-8'))
        if image_path != '':
            with open(image_path, 'rb') as f:
                # 加密附件
                mime = MIMEBase('image', 'png', filename='screen.png')
                mime.add_header('Content-Disposition', 'attachment', filename='screen.png')
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                message.attach(mime)
        smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"

    def send_text(self, header, msg, mode):
        message = MIMEText(msg, mode, "utf-8")
        message['From'] = Header("Mylaptop", 'utf-8')
        message['To'] = Header("Mr.Dong", 'utf-8')
        message['Subject'] = Header(header, 'utf-8')
        smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        smtpObj.quit()
        print "邮件发送成功"

if __name__ == "__main__":
    test = Sender()
    test.send_text("内容", "plain")
