import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
import imutils
from pytesseract import image_to_string

def roi_1(img):
    #cv2.imshow('orignal', img)
    # cv2.imshow("new",img)
    img = img[290:365, 220:380]
    #image = imutils.resize(img, width=900, height=900)
    # orignal
    #cv2.imshow("crop_1", img)

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # edged = cv2.Canny(gray, 170, 200)

    # canny
    # cv2.imshow("4 - Canny Edges", edged)
    # ret2,threshold_img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow('pppp',threshold_img)

    # thresh
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    #ret, threshH = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("tt",threshH)

    contours, h = cv2.findContours(thresh, 1, 1)

    # once I have the contours list, i need to find the contours which form rectangles.
    # the contours can be approximated to minimum polygons, polygons of size 4 are probably rectangles
    largest_rectangle = [0, 0]
    # approximate the contour
    for cnt in contours:
        elipson = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.08 * elipson, True)
        if len(approx) == 4:  # polygons with 4 points is what I need.
            area = cv2.contourArea(cnt)
            if area > largest_rectangle[0]:
                # find the polygon which has the largest size.
                largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

    x, y, w, h = cv2.boundingRect(largest_rectangle[1])
    # crop the rectangle to get the number plate.
    roi = img[y:y + h, x:x + w]
    #cv2.imshow("roi_1", roi)
    cv2.waitKey(0)
    a = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('a', a)
    #sobelx = cv2.Sobel(a, cv2.CV_8U, 1, 0, ksize=3)
    #cv2.imshow("Sob", sobelx)
    #ret, th = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('th', th)

    # cv2.drawContours(img,[largest_rectangle[1]],0,(0,0,255),-1)
    # plt.imshow(roi, cmap = 'gray')
    plt.show()
    #cv2.waitKey(0)

    text = pytesseract.image_to_string(roi)
    char = str.maketrans("“,!@.$~`^&*()-_+}{\|:?/><|", 26 * " ")
    plate = text.translate(char)

    def removeSpaces(str):
        new_str = ""
        for i in range(len(str)):
            if (str[i] != " "):
                new_str += str[i]
        return new_str

    platess = removeSpaces(plate)
    return platess

    return text

#roi_2

def roi_2(img):
    #cv2.imshow('orignal', img)
    # cv2.imshow("new",img)
    img = img[262:363, 200:410]
    #img = img[430:591, 60:458]
    #image = imutils.resize(img, width=900, height=900)
    # orignal
    #cv2.imshow("crop_2", img)

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # edged = cv2.Canny(gray, 170, 200)

    # canny
    # cv2.imshow("4 - Canny Edges", edged)
    # ret2,threshold_img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow('pppp',threshold_img)

    # thresh
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    ret, threshH = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("tt",threshH)

    contours, h = cv2.findContours(thresh, 1, 1)

    # once I have the contours list, i need to find the contours which form rectangles.
    # the contours can be approximated to minimum polygons, polygons of size 4 are probably rectangles
    largest_rectangle = [0, 0]
    for cnt in contours:
        elipson = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.08 * elipson, True)
        if len(approx) == 4:  # polygons with 4 points is what I need.
            area = cv2.contourArea(cnt)
            if area > largest_rectangle[0]:
                # find the polygon which has the largest size.
                largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

    x, y, w, h = cv2.boundingRect(largest_rectangle[1])
    # crop the rectangle to get the number plate.
    roi = img[y:y + h, x:x + w]
    #cv2.imshow("roi_2", roi)
    cv2.waitKey(0)
    a = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('a', a)
    #sobelx = cv2.Sobel(a, cv2.CV_8U, 1, 0, ksize=3)
    #cv2.imshow("Sob", sobelx)
    #ret, th = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('th', th)

    # cv2.drawContours(img,[largest_rectangle[1]],0,(0,0,255),-1)
    # plt.imshow(roi, cmap = 'gray')
    #plt.show()
    #cv2.waitKey(0)

    text = pytesseract.image_to_string(roi)
    char = str.maketrans("“,!@.$~`^&*()-_+}{\|:?/><|", 26 * " ")
    plate = text.translate(char)

    def removeSpaces(str):
        new_str = ""
        for i in range(len(str)):
            if (str[i] != " "):
                new_str += str[i]
        return new_str

    platess = removeSpaces(plate)
    return platess

    return text

#roi_3

