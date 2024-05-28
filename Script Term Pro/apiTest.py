import requests
import urllib.request

# 내 키를 사용한 api 접근
headers = {             #허용 받은 키 입력
    "x-nxopen-api-key": "test_cebf915b37b6eae59393a51b5d2a56e2798071e29e9cae7e85d9e988c8e293b61d98edcf6f5e475acb4e50f454c8019e"
}

# 닉네임으로 유저식별번호(id) 가져오기
characterName = "세글자"
encCharName = urllib.parse.quote(characterName)
urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + encCharName
response = requests.get(urlString, headers=headers)

print(response.json())
print('\n')

# 가져온 id로 캐릭터 정보 조회
urlString_1 = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + response.json()['ocid']
response_1 = requests.get(urlString_1, headers=headers)

print(response_1.json())
print('\n\n')

# 캐릭터 장비 조회
urlString_5 = "https://open.api.nexon.com/maplestory/v1/character/item-equipment?ocid=" + response.json()['ocid']
response_5 = requests.get(urlString_5, headers=headers)
print(response_5.json())
print('\n\n')

#능력치 조회
urlString_6 = "https://open.api.nexon.com/maplestory/v1/character/stat?ocid=" + response.json()['ocid']
response_6 = requests.get(urlString_6, headers=headers)
print(response_6.json())
print('\n\n')

#무릉 조회
urlString_7 = "https://open.api.nexon.com/maplestory/v1/character/dojang?ocid=" + response.json()['ocid']
response_7 = requests.get(urlString_7, headers=headers)
print(response_7.json())
print('\n\n')

# 랭킹정보 보기 서버는 전체(일반서버 기준)
urlString_2 = "https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2023-12-22"
response_2 = requests.get(urlString_2, headers=headers)

for char in response_2.json()['ranking']:
    print(char)

# 서버를 특정하고 싶으면
serverName = "스카니아"
encServerName = urllib.parse.quote(serverName)
urlString_3 = "https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2023-12-22&world_name="+encServerName
response_3 = requests.get(urlString_3, headers=headers)

print('\n\n')
print(serverName)
print('\n\n')
for char in response_3.json()['ranking']:
    print(char)

# 스타포스 강화 정보 count가 몇개씩 가져올 건지
urlString_4 = "https://open.api.nexon.com/maplestory/v1/history/starforce?count=100&date=2023-12-27"
response_4 = requests.get(urlString_4, headers=headers)

print('\n\n')
print(response_4.json())
