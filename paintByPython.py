
import cv2
import numpy as np


cizim= False

mod= False

xi, yi = -1,-1       # x y koordinatların başlangıcı

def draw(event , x, y, flags, param):    # fonksiyon 5 parametre alıyor ve ben doldurmak için flag ve param yükledim event değişken ve x y koordinat

    global  cizim ,xi, yi, mo 



    if event == cv2.EVENT_LBUTTONDOWN:   # eğer ben fareyi tıklama işlemi yaparsam çizim true oluyor başlangıç noktaları koordinatlarla birleşiyor
       xi,yi=x,y
       cizim= True


    elif event== cv2.EVENT_MOUSEMOVE:   # ve ben fareyi hareket ettirirsem m tuşuna basınca daire aksi halde kare çizicek ölçüler verilen gibi
        if cizim==True:
            if mod:
                cv2.circle(resim, (x, y), 5, (130, 66, 99), -1)

            else:
                cv2.rectangle(resim,(xi,yi), (x, y),  (100, 106, 99), -1)

        else:
            pass

    elif event==cv2.EVENT_MBUTTONUP:   #fareyi kaldrıdığımda çizim bitiyor
        cizim=False


resim=np.ones((512,512,3), np.uint8) # çizim yapacağımız resim


cv2.namedWindow("paint")
cv2.setMouseCallback("paint",draw)


while(1):
    cv2.imshow("paint",resim)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if cv2.waitKey(1) & 0xFF== ord("m"):
        mod= not mod


cv2.destroyAllWindows()
