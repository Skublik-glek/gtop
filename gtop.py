from time import sleep
import requests


all_info = {}
sorted_info = {}
print("Подождите, в последнее время API Mojang долго переводит uuid в ники...\n")
data = requests.get("https://api.hypixel.net/guild?key=<<API КЛЮЧ>>&name=<<ИМЯ ГИЛЬДИИ>>").json()["guild"]["members"]
for n, member in enumerate(data):
    try:
        name = requests.get(f"https://api.mojang.com/user/profiles/{member['uuid']}/names").json()[-1]["name"]
    except:
        try:
            sleep(3)
            name = requests.get(f"https://api.mojang.com/user/profiles/{member['uuid']}/names").json()[-1]["name"]
        except:
            name = "Ошибка перевода uuid " + str(member['uuid'])
    all_xp = 0
    for date in member["expHistory"]:
        all_xp += member["expHistory"][date]
    all_info[name] = all_xp

sorted_keys = sorted(all_info, key=all_info.get)
for w in reversed(sorted_keys):
    sorted_info[w] = all_info[w]

for n, key in enumerate(sorted_info.keys()):
    print(f"{n + 1}) {key}: {sorted_info[key]}")

water = input("\nНажмите Enter для завершения")
