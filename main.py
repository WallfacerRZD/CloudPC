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


def login():
    addr = '1048058400@qq.com'
    # 口令
    password = "tuhnimgbsntgbecg"
    # pop服务器
    pop_server = 'pop.qq.com'
    # 连接到pop服务器
    server = poplib.POP3_SSL(pop_server, port=995)
    server.user(addr)
    server.pass_(password)
    return server


def get_mail_count():
    server = login()
    cnt = server.stat()[0]
    server.quit()
    return cnt


def get_mail_content(index):
    server = login()
    try:
        content = ''.join(server.retr(index)[1][:10])
    except Exception, e:
        print e
        "发送邮件提示用户"
        content = ""
    finally:
        server.quit()
    return content


pattern = re.compile('.*?Subject:(.*?)Mime-Version.*?', re.S)

print 'running....'
old_cnt = get_mail_count()
while True:
    time.sleep(1)
    cnt = get_mail_count()
    print cnt
    if cnt != old_cnt:
        content = get_mail_content(cnt)
        match_list = pattern.findall(content)
        instruction = match_list[0].strip() if match_list else ''
        print instruction
        if instruction == 'shotscreen':
            shoot_screen()
            mail_sender.send(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'plain',
                             image_path=screen_path)
        elif instruction == '':
            pass
        else:
            print u'未识别的指令'
        old_cnt = cnt
