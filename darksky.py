import requests
import json
import accesskey
base_url = 'https://api.darksky.net/forecast/'
api_key = accesskey.access_key
lat_lng = '42.280841,-83.738115'
full_url = base_url+api_key+'/'+lat_lng
response = requests.get(full_url)
data = json.loads(response.text)
print(json.dumps(data, indent=4))