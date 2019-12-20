import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('Sejong.mp4')
success,image = vidcap.read()
print(success)
count = 0
#success = True
while success:
  cv2.imwrite(("frame%05d.jpg" % count), image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  if(cnt): break
