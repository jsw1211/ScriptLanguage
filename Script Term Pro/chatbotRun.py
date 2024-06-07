import time
import telepot
from datetime import date
import mapink


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        # mapink.sendMessage(chat_id, '텍스트 메세지만 이해할 수 있습니다.')
        return

    text = msg['text']
    args = text.split()

    if text.startswith('닉네임') and len(args) > 1:
        print('try to 닉네임', args[1])
        replyCharData(chat_id, args[1]) # 캐릭터 정보 찾고 보내기
    elif text.startswith('확률'):
        print('try to 확률')
        replyPercent(chat_id)   # 일반적인 단계별 확률 내보내기
    elif text.startswith('정보'):
        print('try to 정보')
        replyState(chat_id) # 챗봇에 대한 대략적인 정보 보여주기
    elif text.startswith('도움말') or text.startswith('명령어'):
        print('try to 도움말')
        replyHelp(chat_id)  # 챗봇 명령어 보여주기
    else:
        mapink.sendMessage(chat_id, 'err: 명령어가 아닙니다\n명령어를 보시고 싶으시면 "명령어" 또는 "도움말"을 입력하세요')
        pass    # 알지 못하는 명령어 처리


def replyCharData(user_id, name):
    data = mapink.getData(name)
    if not data:
        mapink.sendMessage(user_id, 'err: 입력된 캐릭터 정보를 찾을 수 없습니다')
        return
    msg = ''''''

    imageURL = data['이미지']
    for key, value in data.items():
        if key != '스텟' and key != '이미지':
            msg += key + ' - ' + str(value) + '\n'

    msg += '\n----스텟----\n'
    for key, value in data['스텟'].items():
        msg += key + ' - ' + str(value) + '\n'

    mapink.sendImage(user_id, imageURL)
    mapink.sendMessage(user_id, msg)


def replyPercent(user_id):
    msg = '''[확률]
    0 -> 1 : 95%
    1 -> 2 : 90%
    2 -> 3 : 85%
    3 -> 4 : 85%
    4 -> 5 : 80%
    5 -> 6 : 75%
    6 -> 7 : 70%
    7 -> 8 : 65%
    8 -> 9 : 60%
    9 -> 10 : 55%
    10 -> 11 : 50%
    11 -> 12 : 45%
    12 -> 13 : 40%
    13 -> 14 : 35%
    14 -> 15 : 30%
    15 -> 16 : 30%
    16 -> 17 : 30%
    17 -> 18 : 30%
    18 -> 19 : 30%
    19 -> 20 : 30%
    20 -> 21 : 30%
    21 -> 22 : 30%
    22 -> 23 : 3%
    23 -> 24 : 2%
    24 -> 25 : 1%
    '''
    mapink.sendMessage(user_id, msg)


def replyState(user_id):
    msg = '''[정보]
    이 봇은 캐릭터의 간단한 정보 조회나, 인게임 스타포스의 일반적인 확률을 알 수 있는 챗봇입니다.
    '''
    mapink.sendMessage(user_id, msg)


def replyHelp(user_id):
    msg = '''[명령어]
    - 정보: 이 챗봇에 대해 간단하게 설명한다
    - 닉네임 "검색하고 싶은 닉네임": 이 캐릭터에 대한 정보를 간단하게 보여준다
    - 확률: 스타포스 강화 확률에 대해 보여준다
    - 도움말 or 명령어: 이 챗봇에서 사용할 수 있는 명령어를 보여준다
    '''
    mapink.sendMessage(user_id, msg)

today = date.today()
print('['+str(today)+']recived token:', mapink.TOKEN)

bot = telepot.Bot(mapink.TOKEN)
print(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while True:
    time.sleep(10)
