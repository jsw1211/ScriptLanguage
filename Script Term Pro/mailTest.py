import mimetypes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


smtpServer = "smtp.gmail.com"
mailHost = "msTermProject2024@gmail.com"
mailPassword = "othe owvl tcwp dooo"
portNum = 587
sendMailAddress = "yudle537@gmail.com"    # 테스트용 메일

msg = MIMEMultipart()
msg['From'] = mailHost
msg['To'] = sendMailAddress
msg['Subject'] = "Test Mail"

mainText = '123456'
htmlBody = f"""
    <html>
    <body>
    <p>{mainText}</p>
    <img src="cid:image1">
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
    server = smtplib.SMTP(smtpServer, portNum)
    server.starttls()
    server.login(mailHost, mailPassword)
    text = msg.as_string()
    server.sendmail(mailHost, sendMailAddress, text)
    server.quit()
    print('이메일 보내기 성공적')
except smtplib.SMTPException as e:
    print(f"이메일 보내기 실패. SMTPException: {e}")
except Exception as e:
    print(f'이메일 보내기 실패. Error: {e}')
