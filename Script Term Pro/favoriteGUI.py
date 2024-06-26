from tkinter import *
from tkinter import font
import fio

items = ['이덱']


class favoriteGUI:
    instance = None

    def __init__(self, parent):
        if favoriteGUI.instance is not None:
            return

        favoriteGUI.instance = self
        self.parent = parent

        self.window = Toplevel(self.parent.window)
        self.window.title('즐겨찾기 목록')
        self.window.geometry('400x700')
        self.window.protocol("WM_DELETE_WINDOW", self.onClose)

        self.favFont = font.Font(self.window, size=16, weight='bold', family='메이플스토리')
        self.favFontB = font.Font(self.window, size=32, weight='bold', family='메이플스토리')

        frame = Frame(self.window, width=400, height=700, bg='#7cf496')
        frame.pack()

        Label(frame, text='항목', font=self.favFontB, bg='#b6dd77', borderwidth=2, relief='groove').place(x=100, y=40, width=200, height=80)

        self.listbox = Listbox(frame, selectmode=SINGLE, font=self.favFont)
        self.listbox.place(x=50, y=150, width=300, height=400)
        self.itemLoadListbox()

        bWid = 100
        bHei = 40
        Button(frame, text='선택', font=self.favFont, command=self.pressedSelect).place(x=80, y=570, width=bWid, height=bHei)
        Button(frame, text='삭제', font=self.favFont, command=self.pressedDelete).place(x=220, y=570, width=bWid, height=bHei)
        Button(frame, text='저장', font=self.favFont, command=self.pressedSave).place(x=80, y=630, width=bWid, height=bHei)
        Button(frame, text='불러오기', font=self.favFont, command=self.pressedLoad).place(x=220, y=630, width=bWid, height=bHei)

        self.window.mainloop()

    def pressedSelect(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_text = self.listbox.get(selected_index)
            self.parent.searchStr.set(selected_text)
            self.parent.pressedSearch()
        else:
            return
        self.onClose()

    def pressedDelete(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)

    def pressedSave(self):
        fio.save(items)

    def pressedLoad(self):
        global items
        items = fio.load()
        self.listbox.delete(0, END)
        self.itemLoadListbox()

    def itemLoadListbox(self):
        for item in items:
            self.listbox.insert(END, item)

    def appendItem(self, name):
        self.listbox.insert(END, name)

    def onClose(self):
        favoriteGUI.instance = None
        self.parent = None
        self.window.destroy()
