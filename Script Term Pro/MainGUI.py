from tkinter import *
from tkinter import font
import tkinter.ttk
from PIL import Image, ImageTk


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('메이플스토리(임시)')
        self.window.geometry('600x800')

        self.font = font.Font(self.window, size=16, weight='bold', family='굴림')
        self.fontB = font.Font(self.window, size=16, weight='bold', family='arial')

        image = Image.open('Resource/Image/tempCharImage.png')
        image = image.resize((200, 200))
        self.testImage = ImageTk.PhotoImage(image)

        self.notebook = tkinter.ttk.Notebook(self.window, width=800, height=600)
        self.notebook.pack()

        #
        #
        #
        frame1 = Frame(self.window)  # 캐릭터 정보 검색 기능
        self.notebook.add(frame1, text='캐릭터 정보')
        # Label(frame1, text='캐릭터 정보를 조회', fg='red', font='helvetica 48').pack()
        frame1_1 = Frame(frame1, width=600, height=100)
        frame1_1.pack()
        self.searchStr = StringVar()
        Entry(frame1_1, textvariable=self.searchStr, width=20, justify=LEFT, font=self.font).place(x=50, y=50)
        Button(frame1_1, text='돋보기', width=5, height=1, command=self.pressedSearch, font=self.fontB).place(x=320, y=45)
        Button(frame1_1, text='별', width=3, height=1, command=self.pressedFavorite, font=self.fontB).place(x=450, y=45)
        Button(frame1_1, text='메일', width=3, height=1, command=self.pressedMail, font=self.fontB).place(x=510, y=45)

        frame1_2 = Frame(frame1, width=600, height=700)
        frame1_2.pack()
        frame1_2_1 = Frame(frame1_2, width=160, height=200, bg='#ede0c8')
        frame1_2_1.place(x=50, y=50)
        frame1_2_1_1 = Frame(frame1_2_1, width=140, height=180)
        frame1_2_1_1.pack_propagate(False)
        frame1_2_1_1.pack(padx=10, pady=10)
        self.charImageLabel = Label(frame1_2_1_1, text='이미지', image=self.testImage, width=140, height=180, padx=10, pady=10)
        self.charImageLabel.pack(anchor='center', fill='both')
        frame1_2_2 = Frame(frame1_2, width=290, height=200, bg='red')
        frame1_2_2.place(x=270, y=50)
        name = '김땡땡'    # 테스트용
        self.charNameLabel = Label(frame1_2_2, text=name, font=self.font)
        self.charNameLabel.place(x=10, y=10)
        level = 250     # 토스트용
        self.charLevelLabel = Label(frame1_2_2, text='Lv '+str(level), font=self.font)
        self.charLevelLabel.place(x=100, y=10)
        server = '스카니아'     # 텨스트용
        self.charServerLabel = Label(frame1_2_2, text='서버 - '+server, font=self.font)
        self.charServerLabel.place(x=10, y=50)
        guild = '지존'    # 임시
        self.charGuildLabel = Label(frame1_2_2, text='길드 - '+guild, font=self.font)
        self.charGuildLabel.place(x=10, y=90)
        popular = 999   # 비둘기
        self.charPopularLabel = Label(frame1_2_2, text='인기도 - '+str(popular), font=self.font)
        self.charPopularLabel.place(x=10, y=130)

        #
        #
        #
        frame2 = Frame(self.window)  # 랭킹 기능
        self.notebook.add(frame2, text='랭킹 정보')
        Label(frame2, text='랭킹을 보여줌', fg='blue', font='helvetica 48').pack()

        #
        #
        #
        frame3 = Frame(self.window)  # 확률 정보 기능
        self.notebook.add(frame3, text='확률 정보')
        Label(frame3, text='인게임 확률 통계를 보여줌', fg='green', font='helvetica 48').pack()

        #
        #
        #
        frame4 = Frame(self.window)  # 팝업스토어 위치 지도 기능
        self.notebook.add(frame4, text='팝업스토어')
        Label(frame4, text='팝업스토어 위치를 지도로', fg='black', font='helvetica 48').pack()

        self.window.mainloop()

    def pressedSearch(self):
        pass

    def pressedFavorite(self):
        pass

    def pressedMail(self):
        pass


MainGUI()
