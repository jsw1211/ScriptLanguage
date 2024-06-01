from tkinter import *
from tkinter import font


class mailGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('메일 시스템')
        self.window.geometry('400x200')

        self.mailFont = font.Font(self.window, size=16, weight='bold', family='굴림')
        self.mailFontB = font.Font(self.window, size=32, weight='bold', family='굴림')

        self.mailStr = StringVar()
        entry = Entry(self.window, textvariable=self.mailStr, font=self.mailFont)
        entry.place(x=50, y=50, width=300, height=25)
        button = Button(self.window, text='보내기', command=self.pressedSend, font=self.mailFontB)
        button.place(x=100, y=100, width=200, height=80)

        self.window.mainloop()

    def pressedSend(self):
        pass
