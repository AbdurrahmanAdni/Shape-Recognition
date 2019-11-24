from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import bridge as bg

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
        w = 500
        h = 375
        self.path = filedialog.askopenfilename(title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.img = Image.open(self.path)
        self.imageW, self.imageH = self.img.size

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
        value = self.var.get()
        if(value != "Select shape"):
            if(value == "Segitiga sama kaki"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_kaki.jpg"
            elif (value == "Segitiga sama kaki lancip"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_kaki_lancip.jpg"
            elif (value == "Segitiga sama kaki siku-siku"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_kaki_siku.jpg"
            elif (value == "Segitiga sama kaki tumpul"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_kaki_tumpul.jpg"
            elif (value == "Segitiga lancip"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_lancip.jpg"
            elif (value == "Segitiga sama sisi"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_sisi.jpg"
            elif (value == "Segitiga tumpul"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_tumpul.jpg"
            elif (value == "Segitiga lancip"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segitiga_lancip.jpg"
            elif (value == "Segi empat jajar genjang"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_jajargenjang.jpg"
            elif (value == "Segi empat beraturan"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_beraturan.jpg"
            elif (value == "Segi empat layang-layang"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_layanglayang.jpg"
            elif (value == "Segi empat trapesium"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_trapesium.jpg"
            elif (value == "Segi empat trapesium sama kaki"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_trapesium_kaki.jpg"
            elif (value == "Segi empat trapesium rata kiri"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_trapesium_kiri.jpg"
            elif (value == "Segi empat trapesium rata kanan"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segiempat_trapesium_kanan.jpg"
            elif (value == "Segi lima sembarang"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segilima_sembarang.jpg"
            elif (value == "Segi lima beraturan"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segilima_beraturan.jpg"
            elif (value == "Segi enam sembarang"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segienam_sembarang.jpg"
            elif (value == "Segi enam beraturan"):
                self.p = "D:/Documents/GitHub/Shape-Recognition/img/segienam_beraturan.jpg"

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
            "Segi empat jajar genjang"
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
    
    def Check(self):
        self.matchedRules = bg.matchedRules()
        self.matchedFacts = bg.matchedFacts()

        self.scrollRules = Scrollbar(self.frameMatchedRules)
        self.scrollFacts = Scrollbar(self.frameMatchedFacts)
        self.scrollRules.pack(side = RIGHT, fill = Y)
        self.scrollFacts.pack(side = RIGHT, fill = Y)

        self.txtRules = Text(self.frameMatchedRules, width=46, height=11)
        self.txtFacts = Text(self.frameMatchedFacts, width=46, height=11)
        self.txtRules.pack(side = LEFT, fill = Y)
        self.txtFacts.pack(side = LEFT, fill = Y)

        self.scrollRules.config(command = self.txtRules.yview)
        self.scrollFacts.config(command = self.txtFacts.yview)

        self.txtRules.config(yscrollcommand = self.scrollRules.set)
        self.txtFacts.config(yscrollcommand = self.scrollFacts.set)

        for x in self.matchedRules:
            self.txtRules.insert(END, x + '\n')

        for x in self.matchedFacts:
            self.txtFacts.insert(END, x + '\n')

    def ShowAllRules(self):
        self.allRules = bg.matchedRules()

        self.windowRules = Toplevel()
        self.windowRules.title("All Rules")
        self.windowRules.geometry("600x350")
        self.button = Button(self.windowRules, text="Dismiss", command=self.windowRules.destroy)
        self.button.pack()

        self.scrollAllRules = Scrollbar(self.windowRules)
        self.scrollAllRules.pack(side = RIGHT, fill = Y)
        self.txtAllRules = Text(self.windowRules, width=80, height=30)
        self.txtAllRules.pack(side = LEFT, fill = Y)
        self.scrollAllRules.config(command = self.txtAllRules.yview)
        self.txtAllRules.config(yscrollcommand = self.scrollAllRules.set)

        for x in self.allRules:
            self.txtAllRules.insert(END, x + '\n')
    
    def ShowAllFacts(self):
        self.allFacts = bg.matchedFacts()

        self.windowFacts = Toplevel()
        self.windowFacts.title("All Facts")
        self.windowFacts.geometry("600x350")
        self.button = Button(self.windowFacts, text="Dismiss", command=self.windowFacts.destroy)
        self.button.pack()

        self.scrollAllFacts = Scrollbar(self.windowFacts)
        self.scrollAllFacts.pack(side = RIGHT, fill = Y)
        self.txtAllFacts = Text(self.windowFacts, width=80, height=30)
        self.txtAllFacts.pack(side = LEFT, fill = Y)
        self.scrollAllFacts.config(command = self.txtAllFacts.yview)
        self.txtAllFacts.config(yscrollcommand = self.scrollAllFacts.set)

        for x in self.allFacts:
            self.txtAllFacts.insert(END, x + '\n')


# class AutoScrollbar(Scrollbar):
#     # a scrollbar that hides itself if it's not needed.  only
#     # works if you use the grid geometry manager.
#     def set(self, lo, hi):
#         if float(lo) <= 0.0 and float(hi) >= 1.0:
#             # grid_remove is currently missing from Tkinter!
#             self.tk.call("grid", "remove", self)
#         else:
#             self.grid()
#         Scrollbar.set(self, lo, hi)
#     def pack(self, **kw):
#         raise TclError, "cannot use pack with this widget"
#     def place(self, **kw):
#         raise TclError, "cannot use place with this widget"

window = Tk()
window.title("BADOOR'S YALLA SHAPE RECOGNITION")
window.configure(background = "gray10")
window.geometry("1366x786")
# scrollbar = Scrollbar(window)
# scrollbar.pack(side = RIGHT, fill = Y)
# scrollbar.config(command = window.yview)

play = FrontEnd(window)

def main():
    window.mainloop()

main()