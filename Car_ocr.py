import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
import imutils
from Roi_calc import *
def Car_ocr(pic):
    img = cv2.imread(pic)
    Result_1=roi_1(img)
    #return Result_1
    print(Result_1)

    Result_2=roi_2(img)
    #return Result_2
    print(Result_2)

    Result_3=roi_3(img)
    #return Result_3
    print(Result_3)

    Result_4=roi_4(img)
    #return Result_4
    print(Result_4)
