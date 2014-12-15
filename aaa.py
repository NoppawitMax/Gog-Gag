import Tkinter
import random
import tkFont

class simpleapp_tk(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.started = False # True when timer is running

    def initialize(self):
        self.grid()

        self.infoVariable = Tkinter.StringVar()
        self.labelInfo = Tkinter.Label(self, textvariable=self.infoVariable, font="Angsana")
        self.labelInfo.place(x=290, y=30)
        self.infoVariable.set(u"Press button to start!")

        self.scoreVariable = Tkinter.StringVar()
        self.labelScore = Tkinter.Label(self, textvariable=self.scoreVariable, font="Angsana")
        self.labelScore.place(x=25, y=50)
        self.scoreVariable.set(u"Score :")

        self.buttonStart = Tkinter.Button(self, text=u"Start", command=self.on_buttonStart, height=2, width=8)
        self.buttonStart.place(x=600, y=60)

        self.timeVariable = Tkinter.StringVar()
        self.labelTime = Tkinter.Label(self, textvariable=self.timeVariable, font="Angsana")
        self.labelTime.place(x=25, y=80)
        self.timeVariable.set(u'Time : ')

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable, fg="black", bg="white", width = 48, font="Angsana")
        self.entry.place(x=140, y=70)
        self.entryVariable.set(u"")
        self.entry.bind('<Key>', self.on_key) # event


        self.q = Tkinter.Button(self, text='q', height=2, width=6)
        self.q.place(x=45, y=200)
        self.w = Tkinter.Button(self, text='w', height=2, width=6)
        self.w.place(x=96, y=200)
        self.e = Tkinter.Button(self, text='e', height=2, width=6)
        self.e.place(x=147, y=200)
        self.r = Tkinter.Button(self, text='r', height=2, width=6)
        self.r.place(x=198, y=200)
        self.t = Tkinter.Button(self, text='t', height=2, width=6)
        self.t.place(x=249, y=200)
        self.y = Tkinter.Button(self, text='y', height=2, width=6)
        self.y.place(x=300, y=200)
        self.u = Tkinter.Button(self, text='u', height=2, width=6)
        self.u.place(x=351, y=200)
        self.i = Tkinter.Button(self, text='i', height=2, width=6)
        self.i.place(x=402, y=200)
        self.o = Tkinter.Button(self, text='o', height=2, width=6)
        self.o.place(x=453, y=200)
        self.p = Tkinter.Button(self, text='p', height=2, width=6)
        self.p.place(x=504, y=200)
        self.l_bracket = Tkinter.Button(self, text='[', height=2, width=6)
        self.l_bracket.place(x=555, y=200)
        self.r_bracket = Tkinter.Button(self, text=']', height=2, width=6)
        self.r_bracket.place(x=606, y=200)


        self.a = Tkinter.Button(self, text='a', height=2, width=6)
        self.a.place(x=70, y=240)
        self.s = Tkinter.Button(self, text='s', height=2, width=6)
        self.s.place(x=121, y=240)
        self.d = Tkinter.Button(self, text='d', height=2, width=6)
        self.d.place(x=172, y=240)
        self.f = Tkinter.Button(self, text='f', height=2, width=6)
        self.f.place(x=223, y=240)
        self.g = Tkinter.Button(self, text='g', height=2, width=6)
        self.g.place(x=274, y=240)
        self.h = Tkinter.Button(self, text='h', height=2, width=6)
        self.h.place(x=325, y=240)
        self.j = Tkinter.Button(self, text='j', height=2, width=6)
        self.j.place(x=376, y=240)
        self.k = Tkinter.Button(self, text='k', height=2, width=6)
        self.k.place(x=427, y=240)
        self.l = Tkinter.Button(self, text='l', height=2, width=6)
        self.l.place(x=478, y=240)
        self.semi_Colon = Tkinter.Button(self, text=';', height=2, width=6)
        self.semi_Colon.place(x=529, y=240)
        self.quote = Tkinter.Button(self, text='\'', height=2, width=6)
        self.quote.place(x=580, y=240)

        self.shift_L = Tkinter.Button(self, text='shift', height=2, width=8)
        self.shift_L.place(x=30, y=280)
        self.z = Tkinter.Button(self, text='z', height=2, width=6)
        self.z.place(x=95, y=280)
        self.x = Tkinter.Button(self, text='x', height=2, width=6)
        self.x.place(x=146, y=280)
        self.c = Tkinter.Button(self, text='c', height=2, width=6)
        self.c.place(x=197, y=280)
        self.v = Tkinter.Button(self, text='v', height=2, width=6)
        self.v.place(x=248, y=280)
        self.b = Tkinter.Button(self, text='b', height=2, width=6)
        self.b.place(x=299, y=280)
        self.n = Tkinter.Button(self, text='n', height=2, width=6)
        self.n.place(x=350, y=280)
        self.m = Tkinter.Button(self, text='m', height=2, width=6)
        self.m.place(x=401, y=280)
        self.comma = Tkinter.Button(self, text=',', height=2, width=6)
        self.comma.place(x=452, y=280)
        self.dot = Tkinter.Button(self, text='.', height=2, width=6)
        self.dot.place(x=503, y=280)
        self.slash = Tkinter.Button(self, text='/', height=2, width=6)
        self.slash.place(x=554, y=280)
        self.shift_R = Tkinter.Button(self, text='shift', height=2, width=8)
        self.shift_R.place(x=605, y=280)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.resizable(True,True)


    def on_buttonStart(self):
        if not self.started:
            # reset values
            self.started = True
            self.number_of_letters = 100
            self.score = 0
            self.time = 0.0
            # select first letter
            self.randletter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            if self.randletter == 'Q':
                self.q.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'W':
                self.w.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'E':
                self.e.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'R':
                self.r.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'T':
                self.t.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'A':
                self.a.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'S':
                self.s.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'D':
                self.d.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'F':
                self.f.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'G':
                self.g.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'Z':
                self.z.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'X':
                self.x.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'C':
                self.c.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'V':
                self.v.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'B':
                self.b.config(bg='red')
                self.shift_R.config(bg='red')
            if self.randletter == 'Y':
                self.y.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'U':
                self.u.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'I':
                self.i.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'O':
                self.o.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'P':
                self.p.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'H':
                self.h.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'J':
                self.j.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'K':
                self.k.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'L':
                self.l.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'N':
                self.n.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'M':
                self.m.config(bg='red')
                self.shift_L.config(bg='red')
            if self.randletter == 'q':
                self.q.config(bg='red')
            if self.randletter == 'w':
                self.w.config(bg='red')
            if self.randletter == 'e':
                self.e.config(bg='red')
            if self.randletter == 'r':
                self.r.config(bg='red')
            if self.randletter == 't':
                self.t.config(bg='red')
            if self.randletter == 'y':
                self.y.config(bg='red')
            if self.randletter == 'u':
                self.u.config(bg='red')
            if self.randletter == 'i':
                self.i.config(bg='red')
            if self.randletter == 'o':
                self.o.config(bg='red')
            if self.randletter == 'p':
                self.p.config(bg='red')
            if self.randletter == 'a':
                self.a.config(bg='red')
            if self.randletter == 's':
                self.s.config(bg='red')
            if self.randletter == 'd':
                self.d.config(bg='red')
            if self.randletter == 'f':
                self.f.config(bg='red')
            if self.randletter == 'g':
                self.g.config(bg='red')
            if self.randletter == 'h':
                self.h.config(bg='red')
            if self.randletter == 'j':
                self.j.config(bg='red')
            if self.randletter == 'k':
                self.k.config(bg='red')
            if self.randletter == 'l':
                self.l.config(bg='red')
            if self.randletter == 'z':
                self.z.config(bg='red')
            if self.randletter == 'x':
                self.x.config(bg='red')
            if self.randletter == 'c':
                self.c.config(bg='red')
            if self.randletter == 'v':
                self.v.config(bg='red')
            if self.randletter == 'b':
                self.b.config(bg='red')
            if self.randletter == 'n':
                self.n.config(bg='red')
            if self.randletter == 'm':
                self.m.config(bg='red')
            # show first letter and score
            self.infoVariable.set(self.randletter)
            # start timer
            self.after(100, self.timer)

    def on_key(self, event):
        if not self.started:
            self.entryVariable.set('')
        else:
            if event.char == self.randletter:
                self.q.config(bg='#F0F0F0')
                self.w.config(bg='#F0F0F0')
                self.e.config(bg='#F0F0F0')
                self.r.config(bg='#F0F0F0')
                self.t.config(bg='#F0F0F0')
                self.y.config(bg='#F0F0F0')
                self.u.config(bg='#F0F0F0')
                self.i.config(bg='#F0F0F0')
                self.o.config(bg='#F0F0F0')
                self.p.config(bg='#F0F0F0')
                self.a.config(bg='#F0F0F0')
                self.s.config(bg='#F0F0F0')
                self.d.config(bg='#F0F0F0')
                self.f.config(bg='#F0F0F0')
                self.g.config(bg='#F0F0F0')
                self.h.config(bg='#F0F0F0')
                self.j.config(bg='#F0F0F0')
                self.k.config(bg='#F0F0F0')
                self.l.config(bg='#F0F0F0')
                self.z.config(bg='#F0F0F0')
                self.x.config(bg='#F0F0F0')
                self.c.config(bg='#F0F0F0')
                self.v.config(bg='#F0F0F0')
                self.b.config(bg='#F0F0F0')
                self.n.config(bg='#F0F0F0')
                self.m.config(bg='#F0F0F0')
                self.shift_R.config(bg='#F0F0F0')
                self.shift_L.config(bg='#F0F0F0')
                print 'Correct', event.char
                self.score += 10
                self.randletter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                self.infoVariable.set(self.randletter)
                self.scoreVariable.set('Score : ' + str(self.score))
                
                if self.randletter == 'Q':
                    self.q.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'W':
                    self.w.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'E':
                    self.e.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'R':
                    self.r.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'T':
                    self.t.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'A':
                    self.a.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'S':
                    self.s.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'D':
                    self.d.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'F':
                    self.f.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'G':
                    self.g.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'Z':
                    self.z.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'X':
                    self.x.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'C':
                    self.c.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'V':
                    self.v.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'B':
                    self.b.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'Y':
                    self.y.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'U':
                    self.u.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'I':
                    self.i.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'O':
                    self.o.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'P':
                    self.p.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'H':
                    self.h.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'J':
                    self.j.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'K':
                    self.k.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'L':
                    self.l.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'N':
                    self.n.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'M':
                    self.m.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'q':
                    self.q.config(bg='red')
                if self.randletter == 'w':
                    self.w.config(bg='red')
                if self.randletter == 'e':
                    self.e.config(bg='red')
                if self.randletter == 'r':
                    self.r.config(bg='red')
                if self.randletter == 't':
                    self.t.config(bg='red')
                if self.randletter == 'y':
                    self.y.config(bg='red')
                if self.randletter == 'u':
                    self.u.config(bg='red')
                if self.randletter == 'i':
                    self.i.config(bg='red')
                if self.randletter == 'o':
                    self.o.config(bg='red')
                if self.randletter == 'p':
                    self.p.config(bg='red')
                if self.randletter == 'a':
                    self.a.config(bg='red')
                if self.randletter == 's':
                    self.s.config(bg='red')
                if self.randletter == 'd':
                    self.d.config(bg='red')
                if self.randletter == 'f':
                    self.f.config(bg='red')
                if self.randletter == 'q':
                    self.q.config(bg='red')
                if self.randletter == 'w':
                    self.w.config(bg='red')
                if self.randletter == 'e':
                    self.e.config(bg='red')
                if self.randletter == 'r':
                    self.r.config(bg='red')
                if self.randletter == 't':
                    self.t.config(bg='red')
                if self.randletter == 'y':
                    self.y.config(bg='red')
                if self.randletter == 'u':
                    self.u.config(bg='red')
                if self.randletter == 'i':
                    self.i.config(bg='red')
                if self.randletter == 'o':
                    self.o.config(bg='red')
                if self.randletter == 'p':
                    self.p.config(bg='red')
                if self.randletter == 'a':
                    self.a.config(bg='red')
                if self.randletter == 's':
                    self.s.config(bg='red')
                if self.randletter == 'd':
                    self.d.config(bg='red')
                if self.randletter == 'f':
                    self.f.config(bg='red')
                if self.randletter == 'g':
                    self.g.config(bg='red')
                if self.randletter == 'h':
                    self.h.config(bg='red')
                if self.randletter == 'j':
                    self.j.config(bg='red')
                if self.randletter == 'k':
                    self.k.config(bg='red')
                if self.randletter == 'l':
                    self.l.config(bg='red')
                if self.randletter == 'z':
                    self.z.config(bg='red')
                if self.randletter == 'x':
                    self.x.config(bg='red')
                if self.randletter == 'c':
                    self.c.config(bg='red')
                if self.randletter == 'v':
                    self.v.config(bg='red')
                if self.randletter == 'b':
                    self.b.config(bg='red')
                if self.randletter == 'n':
                    self.n.config(bg='red')
                if self.randletter == 'm':
                    self.m.config(bg='red')

            elif event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
                pass
            elif event.char != self.randletter:
                self.q.config(bg='#F0F0F0')
                self.w.config(bg='#F0F0F0')
                self.e.config(bg='#F0F0F0')
                self.r.config(bg='#F0F0F0')
                self.t.config(bg='#F0F0F0')
                self.y.config(bg='#F0F0F0')
                self.u.config(bg='#F0F0F0')
                self.i.config(bg='#F0F0F0')
                self.o.config(bg='#F0F0F0')
                self.p.config(bg='#F0F0F0')
                self.a.config(bg='#F0F0F0')
                self.s.config(bg='#F0F0F0')
                self.d.config(bg='#F0F0F0')
                self.f.config(bg='#F0F0F0')
                self.g.config(bg='#F0F0F0')
                self.h.config(bg='#F0F0F0')
                self.j.config(bg='#F0F0F0')
                self.k.config(bg='#F0F0F0')
                self.l.config(bg='#F0F0F0')
                self.z.config(bg='#F0F0F0')
                self.x.config(bg='#F0F0F0')
                self.c.config(bg='#F0F0F0')
                self.v.config(bg='#F0F0F0')
                self.b.config(bg='#F0F0F0')
                self.n.config(bg='#F0F0F0')
                self.m.config(bg='#F0F0F0')
                self.shift_R.config(bg='#F0F0F0')
                self.shift_L.config(bg='#F0F0F0')

                print 'Incorrect', event.char
                self.randletter = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                self.infoVariable.set(self.randletter)
                self.scoreVariable.set('Score : ' + str(self.score))
                if self.randletter == 'Q':
                    self.q.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'W':
                    self.w.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'E':
                    self.e.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'R':
                    self.r.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'T':
                    self.t.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'A':
                    self.a.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'S':
                    self.s.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'D':
                    self.d.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'F':
                    self.f.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'G':
                    self.g.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'Z':
                    self.z.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'X':
                    self.x.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'C':
                    self.c.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'V':
                    self.v.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'B':
                    self.b.config(bg='red')
                    self.shift_R.config(bg='red')
                if self.randletter == 'Y':
                    self.y.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'U':
                    self.u.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'I':
                    self.i.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'O':
                    self.o.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'P':
                    self.p.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'H':
                    self.h.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'J':
                    self.j.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'K':
                    self.k.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'L':
                    self.l.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'N':
                    self.n.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'M':
                    self.m.config(bg='red')
                    self.shift_L.config(bg='red')
                if self.randletter == 'q':
                    self.q.config(bg='red')
                if self.randletter == 'w':
                    self.w.config(bg='red')
                if self.randletter == 'e':
                    self.e.config(bg='red')
                if self.randletter == 'r':
                    self.r.config(bg='red')
                if self.randletter == 't':
                    self.t.config(bg='red')
                if self.randletter == 'y':
                    self.y.config(bg='red')
                if self.randletter == 'u':
                    self.u.config(bg='red')
                if self.randletter == 'i':
                    self.i.config(bg='red')
                if self.randletter == 'o':
                    self.o.config(bg='red')
                if self.randletter == 'p':
                    self.p.config(bg='red')
                if self.randletter == 'a':
                    self.a.config(bg='red')
                if self.randletter == 's':
                    self.s.config(bg='red')
                if self.randletter == 'd':
                    self.d.config(bg='red')
                if self.randletter == 'f':
                    self.f.config(bg='red')
                if self.randletter == 'g':
                    self.g.config(bg='red')
                if self.randletter == 'h':
                    self.h.config(bg='red')
                if self.randletter == 'j':
                    self.j.config(bg='red')
                if self.randletter == 'k':
                    self.k.config(bg='red')
                if self.randletter == 'l':
                    self.l.config(bg='red')
                if self.randletter == 'z':
                    self.z.config(bg='red')
                if self.randletter == 'x':
                    self.x.config(bg='red')
                if self.randletter == 'c':
                    self.c.config(bg='red')
                if self.randletter == 'v':
                    self.v.config(bg='red')
                if self.randletter == 'b':
                    self.b.config(bg='red')
                if self.randletter == 'n':
                    self.n.config(bg='red')
                if self.randletter == 'm':
                    self.m.config(bg='red')

            self.number_of_letters -= 1

            if self.number_of_letters == 0:
                self.started = False
                self.entryVariable.set('')
                self.infoVariable.set('Score : ' + str(self.score))

        
        
    def timer(self):
        if self.started:
            self.entry.focus()
            self.time += .1
            self.timeVariable.set('Time : ' + str(round(self.time,1)) )
            self.after(100, self.timer)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('LoL Practice')
    app.geometry("700x500")
    app.mainloop()
