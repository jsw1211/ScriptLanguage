import io
import random
from tkinter import *
from tkinter import font
import tkinter.messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from enum import Enum
import requests
import urllib.request
from datetime import datetime, timedelta
from tkintermapview import TkinterMapView
import threading
from mailGUI import mailGUI
from favoriteGUI import favoriteGUI, items
from guideText import PlaceholderEntry
import chatbotRun


class MainGUI:
    headers = { # 송승호 개발용 키
        "x-nxopen-api-key": "test_cebf915b37b6eae59393a51b5d2a56e2798071e29e9cae7e85d9e988c8e293b61d98edcf6f5e475acb4e50f454c8019e"
    }

    def __init__(self):
        self.window = Tk()
        self.window.title('메핑크빈')
        self.window.geometry('600x800')

        self.font = font.Font(self.window, size=16, weight='bold', family='메이플스토리')
        self.fontS = font.Font(self.window, size=8, weight='bold', family='메이플스토리')
        self.fontB = font.Font(self.window, size=16, weight='bold', family='메이플스토리')
        self.fontT = font.Font(self.window, size=24, weight='bold', family='메이플스토리')
        self.fontV = font.Font(self.window, size=28, weight='bold', family='메이플스토리')
        self.fontN = font.Font(self.window, size=12, weight='bold', family='메이플스토리')

        image = Image.open('Resource/Image/tempCharImage.png')
        image = image.resize((200, 200))
        self.testImage = ImageTk.PhotoImage(image)

        # 모자
        image_hat = Image.open('Resource/Image/testHat.png')
        image_hat = image_hat.resize((50, 50))
        self.testImage_hat = ImageTk.PhotoImage(image_hat)
        # 상의
        image_top = Image.open('Resource/Image/testTop.png')
        image_top = image_top.resize((50, 50))
        self.testImage_top = ImageTk.PhotoImage(image_top)
        # 하의
        image_bot = Image.open('Resource/Image/testBot.png')
        image_bot = image_bot.resize((50, 50))
        self.testImage_bot = ImageTk.PhotoImage(image_bot)
        # 신발
        image_shoe = Image.open('Resource/Image/testShoe.png')
        image_shoe = image_shoe.resize((50, 50))
        self.testImage_shoe = ImageTk.PhotoImage(image_shoe)
        # 무기
        image_weapon = Image.open('Resource/Image/testWeapon.png')
        image_weapon = image_weapon.resize((50, 50))
        self.testImage_weapon = ImageTk.PhotoImage(image_weapon)
        # 보조
        image_bojo = Image.open('Resource/Image/testBojo.png')
        image_bojo = image_bojo.resize((50, 50))
        self.testImage_bojo = ImageTk.PhotoImage(image_bojo)
        # 방토
        image_cloak = Image.open('Resource/Image/testCloak.png')
        image_cloak = image_cloak.resize((50, 50))
        self.testImage_cloak = ImageTk.PhotoImage(image_cloak)
        # 장갑
        image_glove = Image.open('Resource/Image/testGlove.png')
        image_glove = image_glove.resize((50, 50))
        self.testImage_glove = ImageTk.PhotoImage(image_glove)

        self.notebook = ttk.Notebook(self.window, width=600, height=800)
        self.notebook.pack()
        self.notebook.bind("<<NotebookTabChanged>>", self.onTabChange)

        # 캐릭터 정보 검색 페이지
        #
        #
        f1color = 'thistle1'
        frame1 = Frame(self.window, background=f1color)  # 캐릭터 정보 검색 기능
        self.notebook.add(frame1, text='캐릭터 정보')
        # Label(frame1, text='캐릭터 정보를 조회', fg='red', font='helvetica 48').pack()
        frame1_1 = Frame(frame1, width=600, height=100, background=f1color)
        frame1_1.pack()
        self.searchStr = StringVar()
        self.charEntry = PlaceholderEntry(frame1_1, textvariable=self.searchStr, placeholder="캐릭터 닉네임을 입력하시오", justify=LEFT, font=self.font)
        self.charEntry.place(x=50, y=50)
        # 검색 버튼
        image = Image.open('Resource/Image/icon/search.png')
        image = image.resize((35, 35))
        image = ImageTk.PhotoImage(image)
        searchButton = Button(frame1_1, text='', image=image, command=self.pressedSearch, font=self.fontB, background='white')
        searchButton.place(x=340, y=45, width=80, height=40)
        searchButton.image = image
        # 즐겨찾기 버튼
        image = Image.open('Resource/Image/icon/star.png')
        image = image.resize((40, 40))
        image = ImageTk.PhotoImage(image)
        favoriteButton = Button(frame1_1, text='', image=image, command=self.pressedFavorite, font=self.fontB, background='white')
        favoriteButton.place(x=450, y=45, width=40, height=40)
        favoriteButton.image = image
        # 메일 버튼
        image = Image.open('Resource/Image/icon/mail.png')
        image = image.resize((40, 40))
        image = ImageTk.PhotoImage(image)
        mailButton = Button(frame1_1, text='', image=image, command=self.pressedMail, font=self.fontB, background='white')
        mailButton.place(x=510, y=45, width=40, height=40)
        mailButton.image = image

        frame1_2 = Frame(frame1, width=600, height=700, background=f1color)
        frame1_2.pack()

        self.charData = None
        self.charData_pop = None
        self.charData_stat = None
        self.charData_mureung = None
        self.charData_equip = None

        # 종합정보
        Frame(frame1_2, width=600, height=30, background=f1color).pack()
        frame1_2_1 = Frame(frame1_2, width=600, height=200, background=f1color)
        frame1_2_1.pack()
        # 이미지 액자
        phoColor = 'light blue'
        frame1_2_1_1 = Frame(frame1_2_1, width=160, height=200, background=phoColor)
        frame1_2_1_1.place(x=50, y=0)
        frame1_2_1_1_1 = Frame(frame1_2_1_1, width=140, height=180)
        frame1_2_1_1_1.pack_propagate(False)
        frame1_2_1_1_1.pack(padx=10, pady=10)
        self.charImageLabel = Label(frame1_2_1_1_1, text='이미지', image=self.testImage, width=140, height=180, padx=10, pady=10)
        self.charImageLabel.image = self.testImage
        self.charImageLabel.pack(expand=True)


        # 정보
        synColor = 'light cyan'
        labColor = 'azure'
        frame1_2_1_2 = Frame(frame1_2_1, width=290, height=200, background=synColor)
        frame1_2_1_2.place(x=270, y=0)
        image = Image.open('Resource/Image/icon/star2.png')
        image = image.resize((40, 40))
        image = ImageTk.PhotoImage(image)
        starButton = Button(frame1_2_1_2, text='', image=image, command=self.pressedStar, font=self.fontB, background='white')
        starButton.place(x=230, y=20, width=40, height=40)
        starButton.image = image
        name = '김땡땡'    # 테스트용
        self.charNameLabel = Label(frame1_2_1_2, text=name, font=self.fontT, background=labColor, borderwidth=2, relief='groove')
        self.charNameLabel.place(x=10, y=20)
        level = 250     # 토스트용
        self.charLevelLabel = Label(frame1_2_1_2, text='Lv '+str(level), font=self.font, background=labColor, borderwidth=2, relief='groove')
        self.charLevelLabel.place(x=10, y=86)
        server = '스카니아'     # 텨스트용
        self.charServerLabel = Label(frame1_2_1_2, text='서버 - '+server, font=self.font, background=labColor, borderwidth=2, relief='groove')
        self.charServerLabel.place(x=140, y=86)
        guild = '지존'    # 임시
        self.charGuildLabel = Label(frame1_2_1_2, text='길드 - '+guild, font=self.font, background=labColor, borderwidth=2, relief='groove')
        self.charGuildLabel.place(x=140, y=124)
        c_class = '모험가' # 떠나요~ 둘이서~
        self.charClassLabel = Label(frame1_2_1_2, text='직업 - ' + str(c_class), font=self.font, background=labColor, borderwidth=2, relief='groove')
        self.charClassLabel.place(x=10, y=124)
        popular = 999   # 비둘기
        self.charPopularLabel = Label(frame1_2_1_2, text='인기도 - '+str(popular), font=self.font, background=labColor, borderwidth=2, relief='groove')
        self.charPopularLabel.place(x=10, y=162)

        Frame(frame1_2, width=600, height=30, background=f1color).pack()
        frame1_2_2 = Frame(frame1_2, width=600, height=300, background=f1color)
        frame1_2_2.pack()
        # 능력치
        staColor = 'pale green'
        frame1_2_2_1 = Frame(frame1_2_2, width=240, height=300, background=staColor)
        frame1_2_2_1.pack_propagate(False)
        frame1_2_2_1.place(x=40, y=0)
        frame1_2_2_1_1 = Frame(frame1_2_2_1, width=200, height=40, background=staColor)
        frame1_2_2_1_1.pack_propagate(False)
        frame1_2_2_1_1.pack()
        self.statusLabel = Label(frame1_2_2_1_1, text='능력치', font=self.fontT, background=staColor)
        self.statusLabel.pack(side=BOTTOM)
        frame1_2_2_1_2 = Frame(frame1_2_2_1, width=140, height=260, padx=10, pady=10, background=staColor)
        frame1_2_2_1_2.pack_propagate(False)
        frame1_2_2_1_2.pack(padx=5, pady=5)
        self.HPLabel = Label(frame1_2_2_1_2, text='HP: '+str(50000), font=self.font, borderwidth=2, relief='groove')
        self.HPLabel.pack(side=TOP, anchor=W, expand=Y)
        self.MPLabel = Label(frame1_2_2_1_2, text='MP: '+str(10000), font=self.font, borderwidth=2, relief='groove')
        self.MPLabel.pack(side=TOP, anchor=W, expand=Y)
        self.STRLabel = Label(frame1_2_2_1_2, text='STR: '+str(1000), font=self.font, borderwidth=2, relief='groove')
        self.STRLabel.pack(side=TOP, anchor=W, expand=Y)
        self.DEXLabel = Label(frame1_2_2_1_2, text='DEX: '+str(500), font=self.font, borderwidth=2, relief='groove')
        self.DEXLabel.pack(side=TOP, anchor=W, expand=Y)
        self.INTLabel = Label(frame1_2_2_1_2, text='INT: '+str(100), font=self.font, borderwidth=2, relief='groove')
        self.INTLabel.pack(side=TOP, anchor=W, expand=Y)
        self.LUKLabel = Label(frame1_2_2_1_2, text='LUK: '+str(150), font=self.font, borderwidth=2, relief='groove')
        self.LUKLabel.pack(side=TOP, anchor=W, expand=Y)
        # 장비
        equColor = 'peach puff'
        frame1_2_2_2 = Frame(frame1_2_2, width=240, height=300, background=equColor)
        frame1_2_2_2.pack_propagate(False)
        frame1_2_2_2.place(x=320, y=0)
        frame1_2_2_2_1 = Frame(frame1_2_2_2, width=200, height=40, background=equColor)
        frame1_2_2_2_1.pack_propagate(False)
        frame1_2_2_2_1.pack()
        self.equipmnLabel = Label(frame1_2_2_2_1, text='장비', font=self.fontT, background=equColor)
        self.equipmnLabel.pack(side=BOTTOM)
        frame1_2_2_2_2 = Frame(frame1_2_2_2, width=240, height=260, padx=10, pady=10, background=equColor)
        frame1_2_2_2_2.pack_propagate(False)
        frame1_2_2_2_2.pack(padx=5, pady=5)
        # 모자
        self.equipLabel_1 = Button(frame1_2_2_2_2, text='모자이미지', image=self.testImage_hat, command=lambda: self.pressedEquip(EquipMod.hat), width=50, height=50)
        self.equipLabel_1.image = self.testImage_hat
        self.equipLabel_1.place(x=80, y=-5)
        # 상의
        self.equipLabel_2 = Button(frame1_2_2_2_2, text='상의이미지', image=self.testImage_top, command=lambda: self.pressedEquip(EquipMod.top), width=50, height=50)
        self.equipLabel_2.image = self.testImage_top
        self.equipLabel_2.place(x=80, y=60)
        # 하의
        self.equipLabel_3 = Button(frame1_2_2_2_2, text='하의이미지', image=self.testImage_bot, command=lambda: self.pressedEquip(EquipMod.bot), width=50, height=50)
        self.equipLabel_3.image = self.testImage_bot
        self.equipLabel_3.place(x=80, y=125)
        # 신발
        self.equipLabel_4 = Button(frame1_2_2_2_2, text= '신발이미지', image=self.testImage_shoe, command=lambda: self.pressedEquip(EquipMod.shoe), width=50, height=50)
        self.equipLabel_4.image = self.testImage_shoe
        self.equipLabel_4.place(x=80, y=190)
        # 무기
        self.equipLabel_5 = Button(frame1_2_2_2_2, text='무기이미지', image=self.testImage_weapon, command=lambda: self.pressedEquip(EquipMod.weapon), width=50, height=50)
        self.equipLabel_5.image = self.testImage_weapon
        self.equipLabel_5.place(x=15, y=60)
        # 보조
        self.equipLabel_6 = Button(frame1_2_2_2_2, text='보조이미지', image=self.testImage_bojo, command=lambda: self.pressedEquip(EquipMod.bojo), width=50, height=50)
        self.equipLabel_6.image = self.testImage_bojo
        self.equipLabel_6.place(x=15, y=125)
        # 망토
        self.equipLabel_7 = Button(frame1_2_2_2_2, text='망토이미지', image=self.testImage_cloak, command=lambda: self.pressedEquip(EquipMod.cloak), width=50, height=50)
        self.equipLabel_7.image = self.testImage_cloak
        self.equipLabel_7.place(x=145, y=60)
        # 장갑
        self.equipLabel_8 = Button(frame1_2_2_2_2, text='장갑이미지', image=self.testImage_glove, command=lambda: self.pressedEquip(EquipMod.glove), width=50, height=50)
        self.equipLabel_8.image = self.testImage_glove
        self.equipLabel_8.place(x=145, y=125)

        #무릉
        murColor = 'light goldenrod'
        Frame(frame1_2, width=600, height=30, background=f1color).pack()
        frame1_2_3 = Frame(frame1_2, width=600, height=80, background=f1color)
        frame1_2_3.pack_propagate(False)
        frame1_2_3.pack()
        self.mureungLabel = Label(frame1_2_3, text='무릉 '+str(49)+'층 '+str(12)+':'+str(59), font=self.fontV, background=murColor)
        self.mureungLabel.pack(side=TOP)

        # 랭킹 페이지
        #
        #
        f2color = 'cornsilk2'
        self.lankSeenServer = ServerMod.Entire  # default 전체서버(일반서버 전체)
        self.lankPage = 0   # default 0 0~9페이지까지(100위까지 보여줄 예정)
        frame2 = Frame(self.window, background=f2color)  # 랭킹 기능
        self.notebook.add(frame2, text='랭킹 정보')
        frame2_1 = Frame(frame2, width=600, height=100, background=f2color)
        frame2_1.grid_propagate(False)
        frame2_1.pack()
        w = 4   # 버튼 넓이
        h = 1   # 버튼 높이
        px = 60  # 버튼 넓이 픽셀
        py = 35  # 버튼 높이 픽셀
        self.lankServerButton = []
        self.lankServerButton.append(Button(frame2_1, text='전체', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Entire), font=self.font))
        self.lankServerButton.append(Button(frame2_1, text='스카니아', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Scania), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='베라', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Bera), font=self.font))
        self.lankServerButton.append(Button(frame2_1, text='루나', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Luna), font=self.font))
        self.lankServerButton.append(Button(frame2_1, text='제니스', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Zenis), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='크로아', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Croah), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='유니온', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Union), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='엘리시움', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Elisium), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='이노시스', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Enosis), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='레드', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Red), font=self.font))
        self.lankServerButton.append(Button(frame2_1, text='오로라', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Aurora), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='아케인', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Arcane), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='노바', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Nova), font=self.font))
        self.lankServerButton.append(Button(frame2_1, text='리부트', width=w, height=h, command=lambda : self.pressedServer(ServerMod.RebootAll), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='리부트1', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Reboot1), font=self.fontS))
        self.lankServerButton.append(Button(frame2_1, text='리부트2', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Reboot2), font=self.fontS))
        for i in range(len(self.lankServerButton)):
            self.lankServerButton[i].place(x=25+70*(i%8), y=10+45*(i//8), width=px, height=py)
        # 임시 랭킹들 나열
        Frame(frame2, width=600, height=30, background=f2color).pack()
        frame2_2 = Frame(frame2, width=600, height=550, background='ivory3')
        frame2_2.grid_propagate(False)
        frame2_2.pack()
        px = 24  # 버튼 패딩 양옆에 - 버튼 사이 간격 확보
        py = 4  # 버튼 패딩 위아래 - 버튼 사이 간격 확보
        Label(frame2_2, text='랭킹 #', width=5, height=2, font=self.font).place(x=20+115*0, y=10, width=100, height=60)
        Label(frame2_2, text='닉네임', width=5, height=2, font=self.font).place(x=20+115*1, y=10, width=100, height=60)
        Label(frame2_2, text='레벨', width=5, height=2, font=self.font).place(x=20+115*2, y=10, width=100, height=60)
        Label(frame2_2, text='서버', width=5, height=2, font=self.font).place(x=20+115*3, y=10, width=100, height=60)
        Label(frame2_2, text='직업', width=5, height=2, font=self.font).place(x=20+115*4, y=10, width=100, height=60)
        # 1~10 한페이지에서 보여질 10명
        px = 24  # 요소별 양옆에 패딩
        py = 10  # 랭킹 우아래 패딩
        self.lankingLabels = [[] for _ in range(10)]
        for i in range(10):
            self.lankingLabels[i].append(Label(frame2_2, text=str(i+1)+'위', width=5, height=1, font=self.font))
            self.lankingLabels[i].append(Label(frame2_2, text='김땡땡', width=5, height=1, font=self.font))
            self.lankingLabels[i].append(Label(frame2_2, text=str(295)+'Lv', width=5, height=1, font=self.font))
            self.lankingLabels[i].append(Label(frame2_2, text='스카니아', width=5, height=1, font=self.font))
            self.lankingLabels[i].append(Label(frame2_2, text='초보자', width=5, height=1, font=self.font))
            for j, label in enumerate(self.lankingLabels[i]):   # 그리드 배치
                label.place(x=20+115*j, y=80+46*i, width=100, height=40)
        # 다음 페이지 버튼(10 페이지 정도 생각중)
        Frame(frame2, width=600, height=30, background=f2color).pack()
        frame2_3 = Frame(frame2, width=600, height=60, background=f2color)
        frame2_3.pack()
        Button(frame2_3, text='<-', width=10, height=2, command=self.pressedPrev, font=self.fontB).place(x=150, y=0, width=100, height=50)
        Button(frame2_3, text='->', width=10, height=2, command=self.pressedNext, font=self.fontB).place(x=350, y=0, width=100, height=50)
        self.lankPageLabel = Label(frame2_3, text=str(self.lankPage+1), width=2, height=1, font=self.fontB, background='cornsilk3')
        self.lankPageLabel.place(x=250+10, y=0, width=80, height=50)
        self.pressedServer(ServerMod.Entire)

        # 확률 정보 페이지
        #
        #
        frame3 = Frame(self.window)  # 확률 정보 기능
        self.notebook.add(frame3, text='스타포스 확률')
        frame3_1 = Frame(frame3, width=600, height=100)
        frame3_1.pack()
        self.searchAPIKey = StringVar()
        self.apiKeyEntry = PlaceholderEntry(frame3_1, textvariable=self.searchAPIKey, placeholder='넥슨 API 키를 입력하시오', justify=LEFT, font=self.font)
        self.apiKeyEntry.place(x=50, y=50, width=400, height=25)
        Button(frame3_1, text='키 입력', width=5, height=1, command=self.pressedAPIKey, font=self.fontB, background='white').place(x=485, y=48, width=80, height=30)
        frame3_2 = Frame(frame3, width=600, height=660)
        frame3_2.pack_propagate(False)
        frame3_2.pack()
        self.percentageCanvas = Canvas(frame3_2, background="white", width=600, height=600)
        self.percentageCanvas.pack()
        self.cxs = 25   # Canvas x start 좌표
        self.cye = 500  # Canvas y end 좌표
        self.cxw = 22   # Canvas x width
        self.cys = 100
        self.percentageCanvas.create_line(0, 500, 600, 500, tags='graph')
        for i in range(25):
            self.percentageCanvas.create_text(25+22*i+11, 520, text=str(i), width=22, tags='graph')
        self.percentageCanvas.create_rectangle(50, 560, 150, 580, fill='yellow', tags='graph')
        self.percentageCanvas.create_text(220, 570, text='내 강화 확률', tags='graph', font=('Helvetica', 12, 'bold'))
        self.percentageCanvas.create_rectangle(350-30, 560, 450-30, 580, fill='dodger blue', tags='graph')
        self.percentageCanvas.create_text(520-30, 570, text='실제 강화 확률', tags='graph', font=('Helvetica', 12, 'bold'))

        # 오프라인 이벤트 위치 및 이미지
        #
        #
        f4color = 'snow2'
        frame4 = Frame(self.window, background=f4color)  # 팝업스토어 위치 지도 기능
        self.notebook.add(frame4, text='오프라인 행사')
        # Label(frame4, text='팝업스토어 위치를 지도로', fg='black', font='helvetica 48').pack()
        frame4_1 = Frame(frame4, width=600, height=80, background=f4color)
        frame4_1.pack()
        self.eventImage = []
        for imageNum in range(3):
            image = Image.open('Resource/Image/event/'+str(imageNum)+'.jpg')
            image = image.resize((320, 180))
            self.eventImage.append(ImageTk.PhotoImage(image))

        self.locateData = ['2023 겨울 쇼케이스', '팝업스토어', '2023 여름 쇼케이스', '2023 여름 CGV 영등포', '2023 여름 CGV 용산아이파크몰',
                      '2023 여름 CGV 대전', '2023 여름 CGV 서면(6관)', '2023 여름 CGV 대구아카데미', '2023 여름 CGV 광주터미널',
                      '2023 여름 CGV 왕십리', '2023 여름 CGV 신촌아트레온', '2023 여름 CGV 인천', '2023 여름 CGV 원주(폐점)',
                      '2023 여름 CGV 제주노형', '2023 여름 CGV 상봉', '2023 여름 CGV 서면(7관)', '2023 여름 CGV 천안펜타포트']
        self.addressData = ['서울 송파구 올림픽로 240', '서울 영등포구 여의대로 108', '서울 송파구 올림픽로 424', '서울 영등포구 영중로 15', '서울 용산구 한강대로23길 55',
                            '대전 중구 계백로 1700', '부산 부산진구 동천로 4', '대구 중구 중앙대로 412', '광주 서구 무진대로 904',
                            '서울 성동구 왕십리광장로 17', '서울 서대문구 신촌로 129', '인천 남동구 예술로 198', '강원특별자치도 원주시 서원대로 171',
                            '제주특별자치도 제주시 노형로 407', '서울 중랑구 상봉로 131', '부산 부산진구 동천로 4', '충남 천안시 서북구 공원로 196']
        self.scheduleData = ['2023년 12월 15일 ~ 12월 16일', '2023년 10월 5일 ~ 10월 15일', '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일',
                             '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일',
                             '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일',
                             '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일', '2023년 6월 10일']
        self.combo = ttk.Combobox(frame4_1, width=400, height=25, values=self.locateData)
        self.combo.place(x=100, y=30, width=400, height=25)
        self.combo.bind("<<ComboboxSelected>>", self.comboSelect)
        frame4_2 = Frame(frame4, width=600, height=680, background=f4color)
        frame4_2.pack()
        self.mapWidget = TkinterMapView(frame4_2, width=400, height=300, corner_radius=10)
        self.mapWidget.place(x=100, y=20, width=400, height=300)
        self.setMapView(True)
        self.mapDescLabels = []

        mapLabel = Label(frame4_2, text='한국공학대학교', font=self.fontB, anchor=CENTER)
        mapLabel.place(x=100, y=330 + 50 * 0, width=400, height=40)
        self.mapDescLabels.append(mapLabel)
        mapLabel = Label(frame4_2, text='경기 시흥시 산기대학로 237', font=self.fontB, anchor=CENTER)
        mapLabel.place(x=100, y=330 + 50 * 1, width=400, height=40)
        self.mapDescLabels.append(mapLabel)
        mapLabel = Label(frame4_2, text='1997년 12월 20일 ~', font=self.fontB, anchor=CENTER)
        mapLabel.place(x=100, y=330 + 50 * 2, width=400, height=40)
        self.mapDescLabels.append(mapLabel)
        self.mapImageLabel = Label(frame4_2, background=f4color)
        self.mapImageLabel.place(x=140, y=490, width=320, height=180)

        # 강화 시뮬레이터(검키우기)
        #
        #
        f5color = 'gray50'
        self.spentMeso = 0
        frame5 = Frame(self.window, bg='gray50', background=f5color)  # 검키우기 미니게임?
        self.notebook.add(frame5, text='강화 시뮬')
        # Label(frame5, text='검키우기', fg='purple', font='helvetica 48').pack()
        frame5_1 = Frame(frame5, width=600, height=100, background=f5color)
        frame5_1.pack()
        image = Image.open('Resource/Image/icon/mesoB.png')
        image = image.resize((40, 40))
        image = ImageTk.PhotoImage(image)
        mesoLabel = Label(frame5_1, image=image, background=f5color)
        mesoLabel.place(x=100, y=40, width=40, height=40)
        mesoLabel.image = image
        self.spentMesoLabel = Label(frame5_1, text=str(self.spentMeso), width=20, height=2, font=self.fontB, anchor='w', background=f5color)
        self.spentMesoLabel.place(x=140, y=40, width=360, height=40)
        frame5_2 = Frame(frame5, width=600, height=400, background=f5color)
        frame5_2.pack()
        self.weaponLVLabel = Label(frame5_2, width=550, height=30, font=('Helvetica', 14), fg='yellow', background=f5color)
        self.weaponLVLabel.place(x=25, y=10, width=550, height=30)
        self.SFWeaponLabel = Label(frame5_2, width=300, height=300, background=f5color)
        self.SFWeaponLabel.place(x=150, y=50, width=300, height=300)
        self.weaponLNLabel = Label(frame5_2, width=60, height=30, font=('Helvetica', 24, 'bold'), fg='black', background=f5color)
        self.weaponLNLabel.place(x=270, y=360, width=60, height=30)
        frame5_3 = Frame(frame5, width=600, height=260, background=f5color)
        frame5_3.pack()
        self.SFPercentLabel = Label(frame5_3, text='확률', width=20, height=2, font=self.fontB, background=f5color)
        self.SFPercentLabel.place(x=200, y=0, width=200, height=50)
        self.enhanceButton = Button(frame5_3, text='강화하기!', width=30, height=2, command=self.pressedEnhance, font=self.fontB, background='gray70')
        self.enhanceButton.place(x=400, y=100, width=150, height=80)
        frame5_3_1 = Frame(frame5_3, width=300, height=100, background=f5color)
        frame5_3_1.place(x=50, y=100, width=300, height=100)
        self.checkSF = IntVar()
        Checkbutton(frame5_3, text='스타포스 체크', variable=self.checkSF, command=self.pressedNothing, font=self.fontB, background=f5color).place(x=50, y=60)
        Label(frame5_3_1, text='성공확률', width=8, height=1, font=self.fontB, background=f5color).place(x=50, y=6, width=100, height=25)
        self.succesPercentLabel = Label(frame5_3_1, text='', width=8, height=1, font=self.fontB, anchor='e', background=f5color)
        self.succesPercentLabel.place(x=150, y=6, width=100, height=25)
        Label(frame5_3_1, text='실패확률', width=8, height=1, font=self.fontB, background=f5color).place(x=50, y=37, width=100, height=25)
        self.failPercentLabel = Label(frame5_3_1, text='', width=8, height=1, font=self.fontB, anchor='e', background=f5color)
        self.failPercentLabel.place(x=150, y=37, width=100, height=25)
        Label(frame5_3_1, text='파괴확률', width=8, height=1, font=self.fontB, background=f5color).place(x=50, y=68, width=100, height=25)
        self.destroyPercentLabel = Label(frame5_3_1, text='', width=8, height=1, font=self.fontB, anchor='e', background=f5color)
        self.destroyPercentLabel.place(x=150, y=68, width=100, height=25)
        self.enhanceMesoLabel = Label(frame5_3, text='필요한 메소', width=8, height=1, font=self.fontB, background=f5color)
        self.enhanceMesoLabel.place(x=100, y=220, width=400, height=40)

        # 검 키우기를 위한 정보들(멤버변수들)
        self.weaponsImage = []  # 이미지들 저장할 리스트
        for weaponNum in range(25+1):
            image = Image.open('Resource/Image/weapons/'+str(weaponNum)+'.png')
            image = image.resize((280, 280))
            self.weaponsImage.append(ImageTk.PhotoImage(image))
        self.weaponLevel = 0
        self.upgradeWeapon()
        self.miniGameResult = None

        self.window.bind('<Return>', self.bind_enter_key)

        chatbot_thread = threading.Thread(target=self.start_chatbot)
        chatbot_thread.daemon = True
        chatbot_thread.start()
        # Tkinter 나타나게
        self.window.mainloop()

    def pressedSearch(self):
        characterName = self.searchStr.get()  # 입력된 텍스트 가져오기
        if characterName == '캐릭터 닉네임을 입력하시오':
            return
        encCharName = urllib.parse.quote(characterName)
        urlString_1 = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + encCharName
        response_1 = requests.get(urlString_1, headers=self.headers)
        if encCharName:
            urlString_2 = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + response_1.json()['ocid']
            response_2 = requests.get(urlString_2, headers=self.headers)
            urlString_3 = "https://open.api.nexon.com/maplestory/v1/character/popularity?ocid=" + response_1.json()['ocid']
            response_3 = requests.get(urlString_3, headers=self.headers)
            urlString_4 = "https://open.api.nexon.com/maplestory/v1/character/stat?ocid=" + response_1.json()['ocid']
            response_4 = requests.get(urlString_4, headers=self.headers)
            urlString_5 = "https://open.api.nexon.com/maplestory/v1/character/dojang?ocid=" + response_1.json()['ocid']
            response_5 = requests.get(urlString_5, headers=self.headers)
            urlString_6 = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + response_1.json()['ocid']
            response_6 = requests.get(urlString_6, headers=self.headers)
            if response_2.status_code == 200 and response_3.status_code == 200 and response_4.status_code == 200 and response_5.status_code == 200 and response_6.status_code == 200:
                self.charData = response_2.json()
                self.charData_pop = response_3.json()
                self.charData_stat = response_4.json()
                self.charData_mureung = response_5.json()
                self.charData_equip = response_6.json()
                self.updateCharacterInfo(self.charData, self.charData_pop, self.charData_stat, self.charData_mureung, self.charData_equip)
            else:
                print('캐릭터 정보를 가져오는 데 실패했습니다.')
        else:
            print('캐릭터 이름을 입력하세요.')

    def updateCharacterInfo(self, charData, charData_pop, charData_stat, charData_mureung, charData_equip):
        # 캐릭터 정보를 업데이트하는 함수
        self.charNameLabel['text'] = str(charData.get('character_name'))
        self.charLevelLabel['text'] = 'Lv ' + str(charData.get('character_level'))
        self.charServerLabel['text'] = '서버 - ' + str(charData.get('world_name'))
        self.charGuildLabel['text'] = '길드 - ' + str((charData.get('character_guild_name')))
        self.charPopularLabel['text'] = '인기도 - ' + str(charData_pop.get('popularity'))
        self.charClassLabel['text'] = str(charData.get('character_class'))

        # 능력치 업데이트
        for stat in charData_stat['final_stat']:
            if stat['stat_name'] == 'HP':
                self.HPLabel['text'] = 'HP: ' + stat['stat_value']
            elif stat['stat_name'] == 'MP':
                self.MPLabel['text'] = 'MP: ' + stat['stat_value']
            elif stat['stat_name'] == 'STR':
                self.STRLabel['text'] = 'STR: ' + stat['stat_value']
            elif stat['stat_name'] == 'DEX':
                self.DEXLabel['text'] = 'DEX: ' + stat['stat_value']
            elif stat['stat_name'] == 'INT':
                self.INTLabel['text'] = 'INT: ' + stat['stat_value']
            elif stat['stat_name'] == 'LUK':
                self.LUKLabel['text'] = 'LUK: ' + stat['stat_value']

        # 캐릭터 이미지 업데이트
        image_url = charData.get('character_image')
        image_data = urllib.request.urlopen(image_url).read()
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((200, 200))
        self.testImage = ImageTk.PhotoImage(image)
        self.charImageLabel.configure(image=self.testImage)
        self.charImageLabel.image = self.testImage

        #무릉 업데이트
        mureung_min = int(charData_mureung.get('dojang_best_time')) // 60
        mureung_sec = int(charData_mureung.get('dojang_best_time')) % 60
        self.mureungLabel['text'] = '무릉 ' + str(charData_mureung.get('dojang_best_floor')) + '층 ' + str(mureung_min) + ':' + str(mureung_sec)

        #장비 업데이트
        for equip in charData_equip['item_equipment_preset_1']:
            if equip['item_equipment_slot'] == '모자':
                hat_url = equip.get('item_icon')
                hat_data = urllib.request.urlopen(hat_url).read()
                image_hat = Image.open(io.BytesIO(hat_data))
                image_hat = image_hat.resize((50, 50))
                self.testImage_hat = ImageTk.PhotoImage(image_hat)
                self.equipLabel_1.configure(image=self.testImage_hat)
                self.equipLabel_1.image = self.testImage_hat
            elif equip['item_equipment_slot'] == '상의':
                top_url = equip.get('item_icon')
                top_data = urllib.request.urlopen(top_url).read()
                image_top = Image.open(io.BytesIO(top_data))
                image_top = image_top.resize((50, 50))
                self.testImage_top = ImageTk.PhotoImage(image_top)
                self.equipLabel_2.configure(image=self.testImage_top)
                self.equipLabel_2.image = self.testImage_top
            elif equip['item_equipment_slot'] == '하의':
                bot_url = equip.get('item_icon')
                bot_data = urllib.request.urlopen(bot_url).read()
                image_bot = Image.open(io.BytesIO(bot_data))
                image_bot = image_bot.resize((50, 50))
                self.testImage_bot = ImageTk.PhotoImage(image_bot)
                self.equipLabel_3.configure(image=self.testImage_bot)
                self.equipLabel_3.image = self.testImage_bot
            elif equip['item_equipment_slot'] == '신발':
                shoe_url = equip.get('item_icon')
                shoe_data = urllib.request.urlopen(shoe_url).read()
                image_shoe = Image.open(io.BytesIO(shoe_data))
                image_shoe = image_shoe.resize((50, 50))
                self.testImage_shoe = ImageTk.PhotoImage(image_shoe)
                self.equipLabel_4.configure(image=self.testImage_shoe)
                self.equipLabel_4.image = self.testImage_shoe
            elif equip['item_equipment_slot'] == '무기':
                weapon_url = equip.get('item_icon')
                weapon_data = urllib.request.urlopen(weapon_url).read()
                image_weapon = Image.open(io.BytesIO(weapon_data))
                image_weapon = image_weapon.resize((50, 50))
                self.testImage_weapon = ImageTk.PhotoImage(image_weapon)
                self.equipLabel_5.configure(image=self.testImage_weapon)
                self.equipLabel_5.image = self.testImage_weapon
            elif equip['item_equipment_slot'] == '보조무기':
                bojo_url = equip.get('item_icon')
                bojo_data = urllib.request.urlopen(bojo_url).read()
                image_bojo = Image.open(io.BytesIO(bojo_data))
                image_bojo = image_bojo.resize((50, 50))
                self.testImage_bojo = ImageTk.PhotoImage(image_bojo)
                self.equipLabel_6.configure(image=self.testImage_bojo)
                self.equipLabel_6.image = self.testImage_bojo
            elif equip['item_equipment_slot'] == '망토':
                cloak_url = equip.get('item_icon')
                cloak_data = urllib.request.urlopen(cloak_url).read()
                image_cloak = Image.open(io.BytesIO(cloak_data))
                image_cloak = image_cloak.resize((50, 50))
                self.testImage_cloak = ImageTk.PhotoImage(image_cloak)
                self.equipLabel_7.configure(image=self.testImage_cloak)
                self.equipLabel_7.image = self.testImage_cloak
            elif equip['item_equipment_slot'] == '장갑':
                glove_url = equip.get('item_icon')
                glove_data = urllib.request.urlopen(glove_url).read()
                image_glove = Image.open(io.BytesIO(glove_data))
                image_glove = image_glove.resize((50, 50))
                self.testImage_glove = ImageTk.PhotoImage(image_glove)
                self.equipLabel_8.configure(image=self.testImage_glove)
                self.equipLabel_8.image = self.testImage_glove

    def pressedEquip(self, equip):
        if self.charData is None:
            tkinter.messagebox.showinfo('오류', '캐릭터 정보를 조회하지 않았습니다.')
            return

        self.equip_window = Tk()
        self.equip_window.title('장비 능력치')
        self.equip_window.geometry('300x800')
        self.potential_Label = Label(self.equip_window, text="잠재능력 등급: 레어")
        self.potential_Label.pack(pady=5)
        self.potentialoption1_Label = Label(self.equip_window, text="DEX:+9%")
        self.potentialoption1_Label.pack(pady=5)
        self.potentialoption2_Label = Label(self.equip_window, text="DEX:+9%")
        self.potentialoption2_Label.pack(pady=5)
        self.potentialoption3_Label = Label(self.equip_window, text="DEX:+9%")
        self.potentialoption3_Label.pack(pady=5)
        self.additional_Label = Label(self.equip_window, text="에디셔널 잠재능력 등급: 레전드리")
        self.additional_Label.pack(pady=5)
        self.additionaloption1_Label = Label(self.equip_window, text="마:+10")
        self.additionaloption1_Label.pack(pady=5)
        self.additionaloption2_Label = Label(self.equip_window, text="마:+10")
        self.additionaloption2_Label.pack(pady=5)
        self.additionaloption3_Label = Label(self.equip_window, text="점프력:+2")
        self.additionaloption3_Label.pack(pady=5)
        if equip in EquipMod:
            self.updateEquipStat(equip)

    def updateEquipStat(self, equipName):
        for option in self.charData_equip['item_equipment']:
            if option['item_equipment_slot'] == str(equipName.value):
                self.potential_Label['text'] = '잠재능력 등급: ' + str(option['potential_option_grade'])
                self.potentialoption1_Label['text'] = str(option['potential_option_1'])
                self.potentialoption2_Label['text'] = str(option['potential_option_2'])
                if option['potential_option_3'] == None:
                    self.potentialoption3_Label['text'] = ''
                else:
                    self.potentialoption3_Label['text'] = str(option['potential_option_3'])
                self.additional_Label['text'] = '에디셔널 잠재능력 등급: ' + str(option['additional_potential_option_grade'])
                self.additionaloption1_Label['text'] = str(option['additional_potential_option_1'])
                self.additionaloption2_Label['text'] = str(option['additional_potential_option_2'])
                if option['additional_potential_option_3'] == None:
                    self.additionaloption3_Label['text'] = ''
                else:
                    self.additionaloption3_Label['text'] = str(option['additional_potential_option_3'])

    def pressedFavorite(self):
        if favoriteGUI.instance is None or not favoriteGUI.instance.window.winfo_exists():
            favoriteGUI(self)
        else:
            favoriteGUI.instance.window.lift()

    def pressedMail(self):
        if mailGUI.instance is None or not mailGUI.instance.window.winfo_exists():
            mailGUI(self)
        else:
            mailGUI.instance.window.lift()

    def pressedStar(self):
        if self.charData == None:
            return
        name = str(self.charData.get('character_name'))
        if name not in items:
            items.append(name)
            if favoriteGUI.instance is not None:
                favoriteGUI.instance.appendItem(name)

    def pressedServer(self, server):
        self.lankServerButton[self.lankSeenServer.value]['state'] = 'active'
        self.lankServerButton[self.lankSeenServer.value]['bg'] = 'SystemButtonFace'
        if server == ServerMod.Entire or server == ServerMod.RebootAll:
            self.lankSeenServer = server
            if server == ServerMod.Entire:
                self.changeLankServerAll(0) # 0이 일반 서버
            else:
                self.changeLankServerAll(1) # 1이 리부트 서버이기 때문에
        elif server in ServerMod:
            serverNameKorea = ''
            self.lankSeenServer = server
            if server == ServerMod.Scania:
                serverNameKorea = '스카니아'
            elif server == ServerMod.Bera:
                serverNameKorea = '베라'
            elif server == ServerMod.Luna:
                serverNameKorea = '루나'
            elif server == ServerMod.Zenis:
                serverNameKorea = '제니스'
            elif server == ServerMod.Croah:
                serverNameKorea = '크로아'
            elif server == ServerMod.Union:
                serverNameKorea = '유니온'
            elif server == ServerMod.Elisium:
                serverNameKorea = '엘리시움'
            elif server == ServerMod.Enosis:
                serverNameKorea = '이노시스'
            elif server == ServerMod.Red:
                serverNameKorea = '레드'
            elif server == ServerMod.Aurora:
                serverNameKorea = '오로라'
            elif server == ServerMod.Arcane:
                serverNameKorea = '아케인'
            elif server == ServerMod.Nova:
                serverNameKorea = '노바'
            elif server == ServerMod.Reboot1:
                serverNameKorea = '리부트'
            elif server == ServerMod.Reboot2:
                serverNameKorea = '리부트2'
            self.changeLankServer(serverNameKorea)
        else:
            pass    # 유효한 서버가 아닙니다.
        self.lankServerButton[self.lankSeenServer.value]['state'] = 'disabled'
        self.lankServerButton[self.lankSeenServer.value]['bg'] = 'gray70'

    def pressedPrev(self):
        # 랭킹 페이지 <- 버튼에 대해서
        if self.lankPage > 0:
            self.lankPage -= 1
        self.UpdateLankingLabel()

    def pressedNext(self):
        # 랭킹 페이지 -> 버튼에 대해서
        if self.lankPage < 9:
            self.lankPage += 1
        self.UpdateLankingLabel()

    def pressedAPIKey(self):
        urlString = 'https://open.api.nexon.com/maplestory/v1/ouid'
        apiKey = self.searchAPIKey.get()
        if apiKey == '넥슨 API 키를 입력하시오':
            return
        apiKey = apiKey.strip()
        self.nowAPIKey = {"x-nxopen-api-key": apiKey}
        response = requests.get(urlString, headers=self.nowAPIKey)
        if response.status_code == 200:
            pass
        else:
            print('올바른 API 키가 아닙니다')
            return

        startTime = datetime(2023, 12, 28)
        nowTime = datetime.today()
        urlString = 'https://open.api.nexon.com/maplestory/v1/history/starforce?count=1000&date='
        self.userEnhanceData = {'count': 0, 'starforce_history': []}
        print('start crolling')
        while startTime < nowTime:
            nowUrlString = urlString + str(startTime.date())
            response = requests.get(nowUrlString, headers=self.nowAPIKey)
            if response.status_code == 200:
                data = response.json()
                if data['count'] > 0:
                    for his in data['starforce_history']:
                        self.userEnhanceData['count'] += 1
                        self.userEnhanceData['starforce_history'].append(his)
            elif response.json()['error']['message'] != 'Please try again later':
                continue
            startTime += timedelta(days=1)
        print('end crolling')
        print(self.userEnhanceData['count'])
        # for da in self.userEnhanceData['starforce_history']:
        #     print(da)
        self.userEnhanceDict = {i: [0, 0] for i in range(25)}
        for ones in self.userEnhanceData['starforce_history']:
            before = ones['before_starforce_count']
            if ones['item_upgrade_result'] == '성공':
                self.userEnhanceDict[before][0] += 1
            else:
                self.userEnhanceDict[before][1] += 1
        # 테스트용 키 live_89851af69166ce8aa7a91eb387c6842e953dd95faa2ec58e09c3282956a1dbfcefe8d04e6d233bd35cf2fabdeb93fb0d
        self.percentageCanvas.delete('user')
        for keyStr in self.userEnhanceDict.keys():
            key = int(keyStr)
            userPercent = self.userPercentage(key)
            realPercent = self.realPercentage(key)
            self.percentageCanvas.create_rectangle(self.cxs+self.cxw*key, self.cye-(400/100)*userPercent, self.cxs+self.cxw*(2*key+1)/2, self.cye, fill='yellow', tags='user')
            self.percentageCanvas.create_rectangle(self.cxs+self.cxw*(2*key+1)/2, self.cye-(400/100)*realPercent, self.cxs+self.cxw*(key+1), self.cye, fill='dodger blue', tags='user')
            self.percentageCanvas.create_text(self.cxs+self.cxw*(key+0.25), self.cye-(400/100)*userPercent-10, text=str(int(userPercent)), tags='user')
            self.percentageCanvas.create_text(self.cxs+self.cxw*(key+0.75), self.cye-(400/100)*realPercent-10, text=str(int(realPercent)), tags='user')

    def pressedEnhance(self):
        if self.checkSF.get():
            self.miniGameResult = None
            self.openMiniGame()
            successPercent = self.realPercentage(self.weaponLevel)
            if self.miniGameResult:
                successPercent *= 1.05
            self.addSpentMeso()
            luck = random.random()
            if luck <= successPercent / 100:
                # 성공
                self.weaponLevel += 1
                # 무기 업데이트 함수
            elif luck >= 1 - self.brokePrecentage(self.weaponLevel) / 100:
                # 파괴
                self.weaponLevel = 0
            else:
                # 유지
                pass
        else:
            # 스타캐치 없이 확률
            self.addSpentMeso()
            luck = random.random()
            if luck <= self.realPercentage(self.weaponLevel)/100:
                # 성공
                self.weaponLevel += 1
                # 무기 업데이트 함수
            elif luck >= 1 - self.brokePrecentage(self.weaponLevel)/100:
                # 파괴
                self.weaponLevel = 0
            else:
                # 유지
                pass
        self.upgradeWeapon()
        self.spentMesoLabel['text'] = str(int(self.spentMeso))

        if self.weaponLevel == 25:  # 풀강이다
            self.enhanceButton['state'] = 'disable'
            self.enhanceButton['bg'] = 'gray65'

    def pressedNothing(self):
        pass

    def comboSelect(self, event):
        selectStr = self.combo.get()
        selectValue = self.locateData.index(selectStr)
        self.setMapView(False)
        self.mapDescLabels[0]['text'] = self.locateData[selectValue]
        self.mapDescLabels[1]['text'] = self.addressData[selectValue]
        self.mapDescLabels[2]['text'] = self.scheduleData[selectValue]
        self.setEventImage()

    def onTabChange(self, event):
        self.window.focus()
        self.charEntry.foc_out()
        self.apiKeyEntry.foc_out()

    def changeLankServer(self, serverName):
        # 서버 이름을 받고 데이터를 API로 불러온다.
        urlString = 'https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2023-12-22&world_name=' + serverName
        response = requests.get(urlString, headers=self.headers)
        if response.status_code == 200:
            self.lankingData = response.json()['ranking']
        else:
            print('올바른 데이터 반응이 아닙니다(디버깅용)')

        self.lankPage = 0
        self.UpdateLankingLabel()

    def changeLankServerAll(self, serverMod):
        # 서버 통합 모드
        urlString = 'https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2023-12-22&world_type=' + str(serverMod)
        response = requests.get(urlString, headers=self.headers)
        if response.status_code == 200:
            self.lankingData = response.json()['ranking']
        else:
            print('올바른 데이터 반응이 아닙니다(디버깅용)')

        self.lankPage = 0
        self.UpdateLankingLabel()

    def UpdateLankingLabel(self):
        # self.lankPage 에 따라 그에 맞는 label을 보여주기 위해 업데이트
        self.lankPageLabel['text'] = str(self.lankPage+1)
        digit = self.lankPage * 10
        for i in range(10):
            nowLank = self.lankingData[i+digit]
            self.lankingLabels[i][0]['text'] = str(nowLank['ranking'])+'위'
            self.lankingLabels[i][1]['text'] = nowLank['character_name']
            if len(self.lankingLabels[i][1]['text']) > 6:
                self.lankingLabels[i][1]['font'] = self.fontS
            elif len(self.lankingLabels[i][1]['text']) > 4:
                self.lankingLabels[i][1]['font'] = self.fontN
            else:
                self.lankingLabels[i][1]['font'] = self.font
            self.lankingLabels[i][2]['text'] = str(nowLank['character_level'])+'Lv'
            self.lankingLabels[i][3]['text'] = nowLank['world_name']
            if nowLank['sub_class_name'] == '':
                self.lankingLabels[i][4]['text'] = nowLank['class_name']
            else:
                self.lankingLabels[i][4]['text'] = nowLank['sub_class_name']
            if len(self.lankingLabels[i][4]['text']) > 6:
                self.lankingLabels[i][4]['font'] = self.fontS
            elif len(self.lankingLabels[i][4]['text']) > 4:
                self.lankingLabels[i][4]['font'] = self.fontN
            else:
                self.lankingLabels[i][4]['font'] = self.font

    def userPercentage(self, s):
        successed = self.userEnhanceDict[s][0]
        sumCase = successed + self.userEnhanceDict[s][1]
        if sumCase == 0:
            return 0
        return (successed / sumCase)*100

    def realPercentage(self, s):
        if 0 <= s <= 2:
            return 95-5*s
        elif 3 <= s <= 14:
            return 100-5*s
        elif 15 <= s <= 21:
            return 30
        elif 22 == s:
            return 3
        elif 23 == s:
            return 2
        elif 24 == s:
            return 1
        else:
            pass

    def brokePrecentage(self, s):
        if 0 <= s <= 14:
            return 0
        elif 15 <= s <= 17:
            return 2.1
        elif 18 <= s <= 19:
            return 2.8
        elif 20 <= s <= 21:
            return 7.0
        elif 22 == s:
            return 19.4
        elif 23 == s:
            return 29.4
        elif 24 == s:
            return 39.6
        else:
            pass

    def upgradeWeapon(self):
        stars = ''
        for i in range(1, 25+1):
            if i <= self.weaponLevel:
                stars += '★'
            else:
                stars += '☆'

        self.weaponLVLabel['text'] = stars
        self.SFWeaponLabel['image'] = self.weaponsImage[self.weaponLevel]
        self.SFWeaponLabel.image = self.weaponsImage[self.weaponLevel]
        self.weaponLNLabel['text'] = '+'+str(self.weaponLevel)
        succesPercent = self.realPercentage(self.weaponLevel)
        brokePercent = self.brokePrecentage(self.weaponLevel)
        failPercent = 100 - (succesPercent + brokePercent)
        self.succesPercentLabel['text'] = str(float(succesPercent))+'%'
        self.failPercentLabel['text'] = str(float(failPercent))+'%'
        self.destroyPercentLabel['text'] = str(float(brokePercent))+'%'

    def addSpentMeso(self):
        weaponEquipLevel = 200
        if 0 <= self.weaponLevel <= 9:
            self.spentMeso += 1000+((weaponEquipLevel)*(self.weaponLevel+1)/36)
        elif self.weaponLevel == 10:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/571)
        elif self.weaponLevel == 11:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/314)
        elif self.weaponLevel == 12:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/214)
        elif self.weaponLevel == 13:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/157)
        elif self.weaponLevel == 14:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/107)
        elif 15 <= self.weaponLevel <= 24:
            self.spentMeso += 1000+((weaponEquipLevel)*((self.weaponLevel+1)**2.7)/200)
        else:
            pass

    def setMapView(self, first):
        url = 'https://dapi.kakao.com/v2/local/search/address.json'
        params = {'query': '경기도 시흥시 산기대학로 237', 'analyze_type': 'exact'}
        headers = {"Authorization": "KakaoAK 1afd311e3e6fc59b34bc57ed105c19aa"}  # 송승호 카카오 키
        if not first:
            selectStr = self.combo.get()
            index = self.locateData.index(selectStr)
            params['query'] = self.addressData[index]

        response = requests.get(url, params=params, headers=headers).json()
        data = response['documents']
        lat, lon = float(data[0]['y']), float(data[0]['x'])
        try:
            self.mapWidget.set_position(lat, lon, marker=True)
        except ValueError:
            print('error')

    def setEventImage(self):
        selectStr = self.combo.get()
        index = self.locateData.index(selectStr)
        if 0 <= index <= 2:
            self.mapImageLabel['image'] = self.eventImage[index]
        else:
            self.mapImageLabel['image'] = self.eventImage[2]

    def openMiniGame(self):
        def move_star():
            nonlocal star_pos, direction
            canvas.move(star, direction, 0)
            star_pos += direction

            if star_pos >= canvas_width - star_size:
                direction = -5
            elif star_pos <= 0:
                direction = 5

            if not game_ended:
                mini_game.after(30, move_star)

        def check_success(event=None):
            nonlocal game_ended
            if game_ended:
                return

            star_coords = canvas.coords(star)
            if target_x1 < star_coords[0] < target_x2:
                result_label.config(text="성공!", foreground="green")
                mini_game.after(500, close_game_window, True)
            else:
                result_label.config(text="실패!", foreground="red")
                mini_game.after(500, close_game_window, False)
            game_ended = True

        def close_game_window(result):
            self.miniGameResult = result
            mini_game.destroy()

        mini_game = Toplevel(self.window)
        mini_game.title("스타포스")
        mini_game.grab_set()  # 이 창이 닫힐 때까지 다른 창과 상호작용을 막음

        canvas_width = 400
        canvas_height = 100
        star_size = 20

        canvas = Canvas(mini_game, width=canvas_width, height=canvas_height)
        canvas.pack(pady=10)

        star_pos = random.randint(0, canvas_width - star_size)
        direction = 5
        star = canvas.create_oval(star_pos, 40, star_pos + star_size, 40 + star_size, fill="yellow")

        # 가운데 목표 영역 설정
        target_x1 = canvas_width // 2 - 50
        target_x2 = canvas_width // 2 + 50
        canvas.create_rectangle(target_x1, 40, target_x2, 60, outline="blue", width=2)

        button_check = ttk.Button(mini_game, text="확인", command=check_success)
        button_check.pack(pady=5)
        # 키 이벤트 바인딩
        mini_game.bind("<space>", check_success)
        mini_game.bind("<Return>", check_success)

        result_label = ttk.Label(mini_game, text="")
        result_label.pack(pady=5)
        game_ended = False

        mini_game.focus_set()
        move_star()
        self.window.wait_window(mini_game)  # 새로운 창이 닫힐 때까지 기다림

    def bind_enter_key(self, event):
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab == 0:  # 페이지 1
            self.pressedSearch()
        elif current_tab == 2:  # 페이지 3
            self.pressedAPIKey()

    def start_chatbot(self):
        chatbotRun.main()


class ServerMod(Enum):
    Entire = 0
    Scania = 1
    Bera = 2
    Luna = 3
    Zenis = 4
    Croah = 5
    Union = 6
    Elisium = 7
    Enosis = 8
    Red = 9
    Aurora = 10
    Arcane = 11
    Nova = 12
    RebootAll = 13
    Reboot1 = 14
    Reboot2 = 15


class EquipMod(Enum):
    hat = '모자'
    top = '상의'
    bot = '하의'
    shoe = '신발'
    weapon = '무기'
    bojo = '보조무기'
    cloak = '망토'
    glove = '장갑'


MainGUI()
