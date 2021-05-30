# all rights to https://hentaihaven.dev/
# github: https://github.com/tokenlogger/PyDiscordRPC/
import time, sys
from pypresence import Presence
from pypresence.exceptions import InvalidID

print("""
Your client ID is found out the discord developer portal. Create an application, 
then you will be prompted to choose a name, choose a random name you want for your RPC then click enter. 
You will see a client ID. Copy it, and paste it
""")


appid = input("Application ID: ") #This should not be an Int because an end user can just add a random string. Most code editors will help you avoid this, unless
#the dev uses some stupid shit like notepad or idle

try :
    rpc = Presence(appid)

except InvalidID:
    print(
        """
The ID you entered was invalid. Please make sure you enetered the correct ID from the discord developer portal, and not your own personal ID.
        """
    )
    sys.exit()
    


rpc.connect()
details = input("Details: ") #This is way too vague but I am not going to edit it as some users might be a bit advanced
state = input("State: ") #This is vague too
largeimg = input("Large Image Name. You can find the large image name by going to the application on discord developer portal > Rich Presence > Add an image: ") 
smallimg = input("Small Image Name. This is the text that appears when you hover over the large image.: ")
largeimgtext = input("Large Image Text: ")

while True: #while true loop to keep the presence running
    rpc.update(details=details, state=state, large_image=largeimg, small_image=smallimg, large_text=largeimgtext)
    time.sleep(15)

    #Keep the RPC Update in the loop.
