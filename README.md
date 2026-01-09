# PythonTelegramBot


1. Make sure you have Python 3.7 or higher and Pip installed

2. Run botsetup.bat to install needed libraries

3. In Telegram find BOTFATHER and make a new bot and obtain you bot token

4. Go to edit your bot and edit commands, type in(
movie-Watch a Random Movie
remind-Set a Reminder
diceroll-Roll a Dice
game-Get a Random Game
whattodo-Random Activities
rn-Random number between 1-1000
)

5. Create .env file with all of the variables needed (BOT_TOKEN, and WHITELIST for admin chat IDs), example is shown in .env, it will not work without that file

6. Place all other files(sprls.txt, gmls.txt, activities.txt, .env and bot.py) in the same folder

7. In your terminal go to that directory and type python bot.py

8. Your bot should be running and responding to your commands if you did everythin correctly(note: commands will not work if bot.py isnt running so if you plan on using it more seriously think about a small server something like Raspberry PI 2 or 3 should be more than plenty to run this and it should work just fine(I have not tested it yet since my PI has not arrived yet))
