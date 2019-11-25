import numpy as np
import cv2
import itertools
import math

global outputFact

#Variabel keluaran dari program ini. Berisi Array of fakta
outputFact = []

#Dapatkan image
path = "./img/shapes2.jpg"
img = cv2.imread(path)

#Ubah image color menjadi abu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Singkirikan Gaussian Noise
blur = cv2.GaussianBlur(gray, (3,3), 0)

#Dapatkan sisi dari edges
edges = cv2.Canny(gray, 50, 150)
#edges2 = cv2.Canny(blur, 50, 150, apertureSize = 3)

#Aplikasikan inverse binary untuk mendapatkan hasil yang lebih baik
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
#thresh2 = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)

#Ambil kontur image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#Fungsi untuk mendapatkan sudut
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

#Fungsi untuk mendapatkan distance
def getDistance(a, b):  
    #  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    dist = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2) 
    return dist  

def getFaktaSisi(a):
    return "sisi = " + str(a)

def getFaktaSudut(a):
    if (a < 88) :
        return "sudutTerbesar < 88"
    elif (a > 92) :
        return "sudutTerbesar < 92"
    else :
        return "sudutTerbesar >= 88 sudutTerbesar =< 92"

def getsisiSamaPanjang(myList):
    counter = 0
    combList = []
    for L in range(0, len(myList)+1):
        for subset in itertools.combinations(myList, L):
            if(len(subset) == 2) :
                if (abs(subset[0] - subset[1]) <=2) :
                    counter = counter + 1
    
    if (counter == 2) :
        return "pasangSisiSamaPanjang = 2"
    elif (counter < 2) :
        return "pasangSisiSamaPanjang < 2"
    else:
        return "/"

def getSudutLancip(a):
    if ((a > 58) and (a < 62)):
        return "sudutTerbesar > 58 sudutTerbesar < 62"
    else:
        return "/"

def isSegilimaSamaSisi(a, myList):
    if (a == 5) :
        counter = 0
        combList = []
        for L in range(0, len(myList)+1):
            for subset in itertools.combinations(myList, L):
                if(len(subset) == 2) :
                    if (abs(subset[0] - subset[1]) <=2) :
                        counter = counter + 1
        
        if (counter == 5) :
            return "sisiSamaPanjang = 5"
        else :
            return "/"
    else :
        return "/"

def isSegienamSamaSisi(a, myList):
    if (a == 6):
        counter = 0
        combList = []
        for L in range(0, len(myList)+1):
            for subset in itertools.combinations(myList, L):
                if(len(subset) == 2) :
                    if (abs(subset[0] - subset[1]) <=2) :
                        counter = counter + 1
        
        if (counter == 6) :
            return "sisiSamaPanjang = 6"
        else :
            return "/"
    else :
        return "/"


for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(gray, [approx], 0, (0, 0, 0), 5)
    
    #Untuk mendapatkan posisi dari shape, berguna untuk penamaan
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    #Sebuah array yang terdiri dari sisi, [sudut], dan [panjang sisi]
    shape = []

    #Array sudut
    sudut = []

    #Array panjang sisi
    panjang = []

    #Array fakta 1 shape
    fakta = []

    if len(approx) == 3 :
        cv2.putText(gray, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.50, (0, 0, 0), 1)
        for i in range (3) :
            sudut.append(getAngle(approx[i % 3][0], approx[(i+1) % 3][0], approx[(i+2) % 3][0]))
            panjang.append(getDistance(approx[i][0], approx[(i+1)%3][0]))
          
    elif len(approx) == 4 :
        cv2.putText(gray, "Segiempat", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1) 
        for i in range (4) :
            sudut.append(getAngle(approx[i % 4][0], approx[(i+1) % 4][0], approx[(i+2) % 4][0]))
            panjang.append(getDistance(approx[i][0], approx[(i+1)%4][0]))

    elif len(approx) == 5 :
        cv2.putText(gray, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
        for i in range (5) :
            sudut.append(getAngle(approx[i % 5][0], approx[(i+1) % 5][0], approx[(i+2) % 5][0]))
            panjang.append(getDistance(approx[i][0], approx[(i+1) %5][0]))

    elif len(approx) == 6 :
        cv2.putText(gray, "Heksagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
        for i in range (6) :
            sudut.append(getAngle(approx[i % 6][0], approx[(i+1) % 6][0], approx[(i+2) % 6][0]))
            panjang.append(getDistance(approx[i][0], approx[(i+1) %6][0]))
    
    sudut.sort(reverse=True)
    panjang.sort(reverse=True)

    shape.append(len(approx))
    shape.append(sudut)
    shape.append(panjang)
    print(sudut)
    print(sudut[0])

    fakta.append(getFaktaSisi(len(approx)))
    fakta.append(getFaktaSudut(sudut[0]))
    fakta.append(getsisiSamaPanjang(panjang))
    fakta.append(getSudutLancip(sudut[0]))
    fakta.append(isSegilimaSamaSisi(len(approx), panjang))
    fakta.append(isSegienamSamaSisi(len(approx), panjang))
    
    outputFact.append(fakta)

print(outputFact)


#Show image
cv2.imshow("Image", gray)
cv2.imshow("Edges", edges)


#Memastikan windows tidak langsung tertutup
cv2.waitKey(0)
cv2.destroyAllWindows()


