# coding=utf-8
import poplib
import re
import time
import mail_sender
from PIL import ImageGrab


screen_path = 'screen.jpg'
# 邮箱地址
your_email_adr = 'xxxxxxx'
# 口令
your_password = 'xxxxxxx'

def shoot_screen():
    screen = ImageGrab.grab()
    screen.save(screen_path)


def get_mail_count_and_content():
    email = '1048058400@qq.com'
    # 口令
    password = "tuhnimgbsntgbecg"
    # pop服务器
    pop_server = 'pop.qq.com'
    # 连接到pop服务器
    server = poplib.POP3_SSL(pop_server, port=995)
    server.user(email)
    server.pass_(password)
    mail_count = server.stat()[0]
    content = server.retr(mail_count)[1][0:10]
    mail_content = '\r\n'.join(content)
    return (mail_count, mail_content)


pattern = re.compile('.*?Subject:(.*?)Mime-Version.*?', re.S)
print 'running....'
old_count = get_mail_count_and_content()[0]
while True:
    time.sleep(5)
    current_count, msg_content = get_mail_count_and_content()
    if current_count != old_count:
        index = current_count
        match_list = pattern.findall(msg_content)
        instruction = match_list[0].strip() if match_list else ''
        if instruction == 'shotscreen':
            shoot_screen()
            mail_sender.send(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'plain', image_path=screen_path)
        elif instruction == '':
            pass
        else:
            print u'未识别的指令'
        old_count = current_count




