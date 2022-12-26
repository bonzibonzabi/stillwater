import requests
import json

url = "https://api.clashofclans.com/v1/clans/%2329CJ00YPR"

baseplayerurl = "https://api.clashofclans.com/v1/players/"

key = CREATE-YOUR-OWN-KEY


headers = {
    "Accept" : "application/json",
    "Authorization" : "Bearer %s" % key
}
response = requests.request("GET", url, headers = headers)
clan = response.json()
print(clan['tag'])
print(clan['name'])
print(clan['clanLevel'])
print(clan['members'])
#print(clan['memberList'])
print("Tag          Name             Role       Donations  WarStars    Option   ClanCapDonations")
print("-----------  ---------------  -------    ---------  --------    ------   ----------------")

for member in clan['memberList']:
    print(f"{member['tag']:13}",  end='')
    name = member['name'].replace(" ", "")
    print(f"{name:17}", end='' )
    print(f"{member['role']:8}",  end='')
    print(f"{member['donations']:12}", end='')
    playerurl = baseplayerurl + "%23" + member['tag'].strip('#')
    playerresponse = requests.request("GET", playerurl, headers = headers)
    player = playerresponse.json()
    print(f"{player['warStars']:>10}", end='')
    print(f"{player['warPreference']:>9}", end='')
    print(f"{player['clanCapitalContributions']:>19}")
