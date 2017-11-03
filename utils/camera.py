from VideoCapture import Device
import time
import cv2
from PIL import ImageGrab
from io import BytesIO


class Camera(object):


        # def shot(self):
        #     self.camera.setResolution(300, 200)
        # self.camera.getImage(timestamp=0).resize((self.width, self.height)).save("../web/static/test.jpg", quality=80)
    @staticmethod
    def frame():
        camera = cv2.VideoCapture(0)
        try:
            if not camera.isOpened():
                raise RuntimeError("Can't open camera")
            while camera.isOpened():
                ok, frame = camera.read()
                yield cv2.imencode(".png", frame)[1].tobytes()
        except Exception, e:
            print str(e)
            camera.release()

    @staticmethod
    def shot_screen():
        screen = ImageGrab.grab()
        img_io = BytesIO()
        screen.save(img_io, 'png')
        img_io.seek(0)
        return img_io

    @staticmethod
    def shot_camera():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Can't open camera")
        ok, frame = camera.read()
        frame = cv2.resize(frame, (400, 300), interpolation=cv2.INTER_CUBIC)
        return cv2.imencode('.png', frame)[1].tobytes()


if __name__ == "__main__":
    camera = Camera()
    camera.frame()
