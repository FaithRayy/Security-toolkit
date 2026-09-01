import platform
import getmac
import requests
import os 
import subprocess

# get public IP address using api.ipify.org API
getIP = subprocess.run(["curl", "https://api.ipify.org"], capture_output=True, text=True)

# recieve Geolocation with ip-api.com using IP address
geoAPI = "http://ip-api.com/json/"
getpath = os.path.join(geoAPI, getIP.stdout)
response = requests.get(getpath)

json_result = response.json()

# print statements
print(f"OS: {platform.system()}")
print(f"IP address: {getIP.stdout}")
print(f"MAC Address: {getmac.get_mac_address()}")
print(f"Internet Service Provider: {json_result["isp"]}\nCity: {json_result["city"]}\nState: {json_result["regionName"]}\nCountry: {json_result["country"]}\nTimezone: {json_result["timezone"]}")
