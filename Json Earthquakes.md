```python
import json
import requests
from datetime import datetime
urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
```


```python
response = requests.get(urlData)
print(response.status_code)
```

    200
    


```python
#loading the data into a dictionary:
json_response = response.json()

print(json_response)
```

    {'type': 'FeatureCollection', 'metadata': {'generated': 1631265635000, 'url': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson', 'title': 'USGS Magnitude 2.5+ Earthquakes, Past Day', 'status': 200, 'api': '1.10.3', 'count': 51}, 'features': [{'type': 'Feature', 'properties': {'mag': 4.3, 'place': '138 km SE of Mil’kovo, Russia', 'time': 1631263194816, 'updated': 1631264289040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9xw', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9xw.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 284, 'net': 'us', 'code': '7000f9xw', 'ids': ',us7000f9xw,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 1.346, 'rms': 0.58, 'gap': 148, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.3 - 138 km SE of Mil’kovo, Russia'}, 'geometry': {'type': 'Point', 'coordinates': [160.3091, 53.9318, 73.46]}, 'id': 'us7000f9xw'}, {'type': 'Feature', 'properties': {'mag': 2.48, 'place': '13km WSW of The Geysers, CA', 'time': 1631261981930, 'updated': 1631262283849, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73623001', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73623001.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 95, 'net': 'nc', 'code': '73623001', 'ids': ',nc73623001,', 'sources': ',nc,', 'types': ',nearby-cities,origin,phase-data,', 'nst': 7, 'dmin': 0.08681, 'rms': 0.22, 'gap': 166, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.5 - 13km WSW of The Geysers, CA'}, 'geometry': {'type': 'Point', 'coordinates': [-122.8926697, 38.7291679, 4.38]}, 'id': 'nc73623001'}, {'type': 'Feature', 'properties': {'mag': 3.1, 'place': '57 km NNW of Yakutat, Alaska', 'time': 1631260329152, 'updated': 1631261097040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmjg046', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmjg046.geojson', 'felt': 1, 'cdi': 2, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 148, 'net': 'ak', 'code': '021bmjg046', 'ids': ',ak021bmjg046,us7000f9xh,', 'sources': ',ak,us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.84, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.1 - 57 km NNW of Yakutat, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-140.1444, 60.0157, 6.8]}, 'id': 'ak021bmjg046'}, {'type': 'Feature', 'properties': {'mag': 3.3, 'place': '151 km S of False Pass, Alaska', 'time': 1631259634814, 'updated': 1631260791040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9xd', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9xd.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 168, 'net': 'us', 'code': '7000f9xd', 'ids': ',us7000f9xd,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 1.167, 'rms': 0.77, 'gap': 203, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.3 - 151 km S of False Pass, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-163.6824, 53.5014, 28.49]}, 'id': 'us7000f9xd'}, {'type': 'Feature', 'properties': {'mag': 4, 'place': '187 km S of False Pass, Alaska', 'time': 1631253474087, 'updated': 1631255086040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x5', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x5.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 246, 'net': 'us', 'code': '7000f9x5', 'ids': ',us7000f9x5,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 1.535, 'rms': 0.75, 'gap': 158, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.0 - 187 km S of False Pass, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-163.4259, 53.1666, 15.24]}, 'id': 'us7000f9x5'}, {'type': 'Feature', 'properties': {'mag': 4, 'place': '98 km ESE of Iquique, Chile', 'time': 1631252756864, 'updated': 1631254599049, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x1', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x1.geojson', 'felt': 3, 'cdi': 2.5, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 247, 'net': 'us', 'code': '7000f9x1', 'ids': ',us7000f9x1,', 'sources': ',us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': 0.451, 'rms': 1.01, 'gap': 63, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.0 - 98 km ESE of Iquique, Chile'}, 'geometry': {'type': 'Point', 'coordinates': [-69.3082, -20.6219, 87.5]}, 'id': 'us7000f9x1'}, {'type': 'Feature', 'properties': {'mag': 4.7, 'place': '51 km ESE of Hualien City, Taiwan', 'time': 1631252702750, 'updated': 1631254012040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x2', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x2.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 340, 'net': 'us', 'code': '7000f9x2', 'ids': ',us7000f9x2,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 0.561, 'rms': 0.54, 'gap': 96, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.7 - 51 km ESE of Hualien City, Taiwan'}, 'geometry': {'type': 'Point', 'coordinates': [122.0859, 23.8356, 32.7]}, 'id': 'us7000f9x2'}, {'type': 'Feature', 'properties': {'mag': 3.3, 'place': '24 km WNW of Clam Gulch, Alaska', 'time': 1631251909539, 'updated': 1631252408040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmi4pzu', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmi4pzu.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 168, 'net': 'ak', 'code': '021bmi4pzu', 'ids': ',us7000f9wz,ak021bmi4pzu,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.67, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.3 - 24 km WNW of Clam Gulch, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-151.7925, 60.3186, 62.1]}, 'id': 'ak021bmi4pzu'}, {'type': 'Feature', 'properties': {'mag': 4.4, 'place': '36 km S of Jurm, Afghanistan', 'time': 1631251361104, 'updated': 1631254776040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wy', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wy.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 298, 'net': 'us', 'code': '7000f9wy', 'ids': ',us7000f9wy,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 0.622, 'rms': 0.68, 'gap': 73, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.4 - 36 km S of Jurm, Afghanistan'}, 'geometry': {'type': 'Point', 'coordinates': [70.8408, 36.539, 194.11]}, 'id': 'us7000f9wy'}, {'type': 'Feature', 'properties': {'mag': 5.1, 'place': 'West Chile Rise', 'time': 1631247689051, 'updated': 1631249026040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wt', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wt.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 400, 'net': 'us', 'code': '7000f9wt', 'ids': ',us7000f9wt,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 8.683, 'rms': 1.26, 'gap': 116, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 5.1 - West Chile Rise'}, 'geometry': {'type': 'Point', 'coordinates': [-83.6903, -42.8606, 10]}, 'id': 'us7000f9wt'}, {'type': 'Feature', 'properties': {'mag': 4.6, 'place': '41 km SE of Calana, Peru', 'time': 1631244338702, 'updated': 1631245269040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wf', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wf.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 326, 'net': 'us', 'code': '7000f9wf', 'ids': ',us7000f9wf,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 0.413, 'rms': 0.79, 'gap': 94, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.6 - 41 km SE of Calana, Peru'}, 'geometry': {'type': 'Point', 'coordinates': [-69.9241, -18.2139, 97.66]}, 'id': 'us7000f9wf'}, {'type': 'Feature', 'properties': {'mag': 2.7, 'place': '36 km NW of Deering, Alaska', 'time': 1631243352784, 'updated': 1631243891040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmgt26m', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmgt26m.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 112, 'net': 'ak', 'code': '021bmgt26m', 'ids': ',us7000f9wc,ak021bmgt26m,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.99, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.7 - 36 km NW of Deering, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-163.2264, 66.3321, 0]}, 'id': 'ak021bmgt26m'}, {'type': 'Feature', 'properties': {'mag': 4.3, 'place': 'Izu Islands, Japan region', 'time': 1631239825805, 'updated': 1631242089040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9w2', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9w2.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 284, 'net': 'us', 'code': '7000f9w2', 'ids': ',us7000f9w2,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 2.059, 'rms': 1.39, 'gap': 108, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.3 - Izu Islands, Japan region'}, 'geometry': {'type': 'Point', 'coordinates': [139.8833, 31.0509, 164.41]}, 'id': 'us7000f9w2'}, {'type': 'Feature', 'properties': {'mag': 4.7, 'place': '87 km ESE of Katsuren-haebaru, Japan', 'time': 1631239285981, 'updated': 1631242317597, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9w1', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9w1.geojson', 'felt': 1, 'cdi': 1, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 340, 'net': 'us', 'code': '7000f9w1', 'ids': ',us7000f9w1,', 'sources': ',us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': 0.809, 'rms': 0.99, 'gap': 77, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.7 - 87 km ESE of Katsuren-haebaru, Japan'}, 'geometry': {'type': 'Point', 'coordinates': [128.7154, 26.1275, 10]}, 'id': 'us7000f9w1'}, {'type': 'Feature', 'properties': {'mag': 4.4, 'place': '105 km SW of Bengkulu, Indonesia', 'time': 1631238141436, 'updated': 1631240153040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vv', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vv.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 298, 'net': 'us', 'code': '7000f9vv', 'ids': ',us7000f9vv,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 1.268, 'rms': 0.57, 'gap': 190, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.4 - 105 km SW of Bengkulu, Indonesia'}, 'geometry': {'type': 'Point', 'coordinates': [101.7007, -4.5689, 36.55]}, 'id': 'us7000f9vv'}, {'type': 'Feature', 'properties': {'mag': 3.5, 'place': '48 km N of Valdez, Alaska', 'time': 1631237201581, 'updated': 1631237964040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmfpwdp', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmfpwdp.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 188, 'net': 'ak', 'code': '021bmfpwdp', 'ids': ',us7000f9vs,ak021bmfpwdp,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.87, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.5 - 48 km N of Valdez, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-146.518, 61.5628, 16.5]}, 'id': 'ak021bmfpwdp'}, {'type': 'Feature', 'properties': {'mag': 5, 'place': '53 km NE of Anse-Bertrand, Guadeloupe', 'time': 1631234599179, 'updated': 1631265427932, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vl', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vl.geojson', 'felt': 39, 'cdi': 4.6, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 403, 'net': 'us', 'code': '7000f9vl', 'ids': ',us7000f9vl,', 'sources': ',us,', 'types': ',dyfi,moment-tensor,origin,phase-data,', 'nst': None, 'dmin': 0.787, 'rms': 0.72, 'gap': 59, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 5.0 - 53 km NE of Anse-Bertrand, Guadeloupe'}, 'geometry': {'type': 'Point', 'coordinates': [-61.1489, 16.8112, 45.13]}, 'id': 'us7000f9vl'}, {'type': 'Feature', 'properties': {'mag': 4.7, 'place': 'south of the Fiji Islands', 'time': 1631233261422, 'updated': 1631234326040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vi', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vi.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 340, 'net': 'us', 'code': '7000f9vi', 'ids': ',us7000f9vi,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 4.423, 'rms': 1, 'gap': 75, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.7 - south of the Fiji Islands'}, 'geometry': {'type': 'Point', 'coordinates': [178.4356, -26.2276, 618.5]}, 'id': 'us7000f9vi'}, {'type': 'Feature', 'properties': {'mag': 4.5, 'place': '105 km NE of Hotan, China', 'time': 1631231315869, 'updated': 1631232756040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9v9', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9v9.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 312, 'net': 'us', 'code': '7000f9v9', 'ids': ',us7000f9v9,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 5.222, 'rms': 0.84, 'gap': 150, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.5 - 105 km NE of Hotan, China'}, 'geometry': {'type': 'Point', 'coordinates': [80.9206, 37.642, 15.2]}, 'id': 'us7000f9v9'}, {'type': 'Feature', 'properties': {'mag': 3.6, 'place': '85 km SW of Atka, Alaska', 'time': 1631231042205, 'updated': 1631232916040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vd', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vd.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 199, 'net': 'us', 'code': '7000f9vd', 'ids': ',ak021bl5dv3j,us7000f9vd,', 'sources': ',ak,us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 0.588, 'rms': 0.45, 'gap': 228, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.6 - 85 km SW of Atka, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-175.1182, 51.679, 49.58]}, 'id': 'us7000f9vd'}, {'type': 'Feature', 'properties': {'mag': 4.5, 'place': '29 km SE of Jurm, Afghanistan', 'time': 1631230995638, 'updated': 1631232478040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9v7', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9v7.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 312, 'net': 'us', 'code': '7000f9v7', 'ids': ',us7000f9v7,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 0.595, 'rms': 0.6, 'gap': 70, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.5 - 29 km SE of Jurm, Afghanistan'}, 'geometry': {'type': 'Point', 'coordinates': [71.0717, 36.6812, 214.18]}, 'id': 'us7000f9v7'}, {'type': 'Feature', 'properties': {'mag': 3.12, 'place': '0 km NNE of Central Aguirre, Puerto Rico', 'time': 1631226713140, 'updated': 1631235906684, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252012', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252012.geojson', 'felt': 2, 'cdi': 3.4, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 150, 'net': 'pr', 'code': '2021252012', 'ids': ',pr2021252012,', 'sources': ',pr,', 'types': ',dyfi,origin,phase-data,', 'nst': 9, 'dmin': 0.1153, 'rms': 0.11, 'gap': 199, 'magType': 'md', 'type': 'earthquake', 'title': 'M 3.1 - 0 km NNE of Central Aguirre, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-66.2218, 17.9563, 12]}, 'id': 'pr2021252012'}, {'type': 'Feature', 'properties': {'mag': 4.32, 'place': '10km SW of Petrolia, CA', 'time': 1631224676520, 'updated': 1631260873897, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73622771', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622771.geojson', 'felt': 34, 'cdi': 3.4, 'mmi': 2.978, 'alert': 'green', 'status': 'reviewed', 'tsunami': 0, 'sig': 299, 'net': 'nc', 'code': '73622771', 'ids': ',nc73622771,us7000f9um,', 'sources': ',nc,us,', 'types': ',dyfi,focal-mechanism,losspager,moment-tensor,nearby-cities,origin,phase-data,scitech-link,shakemap,', 'nst': 23, 'dmin': 0.03464, 'rms': 0.11, 'gap': 229, 'magType': 'mw', 'type': 'earthquake', 'title': 'M 4.3 - 10km SW of Petrolia, CA'}, 'geometry': {'type': 'Point', 'coordinates': [-124.3813333, 40.2705, 32.83]}, 'id': 'nc73622771'}, {'type': 'Feature', 'properties': {'mag': 4.5, 'place': '218 km ENE of Levuka, Fiji', 'time': 1631224606389, 'updated': 1631225939040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9un', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9un.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 312, 'net': 'us', 'code': '7000f9un', 'ids': ',us7000f9un,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 3.131, 'rms': 0.47, 'gap': 118, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.5 - 218 km ENE of Levuka, Fiji'}, 'geometry': {'type': 'Point', 'coordinates': [-178.6636, -17.6588, 558.09]}, 'id': 'us7000f9un'}, {'type': 'Feature', 'properties': {'mag': 3.2, 'place': 'off the coast of Oregon', 'time': 1631223714848, 'updated': 1631235018586, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9ug', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9ug.geojson', 'felt': 1, 'cdi': 2, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 158, 'net': 'us', 'code': '7000f9ug', 'ids': ',us7000f9ug,', 'sources': ',us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': 1.901, 'rms': 0.63, 'gap': 207, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.2 - off the coast of Oregon'}, 'geometry': {'type': 'Point', 'coordinates': [-128.6559, 44.0804, 10]}, 'id': 'us7000f9ug'}, {'type': 'Feature', 'properties': {'mag': 2.76, 'place': '4 km SSE of Guánica, Puerto Rico', 'time': 1631223455590, 'updated': 1631225208721, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252008', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252008.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 117, 'net': 'pr', 'code': '2021252008', 'ids': ',pr2021252008,', 'sources': ',pr,', 'types': ',origin,phase-data,', 'nst': 14, 'dmin': 0.1591, 'rms': 0.19, 'gap': 217, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.8 - 4 km SSE of Guánica, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-66.8893, 17.933, 8]}, 'id': 'pr2021252008'}, {'type': 'Feature', 'properties': {'mag': 2.49, 'place': '4 km SSE of Guánica, Puerto Rico', 'time': 1631223240640, 'updated': 1631235660530, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252009', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252009.geojson', 'felt': 1, 'cdi': 3.1, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 96, 'net': 'pr', 'code': '2021252009', 'ids': ',pr2021252009,', 'sources': ',pr,', 'types': ',dyfi,origin,phase-data,', 'nst': 19, 'dmin': 0.1608, 'rms': 0.1, 'gap': 197, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.5 - 4 km SSE of Guánica, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-66.8875, 17.9335, 8]}, 'id': 'pr2021252009'}, {'type': 'Feature', 'properties': {'mag': 2.6, 'place': '64 km SE of Denali National Park, Alaska', 'time': 1631222145650, 'updated': 1631224866130, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bl40vdu', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bl40vdu.geojson', 'felt': 1, 'cdi': 3.4, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 104, 'net': 'ak', 'code': '021bl40vdu', 'ids': ',ak021bl40vdu,us7000f9u7,', 'sources': ',ak,us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.46, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.6 - 64 km SE of Denali National Park, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-150.8869, 63.0995, 120.8]}, 'id': 'ak021bl40vdu'}, {'type': 'Feature', 'properties': {'mag': 2.68, 'place': '26 km NW of Rincón, Puerto Rico', 'time': 1631221855060, 'updated': 1631222739694, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252007', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252007.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 110, 'net': 'pr', 'code': '2021252007', 'ids': ',pr2021252007,', 'sources': ',pr,', 'types': ',origin,phase-data,', 'nst': 5, 'dmin': 0.324, 'rms': 0.16, 'gap': 309, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.7 - 26 km NW of Rincón, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-67.4323, 18.5105, 6]}, 'id': 'pr2021252007'}, {'type': 'Feature', 'properties': {'mag': 3.18, 'place': '4 km SSE of Guánica, Puerto Rico', 'time': 1631219603990, 'updated': 1631221087337, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252006', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252006.geojson', 'felt': 1, 'cdi': 2.2, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 156, 'net': 'pr', 'code': '2021252006', 'ids': ',pr2021252006,us7000f9tv,', 'sources': ',pr,us,', 'types': ',dyfi,origin,phase-data,', 'nst': 22, 'dmin': 0.1549, 'rms': 0.2, 'gap': 196, 'magType': 'md', 'type': 'earthquake', 'title': 'M 3.2 - 4 km SSE of Guánica, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-66.8928, 17.9368, 7]}, 'id': 'pr2021252006'}, {'type': 'Feature', 'properties': {'mag': 2.86, 'place': '8 km W of Hormigueros, Puerto Rico', 'time': 1631215542980, 'updated': 1631217369864, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252005', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252005.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 126, 'net': 'pr', 'code': '2021252005', 'ids': ',pr2021252005,', 'sources': ',pr,', 'types': ',origin,phase-data,', 'nst': 12, 'dmin': 0.1736, 'rms': 0.11, 'gap': 167, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.9 - 8 km W of Hormigueros, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-67.206, 18.1508, 11]}, 'id': 'pr2021252005'}, {'type': 'Feature', 'properties': {'mag': 5.1, 'place': 'Unimak Island region, Alaska', 'time': 1631215405350, 'updated': 1631259213016, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9t5', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9t5.geojson', 'felt': 2, 'cdi': 1, 'mmi': 1.826, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 400, 'net': 'us', 'code': '7000f9t5', 'ids': ',us7000f9t5,ak021bl2vo50,', 'sources': ',us,ak,', 'types': ',dyfi,oaf,origin,phase-data,shakemap,', 'nst': None, 'dmin': 1.179, 'rms': 0.84, 'gap': 148, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 5.1 - Unimak Island region, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-163.5308, 53.4726, 21.48]}, 'id': 'us7000f9t5'}, {'type': 'Feature', 'properties': {'mag': 2.8, 'place': '292 km W of Bandon, Oregon', 'time': 1631213883277, 'updated': 1631220542040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9t0', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9t0.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 121, 'net': 'us', 'code': '7000f9t0', 'ids': ',us7000f9t0,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 2.077, 'rms': 0.57, 'gap': 291, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.8 - 292 km W of Bandon, Oregon'}, 'geometry': {'type': 'Point', 'coordinates': [-127.967, 43.5592, 10]}, 'id': 'us7000f9t0'}, {'type': 'Feature', 'properties': {'mag': 2.7, 'place': '102 km WSW of Craig, Alaska', 'time': 1631212277953, 'updated': 1631220115040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bl2byl3', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bl2byl3.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 112, 'net': 'ak', 'code': '021bl2byl3', 'ids': ',us7000f9sv,ak021bl2byl3,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.43, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.7 - 102 km WSW of Craig, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-134.5858, 55.0558, 11.5]}, 'id': 'ak021bl2byl3'}, {'type': 'Feature', 'properties': {'mag': 4.7, 'place': '137 km WSW of Puerto Santa, Peru', 'time': 1631210306235, 'updated': 1631219616040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9sk', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9sk.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 340, 'net': 'us', 'code': '7000f9sk', 'ids': ',us7000f9sk,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 3.643, 'rms': 0.7, 'gap': 139, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.7 - 137 km WSW of Puerto Santa, Peru'}, 'geometry': {'type': 'Point', 'coordinates': [-79.7037, -9.6552, 44.05]}, 'id': 'us7000f9sk'}, {'type': 'Feature', 'properties': {'mag': 4.5, 'place': '27 km N of Yigo Village, Guam', 'time': 1631208212380, 'updated': 1631252213304, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9sj', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9sj.geojson', 'felt': 3, 'cdi': 3.1, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 312, 'net': 'us', 'code': '7000f9sj', 'ids': ',us7000f9sj,', 'sources': ',us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': 14.863, 'rms': 0.62, 'gap': 67, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.5 - 27 km N of Yigo Village, Guam'}, 'geometry': {'type': 'Point', 'coordinates': [144.9313, 13.7852, 126.62]}, 'id': 'us7000f9sj'}, {'type': 'Feature', 'properties': {'mag': 4.6, 'place': 'West Chile Rise', 'time': 1631204843314, 'updated': 1631207240040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9r9', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9r9.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 326, 'net': 'us', 'code': '7000f9r9', 'ids': ',us7000f9r9,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 16.536, 'rms': 0.62, 'gap': 248, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.6 - West Chile Rise'}, 'geometry': {'type': 'Point', 'coordinates': [-93.9273, -37.9316, 10]}, 'id': 'us7000f9r9'}, {'type': 'Feature', 'properties': {'mag': 2.8, 'place': '26km SSW of Smith Valley, NV', 'time': 1631204524730, 'updated': 1631241744852, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73622686', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622686.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 121, 'net': 'nc', 'code': '73622686', 'ids': ',nc73622686,nn00821782,', 'sources': ',nc,nn,', 'types': ',nearby-cities,origin,phase-data,scitech-link,', 'nst': 8, 'dmin': 0.05829, 'rms': 0.07, 'gap': 122, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.8 - 26km SSW of Smith Valley, NV'}, 'geometry': {'type': 'Point', 'coordinates': [-119.4205017, 38.5610008, 1.08]}, 'id': 'nc73622686'}, {'type': 'Feature', 'properties': {'mag': 3.61, 'place': '94 km N of Cruz Bay, U.S. Virgin Islands', 'time': 1631203801880, 'updated': 1631206456741, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252004', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252004.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 200, 'net': 'pr', 'code': '2021252004', 'ids': ',pr2021252004,', 'sources': ',pr,', 'types': ',origin,phase-data,', 'nst': 10, 'dmin': 1.0767, 'rms': 0.38, 'gap': 326, 'magType': 'md', 'type': 'earthquake', 'title': 'M 3.6 - 94 km N of Cruz Bay, U.S. Virgin Islands'}, 'geometry': {'type': 'Point', 'coordinates': [-64.6421, 19.1731, 34]}, 'id': 'pr2021252004'}, {'type': 'Feature', 'properties': {'mag': 2.59, 'place': '5km NNE of Fontana, CA', 'time': 1631199684820, 'updated': 1631232896077, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ci40037896', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40037896.geojson', 'felt': 15, 'cdi': 3.1, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 108, 'net': 'ci', 'code': '40037896', 'ids': ',ci40037896,us7000f9p9,', 'sources': ',ci,us,', 'types': ',dyfi,focal-mechanism,nearby-cities,origin,phase-data,scitech-link,', 'nst': 128, 'dmin': 0.0386, 'rms': 0.19, 'gap': 19, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.6 - 5km NNE of Fontana, CA'}, 'geometry': {'type': 'Point', 'coordinates': [-117.4456667, 34.1378333, 7.33]}, 'id': 'ci40037896'}, {'type': 'Feature', 'properties': {'mag': 2.7, 'place': '25 km SW of Jal, New Mexico', 'time': 1631198874103, 'updated': 1631216999217, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/tx2021rrso', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/tx2021rrso.geojson', 'felt': 0, 'cdi': 1, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 112, 'net': 'tx', 'code': '2021rrso', 'ids': ',tx2021rrso,us7000f9p4,', 'sources': ',tx,us,', 'types': ',dyfi,origin,phase-data,', 'nst': 11, 'dmin': 0.2273324505, 'rms': 0.1, 'gap': 73, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.7 - 25 km SW of Jal, New Mexico'}, 'geometry': {'type': 'Point', 'coordinates': [-103.3764106, 31.94321918, 8.213916016]}, 'id': 'tx2021rrso'}, {'type': 'Feature', 'properties': {'mag': 2.8, 'place': '62 km SSW of Kaktovik, Alaska', 'time': 1631198050002, 'updated': 1631211777040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkzyu14', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkzyu14.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 121, 'net': 'ak', 'code': '021bkzyu14', 'ids': ',us7000f9p1,ak021bkzyu14,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.52, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.8 - 62 km SSW of Kaktovik, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-144.0757, 69.5984, 8.5]}, 'id': 'ak021bkzyu14'}, {'type': 'Feature', 'properties': {'mag': 3.32, 'place': '26km SSW of Smith Valley, NV', 'time': 1631197674070, 'updated': 1631241696441, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73622621', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622621.geojson', 'felt': 2, 'cdi': 2, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 170, 'net': 'nc', 'code': '73622621', 'ids': ',nc73622621,nn00821756,us7000f9nz,', 'sources': ',nc,nn,us,', 'types': ',dyfi,focal-mechanism,nearby-cities,origin,phase-data,scitech-link,', 'nst': 14, 'dmin': 0.05439, 'rms': 0.07, 'gap': 112, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.3 - 26km SSW of Smith Valley, NV'}, 'geometry': {'type': 'Point', 'coordinates': [-119.4169998, 38.5561676, 2.21]}, 'id': 'nc73622621'}, {'type': 'Feature', 'properties': {'mag': 2.6, 'place': '73 km S of Kaktovik, Alaska', 'time': 1631197185135, 'updated': 1631211152040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkzvowj', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkzvowj.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 104, 'net': 'ak', 'code': '021bkzvowj', 'ids': ',us7000f9nx,ak021bkzvowj,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.88, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.6 - 73 km S of Kaktovik, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-143.4635, 69.4772, 0]}, 'id': 'ak021bkzvowj'}, {'type': 'Feature', 'properties': {'mag': 3.4, 'place': '7 km W of Sahiwal, Pakistan', 'time': 1631194024336, 'updated': 1631221074470, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9u0', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9u0.geojson', 'felt': 2, 'cdi': 2, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 178, 'net': 'us', 'code': '7000f9u0', 'ids': ',us7000f9u0,', 'sources': ',us,', 'types': ',dyfi,origin,phase-data,', 'nst': None, 'dmin': 1.877, 'rms': 0.75, 'gap': 285, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 3.4 - 7 km W of Sahiwal, Pakistan'}, 'geometry': {'type': 'Point', 'coordinates': [72.2567, 31.9732, 10]}, 'id': 'us7000f9u0'}, {'type': 'Feature', 'properties': {'mag': 2.5, 'place': '53 km N of Petersville, Alaska', 'time': 1631193307930, 'updated': 1631201470040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkz9bls', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkz9bls.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 96, 'net': 'ak', 'code': '021bkz9bls', 'ids': ',us7000f9ng,ak021bkz9bls,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.48, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.5 - 53 km N of Petersville, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-150.9256, 62.9704, 111.8]}, 'id': 'ak021bkz9bls'}, {'type': 'Feature', 'properties': {'mag': 5.1, 'place': 'South Sandwich Islands region', 'time': 1631192342435, 'updated': 1631193514040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9ne', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9ne.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 400, 'net': 'us', 'code': '7000f9ne', 'ids': ',us7000f9ne,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 7.949, 'rms': 0.89, 'gap': 118, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 5.1 - South Sandwich Islands region'}, 'geometry': {'type': 'Point', 'coordinates': [-25.3618, -59.3747, 46.39]}, 'id': 'us7000f9ne'}, {'type': 'Feature', 'properties': {'mag': 4.1, 'place': 'Fiji region', 'time': 1631186537077, 'updated': 1631188411040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9n2', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9n2.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 259, 'net': 'us', 'code': '7000f9n2', 'ids': ',us7000f9n2,', 'sources': ',us,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': 4.292, 'rms': 0.93, 'gap': 110, 'magType': 'mb', 'type': 'earthquake', 'title': 'M 4.1 - Fiji region'}, 'geometry': {'type': 'Point', 'coordinates': [-178.0582, -19.9624, 568.61]}, 'id': 'us7000f9n2'}, {'type': 'Feature', 'properties': {'mag': 2.63, 'place': '0 km NE of Guánica, Puerto Rico', 'time': 1631184398880, 'updated': 1631185726597, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252003', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252003.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 106, 'net': 'pr', 'code': '2021252003', 'ids': ',pr2021252003,', 'sources': ',pr,', 'types': ',origin,phase-data,', 'nst': 12, 'dmin': 0.1419, 'rms': 0.2, 'gap': 178, 'magType': 'md', 'type': 'earthquake', 'title': 'M 2.6 - 0 km NE of Guánica, Puerto Rico'}, 'geometry': {'type': 'Point', 'coordinates': [-66.9025, 17.9763, 10]}, 'id': 'pr2021252003'}, {'type': 'Feature', 'properties': {'mag': 2.5, 'place': '72 km SSE of King Salmon, Alaska', 'time': 1631182742991, 'updated': 1631192706040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkxhv5m', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkxhv5m.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 96, 'net': 'ak', 'code': '021bkxhv5m', 'ids': ',us7000f9mt,ak021bkxhv5m,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.87, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 2.5 - 72 km SSE of King Salmon, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-156.1168, 58.1075, 127.1]}, 'id': 'ak021bkxhv5m'}, {'type': 'Feature', 'properties': {'mag': 3, 'place': '55 km NNW of Yakutat, Alaska', 'time': 1631181919921, 'updated': 1631191279040, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkxewme', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkxewme.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 138, 'net': 'ak', 'code': '021bkxewme', 'ids': ',us7000f9mr,ak021bkxewme,', 'sources': ',us,ak,', 'types': ',origin,phase-data,', 'nst': None, 'dmin': None, 'rms': 0.85, 'gap': None, 'magType': 'ml', 'type': 'earthquake', 'title': 'M 3.0 - 55 km NNW of Yakutat, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-140.1872, 59.9828, 4.4]}, 'id': 'ak021bkxewme'}], 'bbox': [-178.6636, -59.3747, 0, 178.4356, 69.5984, 618.5]}
    

But is it not nice to have it like the above, so we format it to be easier to read:


```python
formatted_json = json.dumps(json_response, sort_keys=False, indent=2)

print(formatted_json)
```

    {
      "type": "FeatureCollection",
      "metadata": {
        "generated": 1631265635000,
        "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson",
        "title": "USGS Magnitude 2.5+ Earthquakes, Past Day",
        "status": 200,
        "api": "1.10.3",
        "count": 51
      },
      "features": [
        {
          "type": "Feature",
          "properties": {
            "mag": 4.3,
            "place": "138 km SE of Mil\u2019kovo, Russia",
            "time": 1631263194816,
            "updated": 1631264289040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9xw",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9xw.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 284,
            "net": "us",
            "code": "7000f9xw",
            "ids": ",us7000f9xw,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 1.346,
            "rms": 0.58,
            "gap": 148,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.3 - 138 km SE of Mil\u2019kovo, Russia"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              160.3091,
              53.9318,
              73.46
            ]
          },
          "id": "us7000f9xw"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.48,
            "place": "13km WSW of The Geysers, CA",
            "time": 1631261981930,
            "updated": 1631262283849,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc73623001",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73623001.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 95,
            "net": "nc",
            "code": "73623001",
            "ids": ",nc73623001,",
            "sources": ",nc,",
            "types": ",nearby-cities,origin,phase-data,",
            "nst": 7,
            "dmin": 0.08681,
            "rms": 0.22,
            "gap": 166,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.5 - 13km WSW of The Geysers, CA"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -122.8926697,
              38.7291679,
              4.38
            ]
          },
          "id": "nc73623001"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.1,
            "place": "57 km NNW of Yakutat, Alaska",
            "time": 1631260329152,
            "updated": 1631261097040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmjg046",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmjg046.geojson",
            "felt": 1,
            "cdi": 2,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 148,
            "net": "ak",
            "code": "021bmjg046",
            "ids": ",ak021bmjg046,us7000f9xh,",
            "sources": ",ak,us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.84,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.1 - 57 km NNW of Yakutat, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -140.1444,
              60.0157,
              6.8
            ]
          },
          "id": "ak021bmjg046"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.3,
            "place": "151 km S of False Pass, Alaska",
            "time": 1631259634814,
            "updated": 1631260791040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9xd",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9xd.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 168,
            "net": "us",
            "code": "7000f9xd",
            "ids": ",us7000f9xd,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 1.167,
            "rms": 0.77,
            "gap": 203,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.3 - 151 km S of False Pass, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -163.6824,
              53.5014,
              28.49
            ]
          },
          "id": "us7000f9xd"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4,
            "place": "187 km S of False Pass, Alaska",
            "time": 1631253474087,
            "updated": 1631255086040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x5",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x5.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 246,
            "net": "us",
            "code": "7000f9x5",
            "ids": ",us7000f9x5,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 1.535,
            "rms": 0.75,
            "gap": 158,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.0 - 187 km S of False Pass, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -163.4259,
              53.1666,
              15.24
            ]
          },
          "id": "us7000f9x5"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4,
            "place": "98 km ESE of Iquique, Chile",
            "time": 1631252756864,
            "updated": 1631254599049,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x1",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x1.geojson",
            "felt": 3,
            "cdi": 2.5,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 247,
            "net": "us",
            "code": "7000f9x1",
            "ids": ",us7000f9x1,",
            "sources": ",us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": 0.451,
            "rms": 1.01,
            "gap": 63,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.0 - 98 km ESE of Iquique, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -69.3082,
              -20.6219,
              87.5
            ]
          },
          "id": "us7000f9x1"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.7,
            "place": "51 km ESE of Hualien City, Taiwan",
            "time": 1631252702750,
            "updated": 1631254012040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9x2",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9x2.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 340,
            "net": "us",
            "code": "7000f9x2",
            "ids": ",us7000f9x2,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 0.561,
            "rms": 0.54,
            "gap": 96,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.7 - 51 km ESE of Hualien City, Taiwan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              122.0859,
              23.8356,
              32.7
            ]
          },
          "id": "us7000f9x2"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.3,
            "place": "24 km WNW of Clam Gulch, Alaska",
            "time": 1631251909539,
            "updated": 1631252408040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmi4pzu",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmi4pzu.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 168,
            "net": "ak",
            "code": "021bmi4pzu",
            "ids": ",us7000f9wz,ak021bmi4pzu,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.67,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.3 - 24 km WNW of Clam Gulch, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -151.7925,
              60.3186,
              62.1
            ]
          },
          "id": "ak021bmi4pzu"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.4,
            "place": "36 km S of Jurm, Afghanistan",
            "time": 1631251361104,
            "updated": 1631254776040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wy",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wy.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 298,
            "net": "us",
            "code": "7000f9wy",
            "ids": ",us7000f9wy,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 0.622,
            "rms": 0.68,
            "gap": 73,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.4 - 36 km S of Jurm, Afghanistan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              70.8408,
              36.539,
              194.11
            ]
          },
          "id": "us7000f9wy"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.1,
            "place": "West Chile Rise",
            "time": 1631247689051,
            "updated": 1631249026040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wt",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wt.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 400,
            "net": "us",
            "code": "7000f9wt",
            "ids": ",us7000f9wt,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 8.683,
            "rms": 1.26,
            "gap": 116,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 5.1 - West Chile Rise"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -83.6903,
              -42.8606,
              10
            ]
          },
          "id": "us7000f9wt"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.6,
            "place": "41 km SE of Calana, Peru",
            "time": 1631244338702,
            "updated": 1631245269040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9wf",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9wf.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 326,
            "net": "us",
            "code": "7000f9wf",
            "ids": ",us7000f9wf,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 0.413,
            "rms": 0.79,
            "gap": 94,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.6 - 41 km SE of Calana, Peru"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -69.9241,
              -18.2139,
              97.66
            ]
          },
          "id": "us7000f9wf"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.7,
            "place": "36 km NW of Deering, Alaska",
            "time": 1631243352784,
            "updated": 1631243891040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmgt26m",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmgt26m.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 112,
            "net": "ak",
            "code": "021bmgt26m",
            "ids": ",us7000f9wc,ak021bmgt26m,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.99,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.7 - 36 km NW of Deering, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -163.2264,
              66.3321,
              0
            ]
          },
          "id": "ak021bmgt26m"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.3,
            "place": "Izu Islands, Japan region",
            "time": 1631239825805,
            "updated": 1631242089040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9w2",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9w2.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 284,
            "net": "us",
            "code": "7000f9w2",
            "ids": ",us7000f9w2,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 2.059,
            "rms": 1.39,
            "gap": 108,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.3 - Izu Islands, Japan region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              139.8833,
              31.0509,
              164.41
            ]
          },
          "id": "us7000f9w2"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.7,
            "place": "87 km ESE of Katsuren-haebaru, Japan",
            "time": 1631239285981,
            "updated": 1631242317597,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9w1",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9w1.geojson",
            "felt": 1,
            "cdi": 1,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 340,
            "net": "us",
            "code": "7000f9w1",
            "ids": ",us7000f9w1,",
            "sources": ",us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": 0.809,
            "rms": 0.99,
            "gap": 77,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.7 - 87 km ESE of Katsuren-haebaru, Japan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              128.7154,
              26.1275,
              10
            ]
          },
          "id": "us7000f9w1"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.4,
            "place": "105 km SW of Bengkulu, Indonesia",
            "time": 1631238141436,
            "updated": 1631240153040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vv",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vv.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 298,
            "net": "us",
            "code": "7000f9vv",
            "ids": ",us7000f9vv,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 1.268,
            "rms": 0.57,
            "gap": 190,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.4 - 105 km SW of Bengkulu, Indonesia"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              101.7007,
              -4.5689,
              36.55
            ]
          },
          "id": "us7000f9vv"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.5,
            "place": "48 km N of Valdez, Alaska",
            "time": 1631237201581,
            "updated": 1631237964040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bmfpwdp",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bmfpwdp.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 188,
            "net": "ak",
            "code": "021bmfpwdp",
            "ids": ",us7000f9vs,ak021bmfpwdp,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.87,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.5 - 48 km N of Valdez, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -146.518,
              61.5628,
              16.5
            ]
          },
          "id": "ak021bmfpwdp"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5,
            "place": "53 km NE of Anse-Bertrand, Guadeloupe",
            "time": 1631234599179,
            "updated": 1631265427932,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vl",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vl.geojson",
            "felt": 39,
            "cdi": 4.6,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 403,
            "net": "us",
            "code": "7000f9vl",
            "ids": ",us7000f9vl,",
            "sources": ",us,",
            "types": ",dyfi,moment-tensor,origin,phase-data,",
            "nst": null,
            "dmin": 0.787,
            "rms": 0.72,
            "gap": 59,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 5.0 - 53 km NE of Anse-Bertrand, Guadeloupe"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -61.1489,
              16.8112,
              45.13
            ]
          },
          "id": "us7000f9vl"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.7,
            "place": "south of the Fiji Islands",
            "time": 1631233261422,
            "updated": 1631234326040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vi",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vi.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 340,
            "net": "us",
            "code": "7000f9vi",
            "ids": ",us7000f9vi,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 4.423,
            "rms": 1,
            "gap": 75,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.7 - south of the Fiji Islands"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              178.4356,
              -26.2276,
              618.5
            ]
          },
          "id": "us7000f9vi"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.5,
            "place": "105 km NE of Hotan, China",
            "time": 1631231315869,
            "updated": 1631232756040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9v9",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9v9.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 312,
            "net": "us",
            "code": "7000f9v9",
            "ids": ",us7000f9v9,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 5.222,
            "rms": 0.84,
            "gap": 150,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.5 - 105 km NE of Hotan, China"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              80.9206,
              37.642,
              15.2
            ]
          },
          "id": "us7000f9v9"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.6,
            "place": "85 km SW of Atka, Alaska",
            "time": 1631231042205,
            "updated": 1631232916040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9vd",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9vd.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 199,
            "net": "us",
            "code": "7000f9vd",
            "ids": ",ak021bl5dv3j,us7000f9vd,",
            "sources": ",ak,us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 0.588,
            "rms": 0.45,
            "gap": 228,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.6 - 85 km SW of Atka, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -175.1182,
              51.679,
              49.58
            ]
          },
          "id": "us7000f9vd"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.5,
            "place": "29 km SE of Jurm, Afghanistan",
            "time": 1631230995638,
            "updated": 1631232478040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9v7",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9v7.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 312,
            "net": "us",
            "code": "7000f9v7",
            "ids": ",us7000f9v7,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 0.595,
            "rms": 0.6,
            "gap": 70,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.5 - 29 km SE of Jurm, Afghanistan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              71.0717,
              36.6812,
              214.18
            ]
          },
          "id": "us7000f9v7"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.12,
            "place": "0 km NNE of Central Aguirre, Puerto Rico",
            "time": 1631226713140,
            "updated": 1631235906684,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252012",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252012.geojson",
            "felt": 2,
            "cdi": 3.4,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 150,
            "net": "pr",
            "code": "2021252012",
            "ids": ",pr2021252012,",
            "sources": ",pr,",
            "types": ",dyfi,origin,phase-data,",
            "nst": 9,
            "dmin": 0.1153,
            "rms": 0.11,
            "gap": 199,
            "magType": "md",
            "type": "earthquake",
            "title": "M 3.1 - 0 km NNE of Central Aguirre, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -66.2218,
              17.9563,
              12
            ]
          },
          "id": "pr2021252012"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.32,
            "place": "10km SW of Petrolia, CA",
            "time": 1631224676520,
            "updated": 1631260873897,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc73622771",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622771.geojson",
            "felt": 34,
            "cdi": 3.4,
            "mmi": 2.978,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 299,
            "net": "nc",
            "code": "73622771",
            "ids": ",nc73622771,us7000f9um,",
            "sources": ",nc,us,",
            "types": ",dyfi,focal-mechanism,losspager,moment-tensor,nearby-cities,origin,phase-data,scitech-link,shakemap,",
            "nst": 23,
            "dmin": 0.03464,
            "rms": 0.11,
            "gap": 229,
            "magType": "mw",
            "type": "earthquake",
            "title": "M 4.3 - 10km SW of Petrolia, CA"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -124.3813333,
              40.2705,
              32.83
            ]
          },
          "id": "nc73622771"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.5,
            "place": "218 km ENE of Levuka, Fiji",
            "time": 1631224606389,
            "updated": 1631225939040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9un",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9un.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 312,
            "net": "us",
            "code": "7000f9un",
            "ids": ",us7000f9un,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 3.131,
            "rms": 0.47,
            "gap": 118,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.5 - 218 km ENE of Levuka, Fiji"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -178.6636,
              -17.6588,
              558.09
            ]
          },
          "id": "us7000f9un"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.2,
            "place": "off the coast of Oregon",
            "time": 1631223714848,
            "updated": 1631235018586,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9ug",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9ug.geojson",
            "felt": 1,
            "cdi": 2,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 158,
            "net": "us",
            "code": "7000f9ug",
            "ids": ",us7000f9ug,",
            "sources": ",us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": 1.901,
            "rms": 0.63,
            "gap": 207,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.2 - off the coast of Oregon"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -128.6559,
              44.0804,
              10
            ]
          },
          "id": "us7000f9ug"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.76,
            "place": "4 km SSE of Gu\u00e1nica, Puerto Rico",
            "time": 1631223455590,
            "updated": 1631225208721,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252008",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252008.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 117,
            "net": "pr",
            "code": "2021252008",
            "ids": ",pr2021252008,",
            "sources": ",pr,",
            "types": ",origin,phase-data,",
            "nst": 14,
            "dmin": 0.1591,
            "rms": 0.19,
            "gap": 217,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.8 - 4 km SSE of Gu\u00e1nica, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -66.8893,
              17.933,
              8
            ]
          },
          "id": "pr2021252008"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.49,
            "place": "4 km SSE of Gu\u00e1nica, Puerto Rico",
            "time": 1631223240640,
            "updated": 1631235660530,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252009",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252009.geojson",
            "felt": 1,
            "cdi": 3.1,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 96,
            "net": "pr",
            "code": "2021252009",
            "ids": ",pr2021252009,",
            "sources": ",pr,",
            "types": ",dyfi,origin,phase-data,",
            "nst": 19,
            "dmin": 0.1608,
            "rms": 0.1,
            "gap": 197,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.5 - 4 km SSE of Gu\u00e1nica, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -66.8875,
              17.9335,
              8
            ]
          },
          "id": "pr2021252009"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.6,
            "place": "64 km SE of Denali National Park, Alaska",
            "time": 1631222145650,
            "updated": 1631224866130,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bl40vdu",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bl40vdu.geojson",
            "felt": 1,
            "cdi": 3.4,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 104,
            "net": "ak",
            "code": "021bl40vdu",
            "ids": ",ak021bl40vdu,us7000f9u7,",
            "sources": ",ak,us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.46,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.6 - 64 km SE of Denali National Park, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -150.8869,
              63.0995,
              120.8
            ]
          },
          "id": "ak021bl40vdu"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.68,
            "place": "26 km NW of Rinc\u00f3n, Puerto Rico",
            "time": 1631221855060,
            "updated": 1631222739694,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252007",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252007.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 110,
            "net": "pr",
            "code": "2021252007",
            "ids": ",pr2021252007,",
            "sources": ",pr,",
            "types": ",origin,phase-data,",
            "nst": 5,
            "dmin": 0.324,
            "rms": 0.16,
            "gap": 309,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.7 - 26 km NW of Rinc\u00f3n, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -67.4323,
              18.5105,
              6
            ]
          },
          "id": "pr2021252007"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.18,
            "place": "4 km SSE of Gu\u00e1nica, Puerto Rico",
            "time": 1631219603990,
            "updated": 1631221087337,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252006",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252006.geojson",
            "felt": 1,
            "cdi": 2.2,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 156,
            "net": "pr",
            "code": "2021252006",
            "ids": ",pr2021252006,us7000f9tv,",
            "sources": ",pr,us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": 22,
            "dmin": 0.1549,
            "rms": 0.2,
            "gap": 196,
            "magType": "md",
            "type": "earthquake",
            "title": "M 3.2 - 4 km SSE of Gu\u00e1nica, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -66.8928,
              17.9368,
              7
            ]
          },
          "id": "pr2021252006"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.86,
            "place": "8 km W of Hormigueros, Puerto Rico",
            "time": 1631215542980,
            "updated": 1631217369864,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252005",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252005.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 126,
            "net": "pr",
            "code": "2021252005",
            "ids": ",pr2021252005,",
            "sources": ",pr,",
            "types": ",origin,phase-data,",
            "nst": 12,
            "dmin": 0.1736,
            "rms": 0.11,
            "gap": 167,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.9 - 8 km W of Hormigueros, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -67.206,
              18.1508,
              11
            ]
          },
          "id": "pr2021252005"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.1,
            "place": "Unimak Island region, Alaska",
            "time": 1631215405350,
            "updated": 1631259213016,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9t5",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9t5.geojson",
            "felt": 2,
            "cdi": 1,
            "mmi": 1.826,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 400,
            "net": "us",
            "code": "7000f9t5",
            "ids": ",us7000f9t5,ak021bl2vo50,",
            "sources": ",us,ak,",
            "types": ",dyfi,oaf,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 1.179,
            "rms": 0.84,
            "gap": 148,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 5.1 - Unimak Island region, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -163.5308,
              53.4726,
              21.48
            ]
          },
          "id": "us7000f9t5"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.8,
            "place": "292 km W of Bandon, Oregon",
            "time": 1631213883277,
            "updated": 1631220542040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9t0",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9t0.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 121,
            "net": "us",
            "code": "7000f9t0",
            "ids": ",us7000f9t0,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 2.077,
            "rms": 0.57,
            "gap": 291,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.8 - 292 km W of Bandon, Oregon"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -127.967,
              43.5592,
              10
            ]
          },
          "id": "us7000f9t0"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.7,
            "place": "102 km WSW of Craig, Alaska",
            "time": 1631212277953,
            "updated": 1631220115040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bl2byl3",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bl2byl3.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 112,
            "net": "ak",
            "code": "021bl2byl3",
            "ids": ",us7000f9sv,ak021bl2byl3,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.43,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.7 - 102 km WSW of Craig, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -134.5858,
              55.0558,
              11.5
            ]
          },
          "id": "ak021bl2byl3"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.7,
            "place": "137 km WSW of Puerto Santa, Peru",
            "time": 1631210306235,
            "updated": 1631219616040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9sk",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9sk.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 340,
            "net": "us",
            "code": "7000f9sk",
            "ids": ",us7000f9sk,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 3.643,
            "rms": 0.7,
            "gap": 139,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.7 - 137 km WSW of Puerto Santa, Peru"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -79.7037,
              -9.6552,
              44.05
            ]
          },
          "id": "us7000f9sk"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.5,
            "place": "27 km N of Yigo Village, Guam",
            "time": 1631208212380,
            "updated": 1631252213304,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9sj",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9sj.geojson",
            "felt": 3,
            "cdi": 3.1,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 312,
            "net": "us",
            "code": "7000f9sj",
            "ids": ",us7000f9sj,",
            "sources": ",us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": 14.863,
            "rms": 0.62,
            "gap": 67,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.5 - 27 km N of Yigo Village, Guam"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              144.9313,
              13.7852,
              126.62
            ]
          },
          "id": "us7000f9sj"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.6,
            "place": "West Chile Rise",
            "time": 1631204843314,
            "updated": 1631207240040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9r9",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9r9.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 326,
            "net": "us",
            "code": "7000f9r9",
            "ids": ",us7000f9r9,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 16.536,
            "rms": 0.62,
            "gap": 248,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.6 - West Chile Rise"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -93.9273,
              -37.9316,
              10
            ]
          },
          "id": "us7000f9r9"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.8,
            "place": "26km SSW of Smith Valley, NV",
            "time": 1631204524730,
            "updated": 1631241744852,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc73622686",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622686.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 121,
            "net": "nc",
            "code": "73622686",
            "ids": ",nc73622686,nn00821782,",
            "sources": ",nc,nn,",
            "types": ",nearby-cities,origin,phase-data,scitech-link,",
            "nst": 8,
            "dmin": 0.05829,
            "rms": 0.07,
            "gap": 122,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.8 - 26km SSW of Smith Valley, NV"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -119.4205017,
              38.5610008,
              1.08
            ]
          },
          "id": "nc73622686"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.61,
            "place": "94 km N of Cruz Bay, U.S. Virgin Islands",
            "time": 1631203801880,
            "updated": 1631206456741,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252004",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252004.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 200,
            "net": "pr",
            "code": "2021252004",
            "ids": ",pr2021252004,",
            "sources": ",pr,",
            "types": ",origin,phase-data,",
            "nst": 10,
            "dmin": 1.0767,
            "rms": 0.38,
            "gap": 326,
            "magType": "md",
            "type": "earthquake",
            "title": "M 3.6 - 94 km N of Cruz Bay, U.S. Virgin Islands"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -64.6421,
              19.1731,
              34
            ]
          },
          "id": "pr2021252004"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.59,
            "place": "5km NNE of Fontana, CA",
            "time": 1631199684820,
            "updated": 1631232896077,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci40037896",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci40037896.geojson",
            "felt": 15,
            "cdi": 3.1,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 108,
            "net": "ci",
            "code": "40037896",
            "ids": ",ci40037896,us7000f9p9,",
            "sources": ",ci,us,",
            "types": ",dyfi,focal-mechanism,nearby-cities,origin,phase-data,scitech-link,",
            "nst": 128,
            "dmin": 0.0386,
            "rms": 0.19,
            "gap": 19,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.6 - 5km NNE of Fontana, CA"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -117.4456667,
              34.1378333,
              7.33
            ]
          },
          "id": "ci40037896"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.7,
            "place": "25 km SW of Jal, New Mexico",
            "time": 1631198874103,
            "updated": 1631216999217,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/tx2021rrso",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/tx2021rrso.geojson",
            "felt": 0,
            "cdi": 1,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 112,
            "net": "tx",
            "code": "2021rrso",
            "ids": ",tx2021rrso,us7000f9p4,",
            "sources": ",tx,us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": 11,
            "dmin": 0.2273324505,
            "rms": 0.1,
            "gap": 73,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.7 - 25 km SW of Jal, New Mexico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -103.3764106,
              31.94321918,
              8.213916016
            ]
          },
          "id": "tx2021rrso"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.8,
            "place": "62 km SSW of Kaktovik, Alaska",
            "time": 1631198050002,
            "updated": 1631211777040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkzyu14",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkzyu14.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 121,
            "net": "ak",
            "code": "021bkzyu14",
            "ids": ",us7000f9p1,ak021bkzyu14,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.52,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.8 - 62 km SSW of Kaktovik, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -144.0757,
              69.5984,
              8.5
            ]
          },
          "id": "ak021bkzyu14"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.32,
            "place": "26km SSW of Smith Valley, NV",
            "time": 1631197674070,
            "updated": 1631241696441,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc73622621",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73622621.geojson",
            "felt": 2,
            "cdi": 2,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 170,
            "net": "nc",
            "code": "73622621",
            "ids": ",nc73622621,nn00821756,us7000f9nz,",
            "sources": ",nc,nn,us,",
            "types": ",dyfi,focal-mechanism,nearby-cities,origin,phase-data,scitech-link,",
            "nst": 14,
            "dmin": 0.05439,
            "rms": 0.07,
            "gap": 112,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.3 - 26km SSW of Smith Valley, NV"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -119.4169998,
              38.5561676,
              2.21
            ]
          },
          "id": "nc73622621"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.6,
            "place": "73 km S of Kaktovik, Alaska",
            "time": 1631197185135,
            "updated": 1631211152040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkzvowj",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkzvowj.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 104,
            "net": "ak",
            "code": "021bkzvowj",
            "ids": ",us7000f9nx,ak021bkzvowj,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.88,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.6 - 73 km S of Kaktovik, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -143.4635,
              69.4772,
              0
            ]
          },
          "id": "ak021bkzvowj"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3.4,
            "place": "7 km W of Sahiwal, Pakistan",
            "time": 1631194024336,
            "updated": 1631221074470,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9u0",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9u0.geojson",
            "felt": 2,
            "cdi": 2,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 178,
            "net": "us",
            "code": "7000f9u0",
            "ids": ",us7000f9u0,",
            "sources": ",us,",
            "types": ",dyfi,origin,phase-data,",
            "nst": null,
            "dmin": 1.877,
            "rms": 0.75,
            "gap": 285,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 3.4 - 7 km W of Sahiwal, Pakistan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              72.2567,
              31.9732,
              10
            ]
          },
          "id": "us7000f9u0"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.5,
            "place": "53 km N of Petersville, Alaska",
            "time": 1631193307930,
            "updated": 1631201470040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkz9bls",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkz9bls.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 96,
            "net": "ak",
            "code": "021bkz9bls",
            "ids": ",us7000f9ng,ak021bkz9bls,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.48,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.5 - 53 km N of Petersville, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -150.9256,
              62.9704,
              111.8
            ]
          },
          "id": "ak021bkz9bls"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.1,
            "place": "South Sandwich Islands region",
            "time": 1631192342435,
            "updated": 1631193514040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9ne",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9ne.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 400,
            "net": "us",
            "code": "7000f9ne",
            "ids": ",us7000f9ne,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 7.949,
            "rms": 0.89,
            "gap": 118,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 5.1 - South Sandwich Islands region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -25.3618,
              -59.3747,
              46.39
            ]
          },
          "id": "us7000f9ne"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 4.1,
            "place": "Fiji region",
            "time": 1631186537077,
            "updated": 1631188411040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000f9n2",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000f9n2.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 259,
            "net": "us",
            "code": "7000f9n2",
            "ids": ",us7000f9n2,",
            "sources": ",us,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": 4.292,
            "rms": 0.93,
            "gap": 110,
            "magType": "mb",
            "type": "earthquake",
            "title": "M 4.1 - Fiji region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -178.0582,
              -19.9624,
              568.61
            ]
          },
          "id": "us7000f9n2"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.63,
            "place": "0 km NE of Gu\u00e1nica, Puerto Rico",
            "time": 1631184398880,
            "updated": 1631185726597,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2021252003",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/pr2021252003.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 106,
            "net": "pr",
            "code": "2021252003",
            "ids": ",pr2021252003,",
            "sources": ",pr,",
            "types": ",origin,phase-data,",
            "nst": 12,
            "dmin": 0.1419,
            "rms": 0.2,
            "gap": 178,
            "magType": "md",
            "type": "earthquake",
            "title": "M 2.6 - 0 km NE of Gu\u00e1nica, Puerto Rico"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -66.9025,
              17.9763,
              10
            ]
          },
          "id": "pr2021252003"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 2.5,
            "place": "72 km SSE of King Salmon, Alaska",
            "time": 1631182742991,
            "updated": 1631192706040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkxhv5m",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkxhv5m.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 96,
            "net": "ak",
            "code": "021bkxhv5m",
            "ids": ",us7000f9mt,ak021bkxhv5m,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.87,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 2.5 - 72 km SSE of King Salmon, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -156.1168,
              58.1075,
              127.1
            ]
          },
          "id": "ak021bkxhv5m"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 3,
            "place": "55 km NNW of Yakutat, Alaska",
            "time": 1631181919921,
            "updated": 1631191279040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ak021bkxewme",
            "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak021bkxewme.geojson",
            "felt": null,
            "cdi": null,
            "mmi": null,
            "alert": null,
            "status": "automatic",
            "tsunami": 0,
            "sig": 138,
            "net": "ak",
            "code": "021bkxewme",
            "ids": ",us7000f9mr,ak021bkxewme,",
            "sources": ",us,ak,",
            "types": ",origin,phase-data,",
            "nst": null,
            "dmin": null,
            "rms": 0.85,
            "gap": null,
            "magType": "ml",
            "type": "earthquake",
            "title": "M 3.0 - 55 km NNW of Yakutat, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -140.1872,
              59.9828,
              4.4
            ]
          },
          "id": "ak021bkxewme"
        }
      ],
      "bbox": [
        -178.6636,
        -59.3747,
        0,
        178.4356,
        69.5984,
        618.5
      ]
    }
    


