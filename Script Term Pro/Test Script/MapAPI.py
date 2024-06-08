import requests
import tkinter
from tkintermapview import TkinterMapView


url = 'https://dapi.kakao.com/v2/local/search/address.json'
params = {'query': '경기도 시흥시 산기대학로 237', 'analyze_type': 'exact'}
params['query'] = '서울 송파구 올림픽로 240'
params['query'] = '서울 영등포구 여의대로 108'
params['query'] = '서울 송파구 올림픽로 424'
params['query'] = '서울 영등포구 영중로 15'
params['query'] = '서울 용산구 한강대로23길 55'
params['query'] = '대전 중구 계백로 1700'
params['query'] = '부산 부산진구 동천로 4'
params['query'] = '대구 중구 중앙대로 412'
params['query'] = '광주 서구 무진대로 904'
params['query'] = '서울 성동구 왕십리광장로 17'
params['query'] = '서울 서대문구 신촌로 129'
params['query'] = '인천 남동구 예술로 198'
params['query'] = '강원특별자치도 원주시 서원대로 171'
params['query'] = '제주특별자치도 제주시 노형로 407'
params['query'] = '서울 중랑구 상봉로 131'
params['query'] = '충남 천안시 서북구 공원로 196'
headers = {"Authorization": "KakaoAK 1afd311e3e6fc59b34bc57ed105c19aa"} # 송승호 카카오 키
response = requests.get(url, params=params, headers=headers).json()
data = response['documents']

print(data[0])
print(data[0]['x'], data[0]['y'])
class App(tkinter.Tk):
    APP_NAME = "Kakao X GoogleMaps"
    WIDTH = 800
    HEIGHT = 750

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.map_widget = TkinterMapView(width=self.WIDTH, height=600, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan=3, sticky="nsew")

        lat, lon = float(data[0]['y']), float(data[0]['x'])
        try:
            self.map_widget.set_position(lat, lon, marker=True)
        except ValueError:
            print('error')

        self.mainloop()


app = App()
