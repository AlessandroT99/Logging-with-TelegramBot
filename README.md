# Logging with TelegramBot
Do you ever wanted a method that could let you know news from your long software execution which you cannot physically look at? Here it is your solution! 

------------------------------
## What is a Telegram Bot? 
An artificial user of Telegram which can be programmed to behave in a predefined way. You can distinguish them by the termination "bot" after their name.

## How to create one? 
You need to meet the **BotFather**, which you can find just typing its name on the telegram research.
Here it is the procedure that you need to do to create successfully your bot:
* `/start`: You will start the bot father
* `/newbot`: The creation will begin, you just need to follow the steps which will be told you (if needed look at the [step-by-step guide](https://core.telegram.org/bots/features#creating-a-new-bot))
* Get your token from the **BotFather** and save it for later
* Modify eventual preferences of your bot, first `/mybots`, choose your bot, select *Edit Bot* and modify whatever you need.

## Install telepot library
To let this script work, your will need the library `telepot`, which you can simply install as:
* [WINDOWS] -> `py -m pip install telepot`
* [UBUNTU]  -> `pip install telepot`

## Understand you telegram user ID
Now that you got you working bot and its token, you have to know which is your telegram user ID in order to sent messages directly to you.
Open the telegramLoggin.py file and substitute your token into `TOKEN = 'yourtoken'`, now execute the script, your bot will send you a message with your ID, and you will also be able to copy it from the command line.

## Run your logger
Substitute your ID into `userName = xxx` and you are almost ready to go!
Just choose your use:
* Execute it from a MatLab script       -> Set the constant `MATLAB_USE` at the start of the script equal to 1. 
* Execute it from another python script -> Leave the script as it is.

#### MATLAB PROCEDURE
* Install the python version in your machine according to your MatLab version looking at the [supported version guide](https://it.mathworks.com/support/requirements/python-compatibility.html) and be sure to install the wanted version with the last bug fix.
* Run in MatLab `pyenv(Version="C:\Users\YOUR_USER_NAME\AppData\Local\Programs\Python\Python311\python.exe");`
* Check the correctness of the installation with running again `pyenv`
* Call when you want `pyrunfile("YOUR_PATH/telegramLogging.py",TEXT_TO_PRINT)` where *TEXT_TO_PRINT* is your string variable.
----------------------------
## Have you got any issue?
Let me know what is the problem! I will fix it and load a new commit.

## Have you any ideas? 
Feel free to modify and use this code, collaboration is fundamental!

----------------------------
### Author
Alessandro Tiozzo @2023