```python
max_magnitude = 0
max_long = 0
max_lat = 0
for earthquake in json_response["features"]:
    magnitude = earthquake["properties"]["mag"]
    print("----")
    print("Place:  " + earthquake["properties"]["place"])
    tt = earthquake["properties"]["time"]//1000
    print("Time:  " + str(datetime.fromtimestamp(tt).strftime("%Y-%m-%d %I:%M:%S")))    
    print("Mag:  " + str(magnitude))
    if (magnitude > max_magnitude):
        max_magnitude = magnitude
        max_long = earthquake["geometry"]["coordinates"][0]
        max_lat = earthquake["geometry"]["coordinates"][1]

print ("\nMaximum magnitude: " + str(max_magnitude))
print("\nLocation: "+str(max_long),str(max_lat))
```

    ----
    Place:  138 km SE of Mil’kovo, Russia
    Time:  2021-09-10 12:39:54
    Mag:  4.3
    ----
    Place:  13km WSW of The Geysers, CA
    Time:  2021-09-10 12:19:41
    Mag:  2.48
    ----
    Place:  57 km NNW of Yakutat, Alaska
    Time:  2021-09-10 11:52:09
    Mag:  3.1
    ----
    Place:  151 km S of False Pass, Alaska
    Time:  2021-09-10 11:40:34
    Mag:  3.3
    ----
    Place:  187 km S of False Pass, Alaska
    Time:  2021-09-10 09:57:54
    Mag:  4
    ----
    Place:  98 km ESE of Iquique, Chile
    Time:  2021-09-10 09:45:56
    Mag:  4
    ----
    Place:  51 km ESE of Hualien City, Taiwan
    Time:  2021-09-10 09:45:02
    Mag:  4.7
    ----
    Place:  24 km WNW of Clam Gulch, Alaska
    Time:  2021-09-10 09:31:49
    Mag:  3.3
    ----
    Place:  36 km S of Jurm, Afghanistan
    Time:  2021-09-10 09:22:41
    Mag:  4.4
    ----
    Place:  West Chile Rise
    Time:  2021-09-10 08:21:29
    Mag:  5.1
    ----
    Place:  41 km SE of Calana, Peru
    Time:  2021-09-10 07:25:38
    Mag:  4.6
    ----
    Place:  36 km NW of Deering, Alaska
    Time:  2021-09-10 07:09:12
    Mag:  2.7
    ----
    Place:  Izu Islands, Japan region
    Time:  2021-09-10 06:10:25
    Mag:  4.3
    ----
    Place:  87 km ESE of Katsuren-haebaru, Japan
    Time:  2021-09-10 06:01:25
    Mag:  4.7
    ----
    Place:  105 km SW of Bengkulu, Indonesia
    Time:  2021-09-10 05:42:21
    Mag:  4.4
    ----
    Place:  48 km N of Valdez, Alaska
    Time:  2021-09-10 05:26:41
    Mag:  3.5
    ----
    Place:  53 km NE of Anse-Bertrand, Guadeloupe
    Time:  2021-09-10 04:43:19
    Mag:  5
    ----
    Place:  south of the Fiji Islands
    Time:  2021-09-10 04:21:01
    Mag:  4.7
    ----
    Place:  105 km NE of Hotan, China
    Time:  2021-09-10 03:48:35
    Mag:  4.5
    ----
    Place:  85 km SW of Atka, Alaska
    Time:  2021-09-10 03:44:02
    Mag:  3.6
    ----
    Place:  29 km SE of Jurm, Afghanistan
    Time:  2021-09-10 03:43:15
    Mag:  4.5
    ----
    Place:  0 km NNE of Central Aguirre, Puerto Rico
    Time:  2021-09-10 02:31:53
    Mag:  3.12
    ----
    Place:  10km SW of Petrolia, CA
    Time:  2021-09-10 01:57:56
    Mag:  4.32
    ----
    Place:  218 km ENE of Levuka, Fiji
    Time:  2021-09-10 01:56:46
    Mag:  4.5
    ----
    Place:  off the coast of Oregon
    Time:  2021-09-10 01:41:54
    Mag:  3.2
    ----
    Place:  4 km SSE of Guánica, Puerto Rico
    Time:  2021-09-10 01:37:35
    Mag:  2.76
    ----
    Place:  4 km SSE of Guánica, Puerto Rico
    Time:  2021-09-10 01:34:00
    Mag:  2.49
    ----
    Place:  64 km SE of Denali National Park, Alaska
    Time:  2021-09-10 01:15:45
    Mag:  2.6
    ----
    Place:  26 km NW of Rincón, Puerto Rico
    Time:  2021-09-10 01:10:55
    Mag:  2.68
    ----
    Place:  4 km SSE of Guánica, Puerto Rico
    Time:  2021-09-10 12:33:23
    Mag:  3.18
    ----
    Place:  8 km W of Hormigueros, Puerto Rico
    Time:  2021-09-09 11:25:42
    Mag:  2.86
    ----
    Place:  Unimak Island region, Alaska
    Time:  2021-09-09 11:23:25
    Mag:  5.1
    ----
    Place:  292 km W of Bandon, Oregon
    Time:  2021-09-09 10:58:03
    Mag:  2.8
    ----
    Place:  102 km WSW of Craig, Alaska
    Time:  2021-09-09 10:31:17
    Mag:  2.7
    ----
    Place:  137 km WSW of Puerto Santa, Peru
    Time:  2021-09-09 09:58:26
    Mag:  4.7
    ----
    Place:  27 km N of Yigo Village, Guam
    Time:  2021-09-09 09:23:32
    Mag:  4.5
    ----
    Place:  West Chile Rise
    Time:  2021-09-09 08:27:23
    Mag:  4.6
    ----
    Place:  26km SSW of Smith Valley, NV
    Time:  2021-09-09 08:22:04
    Mag:  2.8
    ----
    Place:  94 km N of Cruz Bay, U.S. Virgin Islands
    Time:  2021-09-09 08:10:01
    Mag:  3.61
    ----
    Place:  5km NNE of Fontana, CA
    Time:  2021-09-09 07:01:24
    Mag:  2.59
    ----
    Place:  25 km SW of Jal, New Mexico
    Time:  2021-09-09 06:47:54
    Mag:  2.7
    ----
    Place:  62 km SSW of Kaktovik, Alaska
    Time:  2021-09-09 06:34:10
    Mag:  2.8
    ----
    Place:  26km SSW of Smith Valley, NV
    Time:  2021-09-09 06:27:54
    Mag:  3.32
    ----
    Place:  73 km S of Kaktovik, Alaska
    Time:  2021-09-09 06:19:45
    Mag:  2.6
    ----
    Place:  7 km W of Sahiwal, Pakistan
    Time:  2021-09-09 05:27:04
    Mag:  3.4
    ----
    Place:  53 km N of Petersville, Alaska
    Time:  2021-09-09 05:15:07
    Mag:  2.5
    ----
    Place:  South Sandwich Islands region
    Time:  2021-09-09 04:59:02
    Mag:  5.1
    ----
    Place:  Fiji region
    Time:  2021-09-09 03:22:17
    Mag:  4.1
    ----
    Place:  0 km NE of Guánica, Puerto Rico
    Time:  2021-09-09 02:46:38
    Mag:  2.63
    ----
    Place:  72 km SSE of King Salmon, Alaska
    Time:  2021-09-09 02:19:02
    Mag:  2.5
    ----
    Place:  55 km NNW of Yakutat, Alaska
    Time:  2021-09-09 02:05:19
    Mag:  3
    
    Maximum magnitude: 5.1
    
    Location: -83.6903 -42.8606
    

