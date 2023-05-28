
import cv2
image=cv2.imread("img1.png")
grey_filter=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur =cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch=cv2.divide(grey_filter,invertedblur,scale=256.0)
cv2.imwrite("out4.png",sketch)