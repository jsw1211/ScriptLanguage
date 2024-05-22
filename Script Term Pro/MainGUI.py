from tkinter import *
import tkinter.ttk


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('프로그램 이름')
        self.window.geometry('800x600')

        self.notebook = tkinter.ttk.Notebook(self.window, width=800, height=600)
        self.notebook.pack()

        frame1 = Frame(self.window)  # 캐릭터 정보 검색 기능
        self.notebook.add(frame1, text='캐릭터 정보')
        Label(frame1, text='캐릭터 정보를 조회', fg='red', font='helvetica 48').pack()

        frame2 = Frame(self.window)  # 랭킹 기능
        self.notebook.add(frame2, text='랭킹 정보')
        Label(frame2, text='랭킹을 보여줌', fg='blue', font='helvetica 48').pack()

        frame3 = Frame(self.window)  # 확률 정보 기능
        self.notebook.add(frame3, text='확률 정보')
        Label(frame3, text='인게임 확률 통계를 보여줌', fg='green', font='helvetica 48').pack()

        frame4 = Frame(self.window)  # 팝업스토어 위치 지도 기능
        self.notebook.add(frame4, text='팝업스토어')
        Label(frame4, text='팝업스토어 위치를 지도로', fg='black', font='helvetica 48').pack()

        self.window.mainloop()


MainGUI()