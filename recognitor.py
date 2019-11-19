import numpy as np
import cv2

#Get image
img = cv2.imread("G:\ADNI\AKADEMIK\SEMESTER 5\IF3170 - Integelensi Buatan\TUGAS\TUBES 2\img\shapes.jpg")

#Change image color to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Removing Gaussian Noise
blur = cv2.GaussianBlur(gray, (3,3), 0)

#Get the edges of the shape
edges = cv2.Canny(gray, 50, 150)
#edges2 = cv2.Canny(blur, 50, 150, apertureSize = 3)


#Applying inverse binary due to white background and adapting thresholding for better results
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
#thresh2 = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)

#Get the contours of the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(gray, [approx], 0, (0, 0, 0), 5)
    #Untuk mendapatkan posisi dari shape, berguna untuk penamaan
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3 :
        cv2.putText(gray, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.50, (0, 0, 0), 1)
    elif len(approx) == 4 :
        x1, y1, w, h = cv2.boundingRect(approx)
        ratio = float (w)/h
        if (ratio >= 0.95 and ratio <= 1.05) :
            cv2.putText(gray, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
        else :
            cv2.putText(gray, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
    elif len(approx) == 5 :
        cv2.putText(gray, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
    elif len(approx) == 6 :
        cv2.putText(gray, "Heksagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
    elif len(approx) == 10 :
        cv2.putText(gray, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
    elif len(approx) == 15 :
        cv2.putText(gray, "Elipse", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
    else :
        cv2.putText(gray, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)

#Show image
cv2.imshow("Image", gray)
#cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)
#cv2.imshow("Edges2", edges2)
#cv2.imshow("Binary",thresh)
#cv2.imshow("Binary2",thresh)

#Make sure the image does'nt closed immediately
cv2.waitKey(0)
cv2.destroyAllWindows()


