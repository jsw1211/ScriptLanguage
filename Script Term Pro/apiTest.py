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

# 가져온 id로 캐릭터 정보 조회
urlString_1 = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + response.json()['ocid']
response_1 = requests.get(urlString_1, headers=headers)

print(response_1.json())
