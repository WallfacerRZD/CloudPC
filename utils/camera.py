# coding=utf-8
from cv2 import VideoCapture, imencode, resize, INTER_CUBIC
from PIL import ImageGrab, Image
from io import BytesIO
from selenium import webdriver
from StringIO import StringIO
from time import sleep


class Camera(object):
    @staticmethod
    def frame():
        camera = VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Can't open camera")

        while camera.isOpened():
            ok, frame = camera.read()
            yield imencode(".jpg", frame)[1].tobytes()

    @staticmethod
    def shot_screen():
        screen = ImageGrab.grab()
        img_io = BytesIO()
        screen.save(img_io, 'jpeg')
        img_io.seek(0)
        return img_io

    @staticmethod
    def shot_camera():
        try:
            camera = VideoCapture(0)
            if not camera.isOpened():
                raise RuntimeError("Can't open camera")
            ok, frame = camera.read()
            frame = resize(frame, (1200, 900), interpolation=INTER_CUBIC)
            img_stream = imencode('.jpg', frame)[1].tobytes()
            return img_stream
        except Exception, e:
            print e
            return u'nothing'

    @staticmethod
    def get_position():
        driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
        driver.get('http://127.0.0.1:2333/position')
        sleep(1)
        screen = driver.get_screenshot_as_png()
        string_io = StringIO(screen)
        image = Image.open(string_io)
        image_io = BytesIO()
        try:
            image.save(image_io, 'png')
            image_io.seek(0)
            return image_io
        except Exception, e:
            return "Get Position Failed!!"
        finally:
            driver.quit()


if __name__ == "__main__":
    print 'test'
