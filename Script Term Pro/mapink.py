import telepot
import requests
import traceback
import sys

headers = {
"x-nxopen-api-key": "test_cebf915b37b6eae59393a51b5d2a56e2798071e29e9cae7e85d9e988c8e293b61d98edcf6f5e475acb4e50f454c8019e"
}
baseurl = 'https://open.api.nexon.com/maplestory/v1/id?character_name='
addiurl = 'https://open.api.nexon.com/maplestory/v1/character/'
TOKEN = '7133683141:AAGUsobyWizQI6e5LEbWNwypwogZ_wdBVZQ'
MAX_MSG_LENGTH = 300
bot = telepot.Bot(TOKEN)


def getData(name):
    nameurl = baseurl+str(name)
    response_id = requests.get(nameurl, headers=headers)
    if response_id.status_code == 200:
        pass
    else:
        print('올바른 닉네임이 아닙니다')
        return {}

    ocid = response_id.json()['ocid']

    dataurl1 = addiurl+'basic?ocid='+str(ocid)
    response1 = requests.get(dataurl1, headers=headers)
    dataurl2 = addiurl+'popularity?ocid='+str(ocid)
    response2 = requests.get(dataurl2, headers=headers)
    dataurl3 = addiurl+'stat?ocid='+str(ocid)
    response3 = requests.get(dataurl3, headers=headers)
    dataurl4 = addiurl+'dojang?ocid='+str(ocid)
    response4 = requests.get(dataurl4, headers=headers)

    basicData = response1.json()
    populData = response2.json()
    statuData = response3.json()
    mureuData = response4.json()

    returnData = {}
    returnData['이미지'] = basicData.get('character_image')
    returnData['닉네임'] = basicData.get('character_name')
    returnData['직업'] = basicData.get('character_class')
    returnData['레밸'] = basicData.get('character_level')
    returnData['서버'] = basicData.get('world_name')
    returnData['길드'] = basicData.get('character_guild_name')
    returnData['인기도'] = basicData.get('character_guild_name')
    returnData['길드'] = populData.get('popularity')
    returnData['무릉'] = mureuData.get('dojang_best_floor')

    mainStat = {}
    for stat in statuData['final_stat']:
        if stat['stat_name'] == 'HP':
            mainStat['HP'] = stat['stat_value']
        elif stat['stat_name'] == 'MP':
            mainStat['MP'] = stat['stat_value']
        elif stat['stat_name'] == 'STR':
            mainStat['STR'] = stat['stat_value']
        elif stat['stat_name'] == 'DEX':
            mainStat['DEX'] = stat['stat_value']
        elif stat['stat_name'] == 'INT':
            mainStat['INT'] = stat['stat_value']
        elif stat['stat_name'] == 'LUK':
            mainStat['LUK'] = stat['stat_value']

    returnData['스텟'] = mainStat

    return returnData


def sendMessage(user_id, msg):
    try:
        bot.sendMessage(user_id, msg)
    except:
        traceback.print_exc(file=sys.stdout)


def sendImage(user_id, url):
    try:
        bot.sendPhoto(user_id, url)
    except:
        traceback.print_exc(file=sys.stdout)
