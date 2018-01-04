# coding=utf-8
import time
time1 = time.time()
import cv2
image=cv2.imread("sz000020.png")
res = cv2.resize(image,(550,300), interpolation=cv2.INTER_AREA)
# cv2.imshow('image', image)
# cv2.imshow('resize', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite("2.png",res)
time2=time.time()
print u'总共耗时：' + str(time2 - time1) + 's'