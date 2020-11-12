import requests
from requests.structures import CaseInsensitiveDict
import json
from time import sleep as wait
h = CaseInsensitiveDict()
loading_anim = "-"
token = input("Token: ")
cookie = input("Cookie: ")
jsonshit = {"custom_status":{"text":"{}".format(loading_anim)}}
increase = True
def change_state():
    jsonshit['custom_status'] = {"text":"{}".format(loading_anim)}
h['method'] = "PATCH"
h['path'] = '/api/v8/users/@me/settings'
h['authorization'] = "{}".format(token)
h['content-length'] = "{}".format(len(json.dumps(jsonshit)))
h['content-type'] = 'application/json'
h['cookie'] = "{}".format(cookie)
h['origin'] = 'https://discordapp.com'
h['referer'] = 'https://discordapp.com/channels/@me/'
h['x-super-properties'] = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDgiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MSIsIm9zX2FyY2giOiJ4NjQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MTQ0NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
num = 1
while True:
    wait(2)
    anim = requests.patch(url="https://discordapp.com/api/v8/users/@me/settings",headers=h,json=jsonshit)
    num = num +1
    if num > 3:
        num = 0

    if num == 0:
        loading_anim = "-"
    elif num == 1:
        loading_anim = "/"
    elif num == 2:
        loading_anim = "|"
    elif num == 3:
        loading_anim = "\\"
    change_state()
    print("[{}] {}\nState:{}".format(anim.status_code,anim.reason,loading_anim))