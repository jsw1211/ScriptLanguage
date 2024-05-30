import requests
import tkinter
from tkintermapview import TkinterMapView


url = 'https://dapi.kakao.com/v2/local/search/address.json'
params = {'query': '경기도 시흥시 산기대학로 237', 'analyze_type': 'exact'}
headers = {"Authorization": "KakaoAK 1afd311e3e6fc59b34bc57ed105c19aa"} # 송승호 카카오 키
response = requests.get(url, params=params, headers=headers).json()
data = response['documents']

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
