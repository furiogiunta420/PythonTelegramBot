import os 
import random 
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime, timedelta
import re 
import logging 
import asyncio 
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in enviorment variable")



WHITELIST = os.getenv('WHITELIST')

if not WHITELIST:
    raise ValueError("Admin ID could not be resolved")

WHITELIST = set(int(id.strip()) for id in WHITELIST.split(','))

def raus():
    os.system('cls' if os.name == 'nt' else 'clear')








FILE_PATH = "sprls.txt"
GAME_PATH = "gmls.txt"
ACTIVITIES = "activites.txt"





#=============AUTHORIZATION LOGIC==========

async def author(update: Update) -> bool:
    chat_id = update.effective_chat.id
    if chat_id != WHITELIST:
        await update.message.reply_text("UNAOTHORIZED ACCESS")
        return False
    return True 



#      ADD THESE 2 LINES INSIDE FIRST LINES OF THE FEATURES YOU WANT TO LOCK 

#     if not await author(update):
#        return 








# ================REMINDER LOGIC==============

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "❌ Usage: /remind <time> <message>\n"
            "Example: /remind 30m Smoke break"
        )
        return 
    
    time_str = context.args[0]
    message = ' '.join(context.args[1:])

    match = re.match(r'^(\d+)([mhd])$', time_str.lower())

    if not match:
        await update.message.reply_text(
            "❌ Invalid time format. Use: 5m, 30m, 2h, or 1d\n"
            "m = minutes, h = hours, d = days"
        )
        return 
    
    amount = int(match.group(1))
    unit = match.group(2)

    if unit == 'm':
        seconds = amount * 60
        time_display = f"{amount} minute{'s' if amount > 1 else ''}"
    elif unit == 'h':
        seconds = amount * 3600
        time_display = f"{amount} hour{'s' if amount > 1 else ''}"
    elif unit == 'd':
        seconds = amount * 86400
        time_display = f"{amount} day{'s' if amount > 1 else ''}"

    
    chat_id = update.effective_chat.id
    context.job_queue.run_once(
        send_reminder,
        seconds,
        data={'chat_id': chat_id, 'message': message},
        name=f"reminder_{chat_id}_{datetime.now().timestamp()}"
    )

    reminder_time = datetime.now() + timedelta(seconds=seconds)
    time_formatted = reminder_time.strftime("%I:%M %p on %b %d")

    await update.message.reply_text(
        f"✅ Reminder set!\n"
        f"⏰ I'll remind you in {time_display}\n"
        f"📅 At: {time_formatted}\n"
        f"📝 Message: {message}"
    )


# =============REMINDER SENDER================

async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    job_data = context.job.data
    chat_id = job_data['chat_id']
    message = job_data['message']

    print("=" * 120)

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"REMINDER:\n\n{message}"
    )
    print("=" * 120)


# ==========MOVIE PICKER================
async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:

        if not os.path.exists(FILE_PATH):
            await update.message.reply_text(
                f"Error: {FILE_PATH} not found. Make sure it is in the same directory"
            )
            return
        
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip()]

        if not lines:
            await update.message.reply_text(
                "The file is empty. Please add some movies"
            )
            return 
        
        random_line = random.choice(lines)

        await update.message.reply_text(
            f"You should watch:  {random_line}"
        )
    except Exception as e:
        await update.message.reply_text(f"An error occured: {str(e)}")


# =============GAME PICKER========================

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not os.path.exists(GAME_PATH):
            await update.message.reply_text(
                f"Error: {GAME_PATH} not found. Make sure it is in the same directory"
            )
            return
        with open(GAME_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip()]
        if not lines:
            await update.message.reply_text(
                "The file is empty please add some games to it..."
            )
            return
        random_line = random.choice(lines)
        await update.message.reply_text(
            f"You should play: {random_line}"
        )
    except Exception as e:
        await update.message.reply_text(f"An error occured: {str(e)}")



# ===================ACTIVITIES================

async def whattodo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not os.path.exists(ACTIVITIES):
            await update.message.reply_text(
                f"Error: {ACTIVITIES} not found. Make sure it is in the same directory"
            )
            return
        with open(ACTIVITIES, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip()]
        if not lines:
            await update.message.reply_text(
                "The file is empty please add some activites to it"
            )
            return 
        random_line = random.choice(lines)
        await update.message.reply_text(
            f"You should: {random_line}"
        )
    except Exception as e:
        await update.message.reply_text(f"An error occured: {str(e)}")

# ==========DICE ROLL===================

async def diceroll(update: Update, context: ContextTypes.DEFAULT_TYPE):


    
    numb = random.randint(1, 6)
    
    await update.message.reply_text(
        "Dice is being rolled..."
    )

    await asyncio.sleep(1.5)

    await update.message.reply_text(
        f"🎲 roll is: {numb}"
    )



# ========RANDOM NUMBER============

async def rn(update: Update, context: ContextTypes.DEFAULT_TYPE):

    numb = random.randint(1, 1000)

    await update.message.reply_text(
        "Random number is being generated"
    )

    await asyncio.sleep(1.5)

    await update.message.reply_text(
        f"Your random number is: {numb}"
    )
























# ================MAIN LOOP========================

def main():

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("movie", movie))
    application.add_handler(CommandHandler("remind", remind))
    application.add_handler(CommandHandler("diceroll", diceroll))
    application.add_handler(CommandHandler("game", game))
    application.add_handler(CommandHandler("whattodo", whattodo))
    application.add_handler(CommandHandler("rn", rn))
    

    raus()
    print("Bot is running... Press CTRL+C to stop...")
    print("=" * 120)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
