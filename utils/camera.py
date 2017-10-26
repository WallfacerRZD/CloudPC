from VideoCapture import Device
import time
import cv2


class Camera(object):
    def __init__(self):
        self.camera = Device()
        self.width = 1920
        self.height = 1080

    def shot(self):
        self.camera.setResolution(300, 200)
        # self.camera.getImage(timestamp=0).resize((self.width, self.height)).save("../web/static/test.jpg", quality=80)

    @staticmethod
    def frame():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Can't open camera")
        while camera.isOpened():
            ok, frame = camera.read()
            yield cv2.imencode(".jpg", frame)[1].tobytes()


if __name__ == "__main__":
    camera = Camera()
    camera.frame()
