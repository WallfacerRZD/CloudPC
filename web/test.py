from PIL import ImageGrab

picture = ImageGrab.grab()
picture.tobytes()
print type(picture)
