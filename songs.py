class NoteLine:
    def __init__(self, a=False, b=False, c=False, d=False, e=False):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

class Song:
    def __init__(self, fileName):
        self.noteLines = []
        file = open(fileName, "r")
        lines = file.readlines()[0].split("/")
        for l in lines:
            ret = NoteLine()
            notes = l.split("-")
            for n in notes:
                if n == "1":
                    ret.a = True
                if n == "2":
                    ret.b = True
                if n == "3":
                    ret.c = True
                if n == "4":
                    ret.d = True
                if n == "5":
                    ret.e = True
            self.noteLines.append(ret)
            ret = NoteLine()

    def debugprint(self):
        for l in self.noteLines:
            print(l.a, l.b, l.c, l.d, l.e)