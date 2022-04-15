


#TEKRARLANNA AYNALALNAN UZATILAN RESİM

import cv2
import numpy as np
resim=cv2.imread("cicek.jpg")

aynalanan=cv2.copyMakeBorder(resim,30,30,70,70,cv2.BORDER_REFLECT)
uzatılan=cv2.copyMakeBorder(resim,80,80,80,80,cv2.BORDER_REPLICATE)
tekrarlanan=cv2.copyMakeBorder(resim, 60,60,60,60,cv2.BORDER_WRAP)
sarılan=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT)



cv2.imshow("ayna", aynalanan)
cv2.imshow("uza",uzatılan)
cv2.imshow("tekrar",tekrarlanan)
cv2.imshow("sarılan",sarılan)


cv2.waitKey(0)
cv2.destroyAllWindows()


