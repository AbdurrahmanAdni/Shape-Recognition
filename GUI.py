from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import itertools 
import numpy as np
import cv2
import itertools
import math

global rules
global facts 
global hitRules
global allRules
global outputFact
global sourcePath

sourcePath = ""


##### IMPLEMENTASI IMAGE PREPROCESSING #########

#Variabel keluaran dari program ini. Berisi Array of fakta
outputFact = []

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

def getJumlahSudut(a):
    return "sudut = " + str(a)

def getFaktaSudut(a):
    if (a < 88) :
        return "sudutTerbesar < 88"
    elif (a > 92) :
        return "sudutTerbesar > 92"
    else :
        return "sudutTerbesar >= 88 sudutTerbesar <= 92"

def getsisiSamaPanjang(myList):
    counter = 0
    # combList = []
    for L in range(0, len(myList)+1):
        for subset in itertools.combinations(myList, L):
            if(len(subset) == 2) :
                if (abs(subset[0] - subset[1]) <=2.5) :
                    counter = counter + 1
    
    if (counter >= 2) :
        return "pasangSisiSamaPanjang = 2"
    elif (counter < 2) :
        return "pasangSisiSamaPanjang < 2"
    else:
        return "/"

def getSudutLancip(a):
    if ((a > 58) and (a < 62)):
        return "sudutTerbesar >= 58 sudutTerbesar <= 62"
    else:
        return "/"

def getIsLayang(a,b,c,d):
    diagonal1 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    diagonal2 = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)

    if (abs(diagonal1 - diagonal2) <= 2):
        return "pasangSisi = sama"
    else :
        return "pasangSisi != sama"

def isTrapesiumRata(myList):
    counter = 0
    for i in range(0, len(myList)):
        if ((myList[i] <= 92) and (myList[i] >= 88)) :
            counter = counter + 1
    if counter == 2 :
        return "sudut90 = 2"
    else :
        return "/"

def checkPosisiSikuSiku(myList):
    # if ((myList[0] <= 92) and (myList[0] >= 88)) :
    #     if ((myList[1] <= 92) and (myList[1] >= 88)) :
    #         return "posisi90 = kiri"
    #     else :
    #         return "/"
    # elif ((myList[2] <= 92) and (myList[2] >= 88)) :
    #         if ((myList[3] <= 92) and (myList[3] >= 88)) :
    #             return "posisi90 = kanan"
    #         else :
    #             return "/"

    if ((myList[0] <= 92) and (myList[0] >= 88)) and ((myList[3] <= 92) and (myList[3] >= 88)) :
        return "posisi90 = kiri"
    elif ((myList[1] <= 92) and (myList[1] >= 88)) and ((myList[2] <= 92) and (myList[2] >= 88)) :
        return "posisi90 = kanan"
    elif ((myList[2] <= 92) and (myList[2] >= 88)) and ((myList[3] <= 92) and (myList[3] >= 88)) :
        return "posisi90 = kanan"
    else :
        return "/"

def isSegilimaSamaSisi(a, myList):
    if (a == 5) :
        counter = 0
        # combList = []
        for L in range(0, len(myList)+1):
            for subset in itertools.combinations(myList, L):
                if(len(subset) == 2) :
                    if (abs(subset[0] - subset[1]) <=11) :
                        counter = counter + 1
        if (counter == 10) :
            return "sisiSamaPanjang = 5"
        else :
            return "/"
    else :
        return "/"

def isSegienamSamaSisi(a, myList):
    if (a == 6):
        counter = 0
        # combList = []
        for L in range(0, len(myList)+1):
            for subset in itertools.combinations(myList, L):
                if(len(subset) == 2) :
                    if (abs(subset[0] - subset[1]) <=6) :
                        counter = counter + 1
        
        if (counter == 15) :
            return "sisiSamaPanjang = 6"
        else :
            return "/"
    else :
        return "/"

