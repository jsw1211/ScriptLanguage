import telepot

bot = telepot.Bot('7133683141:AAGUsobyWizQI6e5LEbWNwypwogZ_wdBVZQ') #우리가 생성한 챗봇
myID = '7313475512 '    # 사용자의 아이디

response = bot.getMe()  # 챗봇의 정보
print(response)

msg = '메핑크빈 테스트'    # 보낼 메세지
bot.sendMessage(myID, msg)  # 메세지 보내기