converting time, note the digits:


```python
time = 1631276869
datetime.fromtimestamp(1631276869).strftime("%Y-%m-%d %I:%M:%S")

```




    '2021-09-10 04:27:49'




```python
# print only the events where at least 1 person reported feeling something
print("\n\nEvents that were felt:")
for earthquake in json_response["features"]:
        feltReports = earthquake["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0):
                print("%2.1f" % earthquake["properties"]["mag"], earthquake["properties"]
                      ["place"], " reported " + str(feltReports) + " times")


```

    
    
    Events that were felt:
    3.1 57 km NNW of Yakutat, Alaska  reported 1 times
    4.0 98 km ESE of Iquique, Chile  reported 3 times
    4.7 87 km ESE of Katsuren-haebaru, Japan  reported 1 times
    5.0 53 km NE of Anse-Bertrand, Guadeloupe  reported 39 times
    3.1 0 km NNE of Central Aguirre, Puerto Rico  reported 2 times
    4.3 10km SW of Petrolia, CA  reported 34 times
    3.2 off the coast of Oregon  reported 1 times
    2.5 4 km SSE of Guánica, Puerto Rico  reported 1 times
    2.6 64 km SE of Denali National Park, Alaska  reported 1 times
    3.2 4 km SSE of Guánica, Puerto Rico  reported 1 times
    5.1 Unimak Island region, Alaska  reported 2 times
    4.5 27 km N of Yigo Village, Guam  reported 3 times
    2.6 5km NNE of Fontana, CA  reported 15 times
    3.3 26km SSW of Smith Valley, NV  reported 2 times
    3.4 7 km W of Sahiwal, Pakistan  reported 2 times
    


