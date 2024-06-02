from tkinter import *
from tkinter import font
import tkinter.messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests


class mailGUI:
    instance = None

    smtpServer = "smtp.gmail.com"
    mailHost = "msTermProject2024@gmail.com"
    mailPassword = "othe owvl tcwp dooo"
    portNum = 587

    def __init__(self, parent):
        if mailGUI.instance is not None:
            return

        mailGUI.instance = self
        self.parent = parent

        self.window = Toplevel()
        self.window.title('메일 시스템')
        self.window.geometry('400x200')
        self.window.protocol("WM_DELETE_WINDOW", self.onClose)

        self.mailFont = font.Font(self.window, size=16, weight='bold', family='굴림')
        self.mailFontB = font.Font(self.window, size=32, weight='bold', family='굴림')

        self.mailStr = StringVar()
        entry = Entry(self.window, textvariable=self.mailStr, font=self.mailFont)
        entry.place(x=50, y=50, width=300, height=25)
        button = Button(self.window, text='보내기', command=self.pressedSend, font=self.mailFontB)
        button.place(x=100, y=100, width=200, height=80)

        self.window.mainloop()

    def pressedSend(self):
        reciveAddress = self.mailStr.get()
        reciveAddress.strip()

        msg = MIMEMultipart()
        msg['From'] = self.mailHost
        msg['To'] = reciveAddress
        msg['Subject'] = "메이플스토리 캐릭터 정보"

        if self.parent.charData is None:
            tkinter.messagebox.showinfo('오류', '캐릭터 정보를 조회하지 않았습니다.')
            self.onClose()
            return

        htmlBody = f"""
            <html>
            <body>
            <img src="cid:image1">
            <p>{'닉네임: ' + str(self.parent.charData['character_gender'])}</p>
            <p>{'길드: ' + str(self.parent.charData['character_guild_name'])}</p>
            <p>{'서버: ' + str(self.parent.charData['world_name'])}</p>
            <p>{'직업: ' + str(self.parent.charData['character_class'])}</p>
            <p>{'레밸: ' + str(self.parent.charData['character_level'])}</p>
            <p>{'경험치: ' + str(self.parent.charData['character_exp_rate'])}</p>
            <p>{'인기도: ' + str(self.parent.charData_pop['popularity'])}</p>
            <p>{'무릉(최고층): ' + str(self.parent.charData_mureung['dojang_best_floor'])}</p>
            <p>{'스텟들'}</p>
            </body>
            </html>
            """
        msgPart = MIMEText(htmlBody, 'html')
        msg.attach(msgPart)

        imgUrl = str(self.parent.charData['character_image'])
        response = requests.get(imgUrl)
        imgData = response.content
        img = MIMEImage(imgData)
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)

        try:
            server = smtplib.SMTP(self.smtpServer, self.portNum)
            server.starttls()
            server.login(self.mailHost, self.mailPassword)
            text = msg.as_string()
            server.sendmail(self.mailHost, reciveAddress, text)
            server.quit()
            print('이메일 보내기 성공적')
        except smtplib.SMTPException as e:
            print(f"이메일 보내기 실패. SMTPException: {e}")
        except Exception as e:
            print(f'이메일 보내기 실패. Error: {e}')

        self.onClose()

    def onClose(self):
        mailGUI.instance = None
        self.parent = None
        self.window.destroy()
