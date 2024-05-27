from tkinter import *
from tkinter import font
import tkinter.ttk
from PIL import Image, ImageTk
from enum import Enum
import requests
import urllib.request


class MainGUI:
    headers = { # 송승호 개발용 키
        "x-nxopen-api-key": "test_cebf915b37b6eae59393a51b5d2a56e2798071e29e9cae7e85d9e988c8e293b61d98edcf6f5e475acb4e50f454c8019e"
    }

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
        self.lankSeenServer = ServerMod.Entire  # default 전체서버(일반서버 전체)
        self.lankPage = 0   # default 0 0~9페이지까지(100위까지 보여줄 예정)
        frame2 = Frame(self.window)  # 랭킹 기능
        self.notebook.add(frame2, text='랭킹 정보')
        frame2_1 = Frame(frame2, width=600, height=100, bg='gray50')
        frame2_1.grid_propagate(False)
        frame2_1.pack()
        w = 4   # 버튼 넓이
        h = 1   # 버튼 높이
        px = 60  # 버튼 넓이 픽셀
        py = 35  # 버튼 높이 픽셀
        Button(frame2_1, text='전체', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Entire), font=self.font).place(x=25+70*0, y=10, width=px, height=py)
        Button(frame2_1, text='스카니아', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Scania), font=self.fontS).place(x=25+70*1, y=10, width=px, height=py)
        Button(frame2_1, text='베라', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Bera), font=self.font).place(x=25+70*2, y=10, width=px, height=py)
        Button(frame2_1, text='루나', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Luna), font=self.font).place(x=25+70*3, y=10, width=px, height=py)
        Button(frame2_1, text='제니스', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Zenis), font=self.fontS).place(x=25+70*4, y=10, width=px, height=py)
        Button(frame2_1, text='크로아', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Croah), font=self.fontS).place(x=25+70*5, y=10, width=px, height=py)
        Button(frame2_1, text='유니온', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Union), font=self.fontS).place(x=25+70*6, y=10, width=px, height=py)
        Button(frame2_1, text='엘리시움', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Elisium), font=self.fontS).place(x=25+70*7, y=10, width=px, height=py)
        Button(frame2_1, text='이노시스', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Enosis), font=self.fontS).place(x=25+70*0, y=55, width=px, height=py)
        Button(frame2_1, text='레드', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Red), font=self.font).place(x=25+70*1, y=55, width=px, height=py)
        Button(frame2_1, text='오로라', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Aurora), font=self.fontS).place(x=25+70*2, y=55, width=px, height=py)
        Button(frame2_1, text='아케인', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Arcane), font=self.fontS).place(x=25+70*3, y=55, width=px, height=py)
        Button(frame2_1, text='노바', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Nova), font=self.font).place(x=25+70*4, y=55, width=px, height=py)
        Button(frame2_1, text='리부트', width=w, height=h, command=lambda : self.pressedServer(ServerMod.RebootAll), font=self.fontS).place(x=25+70*5, y=55, width=px, height=py)
        Button(frame2_1, text='리부트1', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Reboot1), font=self.fontS).place(x=25+70*6, y=55, width=px, height=py)
        Button(frame2_1, text='리부트2', width=w, height=h, command=lambda : self.pressedServer(ServerMod.Reboot2), font=self.fontS).place(x=25+70*7, y=55, width=px, height=py)
        # 임시 랭킹들 나열
        Frame(frame2, width=600, height=30, background='LightBlue1').pack()
        frame2_2 = Frame(frame2, width=600, height=550, bg='gray50', padx=10, pady=10)
        frame2_2.grid_propagate(False)
        frame2_2.pack()
        px = 24  # 버튼 패딩 양옆에 - 버튼 사이 간격 확보
        py = 4  # 버튼 패딩 위아래 - 버튼 사이 간격 확보
        Label(frame2_2, text='랭킹 #', width=5, height=2, font=self.font).grid(row=0, column=0, padx=px, pady=py)
        Label(frame2_2, text='닉네임', width=5, height=2, font=self.font).grid(row=0, column=1, padx=px, pady=py)
        Label(frame2_2, text='레벨', width=5, height=2, font=self.font).grid(row=0, column=2, padx=px, pady=py)
        Label(frame2_2, text='서버', width=5, height=2, font=self.font).grid(row=0, column=3, padx=px, pady=py)
        Label(frame2_2, text='직업', width=5, height=2, font=self.font).grid(row=0, column=4, padx=px, pady=py)
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
                label.grid(row=i+1, column=j, padx=px, pady=py)
        # 다음 페이지 버튼(10 페이지 정도 생각중)
        Frame(frame2, width=600, height=30, background='LightBlue1').pack()
        frame2_3 = Frame(frame2, width=600, height=60, bg='plum1')
        frame2_3.pack()
        Button(frame2_3, text='<-', width=10, height=2, command=self.pressedPrev, font=self.fontB).place(x=150, y=0, width=100, height=50)
        Button(frame2_3, text='->', width=10, height=2, command=self.pressedNext, font=self.fontB).place(x=350, y=0, width=100, height=50)
        self.changeLankServerAll(0)

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

    def pressedServer(self, server):
        serverNameKorea = ''
        if server == ServerMod.Entire or server == ServerMod.RebootAll:
            self.lankSeenServer = server
            if server == ServerMod.Entire:
                self.changeLankServerAll(0) # 0이 일반 서버
            else:
                self.changeLankServerAll(1) # 1이 리부트 서버이기 때문에
        elif server in ServerMod:
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
        digit = self.lankPage * 10
        for i in range(10):
            nowLank = self.lankingData[i+digit]
            self.lankingLabels[i][0]['text'] = str(nowLank['ranking'])+'위'
            self.lankingLabels[i][1]['text'] = nowLank['character_name']
            self.lankingLabels[i][2]['text'] = str(nowLank['character_level'])+'Lv'
            self.lankingLabels[i][3]['text'] = nowLank['world_name']
            self.lankingLabels[i][4]['text'] = nowLank['class_name']


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


MainGUI()
