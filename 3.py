import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=nanjing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
data['main']['temp']
data['main']['pressure']
data['weather'][0]['description']
