# coding=utf-8
import os
from chardet import detect
import subprocess
from ctypes import *


class Manager(object):
    def __init__(self):
        self.user32 = windll.LoadLibrary('user32.dll')

    def lock(self):
        self.user32.LockWorkStation()

    @staticmethod
    def shutdown_after(s):
        os.system("shutdown -s -t %d" % s)

    @staticmethod
    def shutdown_cancel():
        os.system("shutdown -a")

    @staticmethod
    def execute(cmd):
        try:
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, error = p.communicate()
            if p.returncode:
                if error:
                    encoding = detect(error)['encoding']
                    content = (u'您执行的命令是:   %s\n' % cmd).encode('utf-8') + error.decode(encoding).encode('utf-8')
                    return content
            else:
                if out:
                    encoding = detect(out)['encoding']
                    content = (u'您执行的命令是:   %s\n' % cmd).encode('utf-8') + out.decode(encoding).encode('utf-8')
                    return content
                else:
                    return (u'您执行的命令是:   %s\n' % cmd).encode('utf-8') + u'执行成功,无输出信息'
        except Exception, e:
            print e
            return u'出错啦!!'


if __name__ == "__main__":
    manager = Manager()
    manager.execute('fir')
