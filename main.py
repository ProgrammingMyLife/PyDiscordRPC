// all rights to https://hentaihaven.dev/
// github: https://github.com/tokenlogger/PyDiscordRPC/
import time
from pypresence import Presence

appid = int(input("Application ID: "))
rpc = Presence(appid)
rpc.connect()
details = input("Details: ")
state = input("State: ")
largeimg = input("Large Image Name: ")
smallimg = input("Small Image Name: ")
largeimgtext = input("Large Image Text: ")
rpc.update(details=details, state=state, large_image=largeimg, small_image=smallimg, large_text=largeimgtext)
while True: #while true loop to keep the presence running
    time.sleep(1)
