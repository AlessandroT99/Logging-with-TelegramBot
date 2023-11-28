#!/usr/bin/python3
import telepot
#import YOUR_LIBRARY

# CODE TO MODIFY ------------------------------------------------------------------------------------------------------------------------------------
MATLAB_USE = 0 # Put equal to 1 if this script is used to MatLab [ONLY FOR THE LOGGING NOT BEFORE THE USER ID RECOGNITION]

# DO NOT SHARE THIS TWO IDs - they are personal
userName = 0   # User Telegram ID
TOKEN = 'yourtoken' # Token of your bot

# FUNCTIONS DEFINE ----------------------------------------------------------------------------------------------------------------------------------
def incomingMessages():
    global update_id
    #Checking if there are messages
    msg = bot.getUpdates(offset=update_id)
    if msg != []:
        update_id = msg[0]['update_id']
        update_id += 1
        name = msg["from"]["first_name"]
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, f"Hi {str(name)}, your Telegram ID is: {str(chat_id)}.")
        print(f"\nHi {str(name)}, your Telegram ID is: {str(chat_id)}.")

# GLOBAL VARIABLES INIT -----------------------------------------------------------------------------------------------------------------------------
update_id = 0
bot = telepot.Bot(TOKEN)

# MAIN PROGRAM --------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    if userName == 0:
        incomingMessages()
    else:
        if MATLAB_USE:
            bot.sendMessage(userName, txtMsg)
        else:
            #txt = YOUR_FUNCTION()
            bot.sendMessage(userName, txt)
            