```python
# print the events that only have a magnitude greater than 4
for earthquake in json_response["features"]:
    if earthquake["properties"]["mag"] >= 4.0:
        print("%2.1f" % earthquake["properties"]["mag"], earthquake["properties"]["place"])
```

    4.3 138 km SE of Mil’kovo, Russia
    4.0 187 km S of False Pass, Alaska
    4.0 98 km ESE of Iquique, Chile
    4.7 51 km ESE of Hualien City, Taiwan
    4.4 36 km S of Jurm, Afghanistan
    5.1 West Chile Rise
    4.6 41 km SE of Calana, Peru
    4.3 Izu Islands, Japan region
    4.7 87 km ESE of Katsuren-haebaru, Japan
    4.4 105 km SW of Bengkulu, Indonesia
    5.0 53 km NE of Anse-Bertrand, Guadeloupe
    4.7 south of the Fiji Islands
    4.5 105 km NE of Hotan, China
    4.5 29 km SE of Jurm, Afghanistan
    4.3 10km SW of Petrolia, CA
    4.5 218 km ENE of Levuka, Fiji
    5.1 Unimak Island region, Alaska
    4.7 137 km WSW of Puerto Santa, Peru
    4.5 27 km N of Yigo Village, Guam
    4.6 West Chile Rise
    5.1 South Sandwich Islands region
    4.1 Fiji region
    


```python

```


```python

```
