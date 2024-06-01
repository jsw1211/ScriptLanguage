from tkinter import *
from tkinter import font
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


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

        mainText = ''
        for first, second in self.parent.charData.items():
            mainText += str(first) + ': ' + str(second) + '\n'

        htmlBody = f"""
            <html>
            <body>
            <img src="cid:image1">
            <p>{mainText}</p>
            </body>
            </html>
            """
        msgPart = MIMEText(htmlBody, 'html')
        msg.attach(msgPart)

        imgPath = 'Resource/Image/tempCharImage.png'
        with open(imgPath, 'rb') as imgFile:
            imgData = imgFile.read()
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
