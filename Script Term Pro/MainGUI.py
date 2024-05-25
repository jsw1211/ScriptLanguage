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
        self.fontS = font.Font(self.window, size=8, weight='bold', family='굴림')
        self.fontB = font.Font(self.window, size=16, weight='bold', family='arial')
        self.fontT = font.Font(self.window, size=24, weight='bold', family='굴림')
        self.fontV = font.Font(self.window, size=28, weight='bold', family='굴림')

        image = Image.open('Resource/Image/tempCharImage.png')
        image = image.resize((200, 200))
        self.testImage = ImageTk.PhotoImage(image)

        self.notebook = tkinter.ttk.Notebook(self.window, width=600, height=800)
        self.notebook.pack()

        # 캐릭터 정보 검색 페이지
        #
        #
        frame1 = Frame(self.window)  # 캐릭터 정보 검색 기능
        self.notebook.add(frame1, text='캐릭터 정보')
        # Label(frame1, text='캐릭터 정보를 조회', fg='red', font='helvetica 48').pack()
        frame1_1 = Frame(frame1, width=600, height=100, bg='gold')
        frame1_1.pack()
        self.searchStr = StringVar()
        Entry(frame1_1, textvariable=self.searchStr, width=20, justify=LEFT, font=self.font).place(x=50, y=50)
        Button(frame1_1, text='돋보기', width=5, height=1, command=self.pressedSearch, font=self.fontB).place(x=320, y=45)
        Button(frame1_1, text='별', width=3, height=1, command=self.pressedFavorite, font=self.fontB).place(x=450, y=45)
        Button(frame1_1, text='메일', width=3, height=1, command=self.pressedMail, font=self.fontB).place(x=510, y=45)

        frame1_2 = Frame(frame1, width=600, height=700, bg='gold')
        frame1_2.pack()

        # 종합정보
        Frame(frame1_2, width=600, height=30, bg='LightBlue1').pack()
        frame1_2_1 = Frame(frame1_2, width=600, height=200, bg='gray50')
        frame1_2_1.pack()
        # 이미지 액자
        frame1_2_1_1 = Frame(frame1_2_1, width=160, height=200, bg='#ede0c8')
        frame1_2_1_1.place(x=50, y=0)
        frame1_2_1_1_1 = Frame(frame1_2_1_1, width=140, height=180)
        frame1_2_1_1_1.pack_propagate(False)
        frame1_2_1_1_1.pack(padx=10, pady=10)
        self.charImageLabel = Label(frame1_2_1_1_1, text='이미지', image=self.testImage, width=140, height=180, padx=10, pady=10)
        self.charImageLabel.image = self.testImage
        self.charImageLabel.pack(expand=True)
        # 정보
        frame1_2_1_2 = Frame(frame1_2_1, width=290, height=200, bg='purple1')
        frame1_2_1_2.place(x=270, y=0)
        name = '김땡땡'    # 테스트용
        self.charNameLabel = Label(frame1_2_1_2, text=name, font=self.font)
        self.charNameLabel.place(x=10, y=10)
        level = 250     # 토스트용
        self.charLevelLabel = Label(frame1_2_1_2, text='Lv '+str(level), font=self.font)
        self.charLevelLabel.place(x=100, y=10)
        server = '스카니아'     # 텨스트용
        self.charServerLabel = Label(frame1_2_1_2, text='서버 - '+server, font=self.font)
        self.charServerLabel.place(x=10, y=50)
        guild = '지존'    # 임시
        self.charGuildLabel = Label(frame1_2_1_2, text='길드 - '+guild, font=self.font)
        self.charGuildLabel.place(x=10, y=90)
        popular = 999   # 비둘기
        self.charPopularLabel = Label(frame1_2_1_2, text='인기도 - '+str(popular), font=self.font)
        self.charPopularLabel.place(x=10, y=130)

        Frame(frame1_2, width=600, height=30, bg='LightBlue1').pack()
        frame1_2_2 = Frame(frame1_2, width=600, height=300, bg='gray50')
        frame1_2_2.pack()
        # 능력치
        frame1_2_2_1 = Frame(frame1_2_2, width=240, height=300, bg='khaki1')
        frame1_2_2_1.pack_propagate(False)
        frame1_2_2_1.place(x=40, y=0)
        frame1_2_2_1_1 = Frame(frame1_2_2_1, width=200, height=40, bg='sky blue')
        frame1_2_2_1_1.pack_propagate(False)
        frame1_2_2_1_1.pack()
        self.statusLabel = Label(frame1_2_2_1_1, text='능력치', font=self.fontT)
        self.statusLabel.pack(side=BOTTOM)
        frame1_2_2_1_2 = Frame(frame1_2_2_1, width=140, height=260, bg='thistle', padx=10, pady=10)
        frame1_2_2_1_2.pack_propagate(False)
        frame1_2_2_1_2.pack(padx=5, pady=5)
        self.HPLabel = Label(frame1_2_2_1_2, text='HP: '+str(50000), font=self.font)
        self.HPLabel.pack(side=TOP, anchor=W, expand=Y)
        self.MPLabel = Label(frame1_2_2_1_2, text='MP: '+str(10000), font=self.font)
        self.MPLabel.pack(side=TOP, anchor=W, expand=Y)
        self.STRLabel = Label(frame1_2_2_1_2, text='STR: '+str(1000), font=self.font)
        self.STRLabel.pack(side=TOP, anchor=W, expand=Y)
        self.DEXLabel = Label(frame1_2_2_1_2, text='DEX: '+str(500), font=self.font)
        self.DEXLabel.pack(side=TOP, anchor=W, expand=Y)
        self.INTLabel = Label(frame1_2_2_1_2, text='INT: '+str(100), font=self.font)
        self.INTLabel.pack(side=TOP, anchor=W, expand=Y)
        self.LUKLabel = Label(frame1_2_2_1_2, text='LUK: '+str(150), font=self.font)
        self.LUKLabel.pack(side=TOP, anchor=W, expand=Y)
        # 장비
        frame1_2_2_2 = Frame(frame1_2_2, width=240, height=300, bg='burlywood1')
        frame1_2_2_2.pack_propagate(False)
        frame1_2_2_2.place(x=320, y=0)
        frame1_2_2_2_1 = Frame(frame1_2_2_2, width=200, height=40, bg='sky blue')
        frame1_2_2_2_1.pack_propagate(False)
        frame1_2_2_2_1.pack()
        self.equipmnLabel = Label(frame1_2_2_2_1, text='장비', font=self.fontT)
        self.equipmnLabel.pack(side=BOTTOM)
        frame1_2_2_2_2 = Frame(frame1_2_2_2, width=240, height=260, bg='thistle', padx=10, pady=10)
        frame1_2_2_2_2.pack_propagate(False)
        frame1_2_2_2_2.pack(padx=5, pady=5)

        Frame(frame1_2, width=600, height=30, bg='LightBlue1').pack()
        frame1_2_3 = Frame(frame1_2, width=600, height=80, bg='gray50')
        frame1_2_3.pack_propagate(False)
        frame1_2_3.pack()
        self.mureungLabel = Label(frame1_2_3, text='무릉 '+str(49)+'층 '+str(12)+':'+str(59), font=self.fontV)
        self.mureungLabel.pack(side=TOP)

        # 랭킹 페이지
        #
        #
        frame2 = Frame(self.window)  # 랭킹 기능
        self.notebook.add(frame2, text='랭킹 정보')
        frame2_1 = Frame(frame2, width=600, height=100, bg='gray50')
        frame2_1.pack_propagate(False)
        frame2_1.pack()
        w = 4   # 버튼 넓이
        h = 1   # 버튼 높이
        px = 5  # 버튼 패딩 양옆에 - 버튼 사이 간격 확보
        py = 5  # 버튼 패딩 위아래 - 버튼 사이 간격 확보
        # 서버들 버튼 (추후에 버튼 크기 맞추어야 함)
        Button(frame2_1, text='전체', width=w, height=h, command=self.pressedServer, font=self.font).grid(row=0, column=0, padx=px, pady=py)
        Button(frame2_1, text='스카니아', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=0, column=1, padx=px, pady=py)
        Button(frame2_1, text='베라', width=w, height=h, command=self.pressedServer, font=self.font).grid(row=0, column=2, padx=px, pady=py)
        Button(frame2_1, text='루나', width=w, height=h, command=self.pressedServer, font=self.font).grid(row=0, column=3, padx=px, pady=py)
        Button(frame2_1, text='제니스', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=0, column=4, padx=px, pady=py)
        Button(frame2_1, text='크로아', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=0, column=5, padx=px, pady=py)
        Button(frame2_1, text='유니온', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=0, column=6, padx=px, pady=py)
        Button(frame2_1, text='엘리시움', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=0, column=7, padx=px, pady=py)
        Button(frame2_1, text='이노시스', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=0, padx=px, pady=py)
        Button(frame2_1, text='레드', width=w, height=h, command=self.pressedServer, font=self.font).grid(row=1, column=1, padx=px, pady=py)
        Button(frame2_1, text='오로라', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=2, padx=px, pady=py)
        Button(frame2_1, text='아케인', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=3, padx=px, pady=py)
        Button(frame2_1, text='노바', width=w, height=h, command=self.pressedServer, font=self.font).grid(row=1, column=4, padx=px, pady=py)
        Button(frame2_1, text='리부트', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=5, padx=px, pady=py)
        Button(frame2_1, text='리부트1', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=6, padx=px, pady=py)
        Button(frame2_1, text='리부트2', width=w, height=h, command=self.pressedServer, font=self.fontS).grid(row=1, column=7, padx=px, pady=py)

        # 확률 정보 페이지
        #
        #
        frame3 = Frame(self.window)  # 확률 정보 기능
        self.notebook.add(frame3, text='확률 정보')
        Label(frame3, text='인게임 확률 통계를 보여줌', fg='green', font='helvetica 48').pack()

        # 팝업스토어 위치 및 이미지
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

    def pressedServer(self):
        pass


MainGUI()
