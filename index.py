import os

if os.getenv("TOKEN","bad") == "bad":
    print("You need to export your token as a env var")
    print('On Linux/MacOS : export TOKEN="token"')
else:
    token = os.getenv("TOKEN")
    print("Token found !")
    print("Your token is : "+token)
