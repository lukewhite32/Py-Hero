from tkinter import *
import time
from songs import NoteLine, Song

s = Song("song1.txt")
s.debugprint()

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = Tk()
        self.canvas = Canvas(self.window, height=height, width=width)

        self.canvas.pack()

        self.score = 0
        self.song = Song("song1.txt")
        self.notePattern = self.song.noteLines
        self.currentNotes = 0
        self.yOffset = 0
        self.multiplier = 1
        self.currentLine = NoteLine(False, False, False, False, False)
        self.window.bind("<Key>", self.handleButtonInput)

    def updateNotes(self):
        y = self.height + self.yOffset
        for x in range(self.currentNotes, self.currentNotes+16):
            if self.notePattern[x].a:
                self.canvas.create_oval(200,y-10,220,y)
            if self.notePattern[x].b:
                self.canvas.create_oval(245,y-10,265,y)
            if self.notePattern[x].c:
                self.canvas.create_oval(290,y-10,310,y)
            if self.notePattern[x].d:
                self.canvas.create_oval(335,y-10,355,y)
            if self.notePattern[x].e:
                self.canvas.create_oval(380,y-10,400,y)
            if y == (self.height-80):
                print("settin currentline to b ", self.notePattern[x].b)
                if (self.currentLine.a or self.currentLine.b or self.currentLine.c or self.currentLine.d or self.currentLine.e):
                    self.multiplier = 1
                    self.score -= 10
                self.currentLine = self.notePattern[x]
            y -= 10
        self.yOffset += 2
        if self.yOffset == 8:
            self.currentNotes += 1
            self.yOffset = 0

    def update(self):
        self.updateNotes()
        self.window.update()
        #time.sleep(.0001)
        self.canvas.delete("all")
        self.canvas.create_line(200, 0, 200, self.height, fill="black", width=5)
        self.canvas.create_line(self.width-200, 0, self.width-200, self.height, fill="black", width=5)
        self.canvas.create_line(0, self.height-80, self.width, self.height-80, fill="black", width=5)
        self.canvas.create_text(20,20,fill="darkblue",font="Times 20 italic bold",
                        text=self.score)

    def noteA(self):
        if self.currentLine.a:
            self.currentLine.a = False
            self.score += 10 * self.multiplier
        else:
            self.score -= 10
 
    def noteB(self):
        if self.currentLine.b:
            self.currentLine.b = False
            self.score += 10 * self.multiplier
        else:
            self.score -= 10

    def noteC(self):
        if self.currentLine.c:
            self.currentLine.c = False
            self.score += 10 * self.multiplier
        else:
            self.score -= 10

    def noteD(self):
        if self.currentLine.d:
            self.currentLine.d = False
            self.score += 10 * self.multiplier
        else:
            self.score -= 10

    def noteE(self):
        if self.currentLine.e:
            self.currentLine.e = False
            self.score += 10 * multiplier
        else:
            self.score -= 10

    def handleButtonInput(self, event):
        if event.char == "a":
            self.noteA()
        if event.char == "s":
            self.noteB()
        if event.char == "d":
            self.noteC()
        if event.char == "f":
            self.noteD()
        if event.char == "g":
            self.noteE()


game = Game(600, 400)
while 1:
    game.update()