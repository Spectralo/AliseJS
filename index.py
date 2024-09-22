import os
import requests

schoolid = ""
token = ""

if os.getenv("TOKEN","bad") == "bad":
    print("You need to export your token as a env var")
    print('On Linux/MacOS : export TOKEN="token"')
else:
    token = os.getenv("TOKEN")
    print("Token found !")
    print("Your token is : "+token)

if os.getenv("SCHOOLID","bad") == "bad":
    print("You need to export your SCHOOLID as a env var")
    print('On Linux/MacOS : export SCHOOLID="schoolid"')
else:
    schoolid = os.getenv("SCHOOLID")
    print("Schoolid found !")
    print("Your schoolid is : "+schoolid)

if token != "" and schoolid != "":
    session = requests.Session()
    r = session.get('https://webparent.paiementdp.com/aliAuthentification.php?site='+schoolid+'&token='+token)
    print(session.cookies.get_dict())