def returnAllFact():
    global outputFact
    global sourcePath

    #Dapatkan image
    path = sourcePath
    img = cv2.imread(path)

    #Ubah image color menjadi abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Singkirikan Gaussian Noise
    blur = cv2.GaussianBlur(gray, (3,3), 0)

    #Aplikasikan inverse binary untuk mendapatkan hasil yang lebih baik
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
    #thresh2 = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)

    #Ambil kontur image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

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

                fakta.append(getIsLayang(approx[0][0], approx[1][0], approx[2][0], approx[3][0]))
            
            if (isTrapesiumRata(sudut)) != "/" :
                fakta.append(isTrapesiumRata(sudut))
                fakta.append(checkPosisiSikuSiku(sudut))

        elif len(approx) == 5 :
            cv2.putText(gray, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
            for i in range (5) :
                sudut.append(getAngle(approx[i % 5][0], approx[(i+1) % 5][0], approx[(i+2) % 5][0]))
                panjang.append(getDistance(approx[i][0], approx[(i+1) %5][0]))
    
            if(isSegilimaSamaSisi(len(approx), panjang) != "/"):
                fakta.append(isSegilimaSamaSisi(len(approx), panjang))
    

        elif len(approx) == 6 :
            cv2.putText(gray, "Heksagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.40, (0, 0, 0), 1)
            for i in range (6) :
                sudut.append(getAngle(approx[i % 6][0], approx[(i+1) % 6][0], approx[(i+2) % 6][0]))
                panjang.append(getDistance(approx[i][0], approx[(i+1) %6][0]))
                
            if(isSegienamSamaSisi(len(approx), panjang) != "/"):
                fakta.append(isSegienamSamaSisi(len(approx), panjang))
            
        
        print(sudut)
        print(panjang)
        sudut.sort(reverse=True)
        panjang.sort(reverse=True)
        #print(sudut)
        #print(panjang)

        shape.append(len(approx))
        shape.append(sudut)
        shape.append(panjang)

        #print(sudut[0])

        fakta.append(getFaktaSisi(len(approx)))
        fakta.append(getJumlahSudut(len(approx)))
        
        if (len(approx) < 5) :
            fakta.append(getFaktaSudut(sudut[0]))

            if(getsisiSamaPanjang(panjang) != "/"):
                fakta.append(getsisiSamaPanjang(panjang))
            
            if(getSudutLancip(sudut[0]) != "/"):
                fakta.append(getSudutLancip(sudut[0]))
        #else :

            # if(isSegilimaSamaSisi(len(approx), panjang) != "/"):
            #     fakta.append(isSegilimaSamaSisi(len(approx), panjang))
            
            # if(isSegienamSamaSisi(len(approx), panjang) != "/"):
            #     fakta.append(isSegienamSamaSisi(len(approx), panjang))
            
        
        outputFact.append(fakta)


##### IMPLEMENTASI KBS #####

# knowledge based
rules = {
    "sisi = 3 sudut = 3 " : "segitiga",
    "sisi = 4 sudut = 4 " : "segiempat",
    "sisi = 5 sudut = 5 " : "segilima",
    "sisi = 6 sudut = 6 " : "segienam",

    "sudutTerbesar < 88 segitiga " : "segitigaLancip",
    "sudutTerbesar > 92 segitiga " : "segitigaTumpul",
    "sudutTerbesar >= 88 sudutTerbesar <= 92  segitiga " : "segitigaSiku",

    "sisiSamaPanjang = 2 segitiga " : "segitigaSamaKaki",
    "segitigaLancip segitigaSamaKaki " : "segitigaSamaKakiLancip",
    "segitigaTumpul segitigaSamaKaki " : "segitigaSamaKakiTumpul",
    "segitigaSiku segitigaSamaKaki " : "segitigaSamaKakiSiku",
    "sudutTerbesar >= 58 sudutTerbesar <= 62 segitigaSamaKakiLancip " : "segitigaSamaSisi",

    "pasangSisiSamaPanjang = 2 segiempat " : "jajaranGenjang",
    "pasangSisiSamaPanjang < 2 segiempat " : "trapesium",

    "pasangSisi = sama jajaranGenjang " : "segiempatBeraturan",
    "pasangSisi != sama jajaranGenjang " : "layangLayang",
    "sudut90 = 2 trapesium " : "trapesiumRata",
    "pasangSisiSamaPanjang < 2 trapesium " : "trapesiumSamaKaki",
    "sudut90 = 2 trapesiumSamaKaki " : "trapesiumRata",

    "posisi90 = kiri trapesiumRata " : "trapesiumRataKiri",
    "posisi90 = kanan trapesiumRata " : "trapesiumRataKanan",

    "sisiSamaPanjang = 5 segilima " : "segilimaSamaSisi",

    "sisiSamaPanjang = 6 segienam " : "segienamSamaSisi",
}

# facts list
facts = []

# hit rules list untuk queue rules
hitRules = []

# Untuk menyimpan rules yang telah diproses berdasarkan fakta (akan terurut berdasarkan type engine yang akan diproses)
allRules = []


# fungsi untuk mengembalikan list of facts yang sesuai rules
def generatePatternFacts(myList):
    # inisialisasi
    patternFacts = []

    for L in range(0, len(myList)+1):
        for subset in itertools.combinations(myList, L):
            if(len(subset) > 1):
                string = ""
                for i in subset:
                    string = string + i + " " 
                patternFacts.append(string)

    return patternFacts 

# fungsi untuk mendapatkan hit rules
def getHitRules(ruleList, factList):
    global allRules
    global hitRules

    tempRules = []

    # mendapatkan semua LHS dari rules 
    rules = ruleList.keys() 

    # memasukan ke list hit rules yang baru jika fakta sesuai dengan rules dan belum pernah dibangkitkan
    for rule in rules:
        if rule in factList and rule not in allRules and rule not in hitRules:
            tempRules.append(rule)
    
    return tempRules

# fungsi untuk update facts
def updateNewFacts(rule):
    global facts
    global rules

    InsertedFact = rules.get(rule)
    facts.append(InsertedFact)


# Proses inference engine
# Hanya ada 2 tipe yaitu secara DFS atau BFS
def inferenceEngine(tipe, shape):
    global rules
    global facts 
    global hitRules
    global allRules

    if(tipe == "DFS"):
        # inisialisasi proses
        factList = generatePatternFacts(facts)
        hitRules = getHitRules(rules, factList)

        while(len(hitRules) != 0):
            # inisialisasi
            tempRules = []

            # update fakta baru berdasarkan rule pada antrian pertama
            updateNewFacts(hitRules[0])
            allRules.append(hitRules[0])

            # delete rule pertama pada antrian hit rules
            del hitRules[0]

            factList = generatePatternFacts(facts)
            tempRules = getHitRules(rules, factList)

            # memasukan hasil hit rules terbaru ke depan antrian
            temp = hitRules
            del hitRules[0 : len(hitRules)]
            tempRules.extend(temp)
            hitRules = tempRules

            print(facts)
            # break proses jika sudah ditemukan
            if(shape in facts):
                return True

        if(len(hitRules) == 0):
            if shape in facts:
                return True
            else:
                return False
        else:
            return True

    elif(tipe == "BFS"):
        # inisialisasi proses
        factList = generatePatternFacts(facts)
        hitRules = getHitRules(rules, factList)

        while(len(hitRules) != 0):
            # inisialisasi
            tempRules = []

            # update fakta baru berdasarkan rule pada antrian pertama
            updateNewFacts(hitRules[0])
            allRules.append(hitRules[0])

            # delete rule pertama pada antrian hit rules 
            del hitRules[0]

            factList = generatePatternFacts(facts)
            tempRules = getHitRules(rules, factList)

            # memasukan hasil hit rules terbaru ke belakang antrian
            hitRules.extend(tempRules)

            # break proses jika sudah ditemukan
            if(shape in facts):
                del hitRules[0 : len(hitRules)]

        if(len(hitRules) == 0):
            if shape in facts:
                return True
            else:
                return False
        else:
            return True
    else:
        return("Tidak ada tipe")

# mengecek apakah shape yang dipilih ada pada gambar yang dipilih pengguna (shape yang dipilih merupakan subset dari kumpulan gambar)
def runner(allShape, tipe, shapeCheck):
    global rules
    global facts 
    global hitRules
    global allRules

    for shape in allShape:
        facts.extend(shape)
        if (len(facts) != 0):
            check = inferenceEngine(tipe, shapeCheck)
            if (check):
                return True
            else:
                del facts[0 : len(facts)]
    
    return False

######## GUI ########

class FrontEnd(object):
    def __init__(self, master):
        #Welcome page title 1
        self.wpage1 = Label(window, text = "WELCOME TO", fg = "turquoise1", bg = "grey10", font = ("Arial", 60, "bold"))
        self.wpage1.pack()
        self.wpage1.place(relx=0.48, rely=0.2, anchor=CENTER)
        
        
        #Welcome page title 2
        self.wpage2 = Label(window, text = "BADOOR'S YALLA SHAPE RECOGNITOR", fg = "chartreuse2", bg = "grey10", font = ("Arial", 42, "bold"))
        self.wpage2.pack()
        self.wpage2.place(relx=0.48, rely=0.35, anchor=CENTER)
        
        #Start button
        self.bstart = Button(window, width = 40, height = 2, text = "CLICK ME!", fg = "gold", bg = "grey10", activeforeground = "grey10", activebackground = "gold", font = ("Arial", 14), command = self.FirstStart)
        self.bstart.pack()
        self.bstart.place(relx=0.32, rely = 0.55)

        #Quit button
        self.bquit = Button(window, width = 40, height = 2, text = "EXIT", fg = "red2", bg = "grey10", activeforeground = "grey10", activebackground = "red2", font = ("Arial", 14), command = quit)
        self.bquit.pack()
        self.bquit.place(relx=0.32, rely = 0.645)
    
    def FirstStart(self):
        self.bstart.destroy()
        self.wpage1.destroy()
        self.Layout()
    
    def BrowseImage(self):
        global sourcePath
        w = 500
        h = 375
        self.path = filedialog.askopenfilename(title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.img = Image.open(self.path)
        self.imageW, self.imageH = self.img.size
        sourcePath = self.path

        if (self.imageW > self.imageH):
            self.newImgW = w
            factor = self.imageW / w
            self.newImgH = self.imageH / factor
        else:
            self.newImgH = h
            factor = self.imageH / h
            self.newImgW = self.imageW / factor
        
        self.img = self.img.resize((int(self.newImgW), int(self.newImgH)), Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(self.img)
        self.myvar = Label(self.frameImage, image = self.tkimage)
        self.myvar.image = self.tkimage
        self.myvar.pack()

    def ShowShape(self):
        sourcePath = ""
        value = self.var.get()

        if(value != "Select shape"):
            if(value == "Segitiga sama kaki"):
                self.p = "./img/segitiga_kaki.jpg"
                self.choosenShape = "segitigaSamaKaki"
            elif (value == "Segitiga sama kaki lancip"):
                self.p = "./img/segitiga_kaki_lancip.jpg"
                self.choosenShape = "segitigaSamaKakiLancip"
            elif (value == "Segitiga sama kaki siku-siku"):
                self.p = "./img/segitiga_kaki_siku.jpg"
                self.choosenShape = "segitigaSamaKakiSiku"
            elif (value == "Segitiga sama kaki tumpul"):
                self.p = "./img/segitiga_kaki_tumpul.jpg"
                self.choosenShape = "segitigaSamaKakiTumpul"
            elif (value == "Segitiga lancip"):
                self.p = "./img/segitiga_lancip.jpg"
                self.choosenShape = "segitigaLancip"
            elif (value == "Segitiga sama sisi"):
                self.p = "./img/segitiga_sisi.jpg"
                self.choosenShape = "segitigaSamaSisi"
            elif (value == "Segitiga tumpul"):
                self.p = "./img/segitiga_tumpul.jpg"
                self.choosenShape = "segitigaTumpul"
            elif (value == "Segitiga lancip"):
                self.p = "./img/segitiga_lancip.jpg"
                self.choosenShape = "segitigaLancip"
            elif (value == "Segi empat jajar genjang"):
                self.p = "./img/segiempat_jajargenjang.jpg"
                self.choosenShape = "jajaranGenjang"
            elif (value == "Segi empat beraturan"):
                self.p = "./img/segiempat_beraturan.jpg"
                self.choosenShape = "segiempatBeraturan"
            elif (value == "Segi empat layang-layang"):
                self.p = "./img/segiempat_layanglayang.jpg"
                self.choosenShape = "layangLayang"
            elif (value == "Segi empat trapesium"):
                self.p = "./img/segiempat_trapesium.jpg"
                self.choosenShape = "trapesium"
            elif (value == "Segi empat trapesium sama kaki"):
                self.p = "./img/segiempat_trapesium_kaki.jpg"
                self.choosenShape = "trapesiumSamaKaki"
            elif (value == "Segi empat trapesium rata kiri"):
                self.p = "./img/segiempat_trapesium_kiri.jpg"
                self.choosenShape = "trapesiumRataKiri"
            elif (value == "Segi empat trapesium rata kanan"):
                self.p = "./img/segiempat_trapesium_kanan.jpg"
                self.choosenShape = "trapesiumRataKanan"
            elif (value == "Segi lima sembarang"):
                self.p = "./img/segilima_sembarang.jpg"
                self.choosenShape = "segilima"
            elif (value == "Segi lima beraturan"):
                self.p = "./img/segilima_beraturan.jpg"
                self.choosenShape = "segilimaSamaSisi"
            elif (value == "Segi enam sembarang"):
                self.p = "./img/segienam_sembarang.jpg"
                self.choosenShape = "segienam"
            elif (value == "Segi enam beraturan"):
                self.p = "./img/segienam_beraturan.jpg"
                self.choosenShape = "segienamSamaSisi"
            
            sourcePath = self.choosenShape
            self.shape = Image.open(self.p)
            self.tkshape = ImageTk.PhotoImage(self.shape)
            self.showShape = Label(self.frameShape, image = self.tkshape)
            self.showShape.image = self.tkshape
            self.showShape.pack()
    
    def Layout(self):
        self.wpage2.config(fg = "IndianRed2", font = ("Arial", 24, "bold"))
        self.wpage2.pack()
        self.wpage2.place(relx=0.48, rely=0.05, anchor=CENTER)

        self.bquit.config(width = 10, height = 1, font = ("Arial", 10))
        self.bquit.pack()
        self.bquit.place(relx=0.92, rely = 0.935)

        self.bcheck = Button(window, width = 10, height = 1, text = "CHECK!", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 10), command = self.Check)
        self.bcheck.pack()
        self.bcheck.place(relx=0.46, rely=0.45)

        self.labelCheck1 = Label(window, text = "Does your image", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 16, "bold"))
        self.labelCheck1.pack()
        self.labelCheck1.place(relx=0.428, rely=0.3)
        self.labelCheck2 = Label(window, text = "match the shape?", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 16, "bold"))
        self.labelCheck2.pack()
        self.labelCheck2.place(relx=0.425, rely=0.35)

        self.labelImage = Label(window, text = "Your Image", fg = "OliveDrab1", bg = "grey10", font = ("Arial", 12))
        self.labelImage.pack()
        self.labelImage.place(relx=0.16, rely=0.085)
        self.frameImage = Frame(window, width=500, height=375, bg="grey10", highlightbackground = "OliveDrab1", highlightthickness = 2)
        self.frameImage.pack()
        self.frameImage.place(relx=0.02, rely = 0.13)
        self.browseImage = Button(self.frameImage, width = 10, height = 1, text = "BROWSE", fg = "OliveDrab1", bg = "grey10", font = ("Arial", 10), command = self.BrowseImage)
        self.browseImage.pack()
        self.browseImage.place(relx=0.38, rely = 0.45)

        self.labelShape = Label(window, text = "Your Shape", fg = "SeaGreen1", bg = "grey10", font = ("Arial", 12))
        self.labelShape.pack()
        self.labelShape.place(relx=0.76, rely=0.085)
        self.frameShape = Frame(window, width=500, height=375, bg="grey10", highlightbackground = "SeaGreen1", highlightthickness = 2)
        self.frameShape.pack()
        self.frameShape.place(relx=0.61, rely = 0.13)

        self.shapeOptions = [
            "Select shape",
            "Segitiga sama kaki",
            "Segitiga sama kaki lancip",
            "Segitiga sama kaki siku-siku",
            "Segitiga sama kaki tumpul",
            "Segitiga lancip",
            "Segitiga sama sisi",
            "Segitiga tumpul",
            "Segi empat jajar genjang",
            "Segi empat beraturan",
            "Segi empat layang-layang",
            "Segi empat trapesium",
            "Segi empat trapesium sama kaki",
            "Segi empat trapesium rata kiri",
            "Segi empat trapesium rata kanan",
            "Segi lima sembarang",
            "Segi lima beraturan",
            "Segi enam sembarang",
            "Segi enam beraturan"
        ]
        self.var = StringVar(self.frameShape)
        self.var.set(self.shapeOptions[0]) # initial value
        self.show = OptionMenu(* (self.frameShape, self.var) + tuple(self.shapeOptions))
        self.show.configure(fg = "SeaGreen1", bg = "grey10", highlightbackground = "SeaGreen1", highlightthickness = 2, font = ("Arial", 10))
        self.show.pack()
        self.show.place(relx=0.35, rely=0.3)
        self.okImage = Button(self.frameShape, width = 10, height = 1, text = "OK!", fg = "SeaGreen1", bg = "grey10", font = ("Arial", 10), command = self.ShowShape)
        self.okImage.pack()
        self.okImage.place(relx=0.38, rely = 0.45)

        self.labelMatchedFacts = Label(window, text = "Matched Facts", fg = "DarkOrchid3", bg = "grey10", font = ("Arial", 12))
        self.labelMatchedFacts.pack()
        self.labelMatchedFacts.place(relx=0.132, rely=0.675)
        self.frameMatchedFacts = Frame(window, width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameMatchedFacts.pack()
        self.frameMatchedFacts.place(relx=0.02, rely = 0.715)

        self.labelMatchedRules = Label(window, text = "Matched Rules", fg = "DarkOrchid3", bg = "grey10", font = ("Arial", 12))
        self.labelMatchedRules.pack()
        self.labelMatchedRules.place(relx=0.42, rely=0.675)
        self.frameMatchedRules = Frame(window, width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameMatchedRules.pack()
        self.frameMatchedRules.place(relx=0.32, rely = 0.715)

        self.labelDetectionResult = Label(window, text = "Detection Result", fg = "DarkOrchid3", bg = "grey10", font = ("Arial", 12))
        self.labelDetectionResult.pack()
        self.labelDetectionResult.place(relx=0.73, rely=0.675)
        self.frameDetectionResult = Frame(window,width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameDetectionResult.pack()
        self.frameDetectionResult.place(relx=0.62, rely = 0.715)

        self.ruleEditor = Button(window, width = 10, height = 1, text = "Rule Editor", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 10))
        self.ruleEditor.pack()
        self.ruleEditor.place(relx=0.92, rely = 0.716)

        self.showRules = Button(window, width = 10, height = 1, text = "Show Rules", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 10), command = self.ShowAllRules)
        self.showRules.pack()
        self.showRules.place(relx=0.92, rely = 0.76)

        self.showFacts = Button(window, width = 10, height = 1, text = "Show Facts", fg = "AntiqueWhite1", bg = "grey10", font = ("Arial", 10), command = self.ShowAllFacts)
        self.showFacts.pack()
        self.showFacts.place(relx=0.92, rely = 0.805)

        self.breset = Button(window, width = 10, height = 1, text = "RESET", fg = "gold", bg = "grey10", activeforeground = "grey10", activebackground = "gold", font = ("Arial", 10), command = self.ResetLayout)
        self.breset.pack()
        self.breset.place(relx=0.92, rely = 0.85)
    
    def ResetLayout(self):
        if('self.myvar' in globals()):
            self.myvar.destroy()
            
        self.frameImage.destroy()
        self.browseImage.destroy()

        self.frameImage = Frame(window, width=500, height=375, bg="grey10", highlightbackground = "OliveDrab1", highlightthickness = 2)
        self.frameImage.pack()
        self.frameImage.place(relx=0.02, rely = 0.13)
        self.browseImage = Button(self.frameImage, width = 10, height = 1, text = "BROWSE", fg = "OliveDrab1", bg = "grey10", font = ("Arial", 10), command = self.BrowseImage)
        self.browseImage.pack()
        self.browseImage.place(relx=0.38, rely = 0.45)

        if('self.showShape' in globals()):
            self.showShape.destroy()

        self.frameShape.destroy()
        self.show.destroy()
        self.okImage.destroy()
        
        self.frameShape = Frame(window, width=500, height=375, bg="grey10", highlightbackground = "SeaGreen1", highlightthickness = 2)
        self.frameShape.pack()
        self.frameShape.place(relx=0.61, rely = 0.13)
        self.show = OptionMenu(* (self.frameShape, self.var) + tuple(self.shapeOptions))
        self.show.configure(fg = "SeaGreen1", bg = "grey10", highlightbackground = "SeaGreen1", highlightthickness = 2, font = ("Arial", 10))
        self.show.pack()
        self.show.place(relx=0.35, rely=0.3)
        self.okImage = Button(self.frameShape, width = 10, height = 1, text = "ok", fg = "SeaGreen1", bg = "grey10", font = ("Arial", 10), command = self.ShowShape)
        self.okImage.pack()
        self.okImage.place(relx=0.38, rely = 0.45)

        if('self.matchedRules' in globals()):
            self.scrollFacts.destroy()
            self.scrollRules.destroy()
            self.txtFacts.destroy()
            self.txtRules.destroy()
        
        self.frameMatchedFacts.destroy()
        self.frameMatchedRules.destroy()

        self.frameMatchedFacts = Frame(window, width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameMatchedFacts.pack()
        self.frameMatchedFacts.place(relx=0.02, rely = 0.715)
        self.frameMatchedRules = Frame(window, width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameMatchedRules.pack()
        self.frameMatchedRules.place(relx=0.32, rely = 0.715)

        if ('self.showResult' in globals()):
            self.showResult.destroy()
            self.frameDetectionResult.destroy()
            self.sResult.destroy()

        self.frameDetectionResult = Frame(window,width=400, height=185, bg="grey10", highlightbackground = "DarkOrchid3", highlightthickness = 2)
        self.frameDetectionResult.pack()
        self.frameDetectionResult.place(relx=0.62, rely = 0.715)

    def Check(self):
        global outputFact
        global allRules
        global facts

        # inisialisasi
        self.shapeRules = []
        self.shapeFacts = []
        self.result = False

        returnAllFact()
        self.result = runner(outputFact, "DFS", self.choosenShape)
        self.shapeFacts.extend(facts)
        self.shapeRules.extend(allRules)
        self.scrollRules = Scrollbar(self.frameMatchedRules)
        self.scrollRules.pack(side = RIGHT, fill = Y)
        self.scrollFacts = Scrollbar(self.frameMatchedFacts)
        self.scrollFacts.pack(side = RIGHT, fill = Y)

        self.txtRules = Text(self.frameMatchedRules, width=46, height=11)
        self.txtFacts = Text(self.frameMatchedFacts, width=46, height=11)
        self.txtRules.pack(side = LEFT, fill = Y)
        self.txtFacts.pack(side = LEFT, fill = Y)
 
        self.scrollRules.config(command = self.txtRules.yview)
        self.scrollFacts.config(command = self.txtFacts.yview)
 
        self.txtRules.config(yscrollcommand = self.scrollRules.set)
        self.txtFacts.config(yscrollcommand = self.scrollFacts.set)
 
        for x in self.shapeRules:
            self.txtRules.insert(END, x + '\n')
            if(x == self.shapeRules[len(self.shapeRules)-1]):
                self.txtRules.insert(END, "DONE")
 
        for x in self.shapeFacts:
            self.txtFacts.insert(END, x + '\n')

            
        if(self.result):
            self.pResult = "./img/yes.jpg"
        else:
            self.pResult = "./img/no.jpg"
        
        self.sResult = Image.open(self.pResult)
        self.tkResult = ImageTk.PhotoImage(self.sResult)
        self.showResult = Label(self.frameDetectionResult, image = self.tkResult)
        self.showResult.image = self.tkResult
        self.showResult.pack()

    def ShowAllRules(self):
        self.allRules = rules

        self.windowRules = Toplevel()
        self.windowRules.title("All Rules")
        self.windowRules.geometry("800x350")
        self.button = Button(self.windowRules, text="Dismiss", command=self.windowRules.destroy)
        self.button.pack()

        self.scrollAllRules = Scrollbar(self.windowRules)
        self.scrollAllRules.pack(side = RIGHT, fill = Y)
        self.txtAllRules = Text(self.windowRules, width=120, height=30)
        self.txtAllRules.pack(side = LEFT, fill = Y)
        self.scrollAllRules.config(command = self.txtAllRules.yview)
        self.txtAllRules.config(yscrollcommand = self.scrollAllRules.set)

        for x in self.allRules:
            self.txtAllRules.insert(END, 'IF ' + x + ' THEN ' + self.allRules[x] + '\n')
    
    def ShowAllFacts(self):
        self.allFacts = []
        for x in outputFact:
            for y in outputFact:
                self.allFacts.append(y)

        self.windowFacts = Toplevel()
        self.windowFacts.title("All Facts")
        self.windowFacts.geometry("800x350")
        self.button = Button(self.windowFacts, text="Dismiss", command=self.windowFacts.destroy)
        self.button.pack()

        self.scrollAllFacts = Scrollbar(self.windowFacts)
        self.scrollAllFacts.pack(side = RIGHT, fill = Y)
        self.txtAllFacts = Text(self.windowFacts, width=120, height=30)
        self.txtAllFacts.pack(side = LEFT, fill = Y)
        self.scrollAllFacts.config(command = self.txtAllFacts.yview)
        self.txtAllFacts.config(yscrollcommand = self.scrollAllFacts.set)

        for x in self.allFacts:
            self.txtAllFacts.insert(END, x + '\n')


window = Tk()
window.title("BADOOR'S YALLA SHAPE RECOGNITION")
window.configure(background = "gray10")
window.geometry("1366x786")

play = FrontEnd(window)

def main():
    window.mainloop()

main()
