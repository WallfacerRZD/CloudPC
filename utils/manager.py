import os
from ctypes import *
from PIL import ImageGrab


class Manager(object):
    def __init__(self):
        self.user32 = windll.LoadLibrary('user32.dll')
        self.path = "../pictures/screen.jpg"

    def lock(self):
        self.user32.LockWorkStation()

    def shot_screen(self):
        screen = ImageGrab.grab()
        screen.save(self.path)

    @staticmethod
    def shutdown_after(h=0, m=0, s=0):
        os.system("shutdown -s -t %d" % 2000)

    @staticmethod
    def shutdown_cancel():
        os.system("shutdown -a")


if __name__ == "__main__":
    manager = Manager()
    manager.shot_screen()
