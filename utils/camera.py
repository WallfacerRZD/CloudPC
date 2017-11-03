from VideoCapture import Device
import time
import cv2


class Camera(object):
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.camera = cv2.VideoCapture(0)

    def release_cam(self):
        self.camera.release()


        # def shot(self):
        #     self.camera.setResolution(300, 200)
        # self.camera.getImage(timestamp=0).resize((self.width, self.height)).save("../web/static/test.jpg", quality=80)

    def frame(self):
        if not self.camera.isOpened():
            raise RuntimeError("Can't open camera")
        while self.camera.isOpened():
            ok, frame = self.camera.read()
            yield cv2.imencode(".jpg", frame)[1].tobytes()


if __name__ == "__main__":
    camera = Camera()
    camera.frame()
