import mimetypes
import smtplib
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText

smtpServer = "smtp.gmail.com"
mailHost = "msTermProject2024@gmail.com"
mailPassword = "othe owvl tcwp dooo"
portNum = 587
sendMailAddress = "yudle537@gmail.com"    # 테스트용 메일

msg = MIMEMultipart()
msg['From'] = mailHost
msg['To'] = sendMailAddress
msg['Subject'] = "Test Mail"

msgPart = MIMEText('123', 'plain')
msg.attach(msgPart)

try:
    server = smtplib.SMTP(smtpServer, portNum)
    server.starttls()
    server.login(mailHost, mailPassword)
    text = msg.as_string()
    server.sendmail(mailHost, sendMailAddress, text)
    server.quit()
    print('이메일 보내기 성공적')
except Exception as e:
    print(f'이메일 보내기 실패. Error: {e}')