def roi_3(img):
    #cv2.imshow('orignal', img)
    # cv2.imshow("new",img)
    img = img[260:350,100:436]
    #image = imutils.resize(img, width=900, height=900)
    # orignal
    #cv2.imshow("crop_3", img)

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # edged = cv2.Canny(gray, 170, 200)

    # canny
    # cv2.imshow("4 - Canny Edges", edged)
    # ret2,threshold_img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow('pppp',threshold_img)

    # thresh
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    ret, threshH = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("tt",threshH)

    contours, h = cv2.findContours(thresh, 1, 1)

    # once I have the contours list, i need to find the contours which form rectangles.
    # the contours can be approximated to minimum polygons, polygons of size 4 are probably rectangles
    largest_rectangle = [0, 0]
    for cnt in contours:
        elipson = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.08 * elipson, True)
        if len(approx) == 4:  # polygons with 4 points is what I need.
            area = cv2.contourArea(cnt)
            if area > largest_rectangle[0]:
                # find the polygon which has the largest size.
                largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

    x, y, w, h = cv2.boundingRect(largest_rectangle[1])
    # crop the rectangle to get the number plate.
    roi = img[y:y + h, x:x + w]
    #cv2.imshow("roi_3", roi)
    cv2.waitKey(0)
    a = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('a', a)
   # sobelx = cv2.Sobel(a, cv2.CV_8U, 1, 0, ksize=3)
    #cv2.imshow("Sob", sobelx)
    #ret, th = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('th', th)

    # cv2.drawContours(img,[largest_rectangle[1]],0,(0,0,255),-1)
    # plt.imshow(roi, cmap = 'gray')
    #plt.show()
    #cv2.waitKey(0)

    text = pytesseract.image_to_string(roi)
    char = str.maketrans("“,!@.$~`^&*()-_+}{\|:?/><|", 26 * " ")
    plate = text.translate(char)

    def removeSpaces(str):
        new_str = ""
        for i in range(len(str)):
            if (str[i] != " "):
                new_str += str[i]
        return new_str

    platess = removeSpaces(plate)
    return platess

    return text
#roi_4

def roi_4(img):
    cv2.imshow('orignal', img)
    # cv2.imshow("new",img)
    img = img[233:400, 131:600]
    #image = imutils.resize(img, width=900, height=900)
    # orignal
    #cv2.imshow("crop_4", img)

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # edged = cv2.Canny(gray, 170, 200)

    # canny
    # cv2.imshow("4 - Canny Edges", edged)
    # ret2,threshold_img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow('pppp',threshold_img)

    # thresh
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    ret, threshH = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("tt",threshH)

    contours, h = cv2.findContours(thresh, 1, 1)

    # once I have the contours list, i need to find the contours which form rectangles.
    # the contours can be approximated to minimum polygons, polygons of size 4 are probably rectangles
    largest_rectangle = [0, 0]
    for cnt in contours:
        elipson = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.08 * elipson, True)
        if len(approx) == 4:  # polygons with 4 points is what I need.
            area = cv2.contourArea(cnt)
            if area > largest_rectangle[0]:
                # find the polygon which has the largest size.
                largest_rectangle = [cv2.contourArea(cnt), cnt, approx]

    x, y, w, h = cv2.boundingRect(largest_rectangle[1])
    # crop the rectangle to get the number plate.
    roi = img[y:y + h, x:x + w]
    #cv2.imshow("roi_4", roi)
    cv2.waitKey(0)
    a = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('a', a)
    #sobelx = cv2.Sobel(a, cv2.CV_8U, 1, 0, ksize=3)
    #cv2.imshow("Sob", sobelx)
    #ret, th = cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('th', th)

    # cv2.drawContours(img,[largest_rectangle[1]],0,(0,0,255),-1)
    # plt.imshow(roi, cmap = 'gray')
    #plt.show()
    #cv2.waitKey(0)

    text = pytesseract.image_to_string(roi)
    char = str.maketrans("“,!@.$~`^&*()-_+}{\|:?/><|", 26 * " ")
    plate = text.translate(char)

    def removeSpaces(str):
        new_str = ""
        for i in range(len(str)):
            if (str[i] != " "):
                new_str += str[i]
        return new_str

    platess = removeSpaces(plate)
    return platess
    con = sqlite3.connect('Form.db')
    cursor = con.cursor()

    cursor.execute("SELECT Plate FROM EMPLOYEE WHERE Plate = ?", [platess])
    for row in cursor.fetchall():
        print(row)
        if plate in row:
            print('Plate Found')
            con.commit()
            con.close()



    else:
        print("Plate Not Found")
        con.commit()
        con.close()

