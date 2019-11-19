import cv2
import numpy as np

img = cv2.imread('G:\ADNI\AKADEMIK\SEMESTER 5\IF3170 - Integelensi Buatan\TUGAS\TUBES 2\img\persegi_1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

for line in lines:
    pix, rad = line[0]
    a = np.cos(rad)
    b = np.sin(rad)
    x0 = a * pix
    y0 = b * pix
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('edges', edges)
cv2.imshow('image', img)
cv2.waitKey(0)
