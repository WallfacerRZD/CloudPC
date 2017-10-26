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


if __name__ == "__main__":
    # cam = Camera()
    # while True:
    #     cam.shot()
    #     time.sleep(2)
    #     print 'test'
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        print type(frame)
        cv2.waitKey(10)
        cv2.imshow('test', frame)
    cap.release()
    cv2.destroyAllWindows()

