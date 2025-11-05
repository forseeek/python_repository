from typing import Final
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import random

# Constants
TOKEN: Final[str] = "Your token here"
BOT_USERNAME: Final[str] = "@name_of_your_bot"

"""Send a message when the command /start is issued."""
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Hello!! {user.mention_html()}!"
    )

"""Send an image of parrot when the command /parrot is issued."""
async def parrot_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parrot_photo = "https://cdn.britannica.com/35/3635-050-96241EC1/Scarlet-macaw-ara-macao.jpg"
    
    await update.message.reply_photo((parrot_photo), caption="Look!!")

def handle_response(text: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    processed: str = text.lower()
    if "привіт" in processed:
        return "Привіт!"
    elif "як ти" in processed:
        answers = [
            "Як Windows без оновлень — тримаюсь, але трохи глючу.",
            "Як котик у коробці — одночасно добре і загадково.",
            "Наче Wi-Fi: іноді стабільно, іноді взагалі без зв’язку.",
            "Живу, як Google Chrome: відкрито 100 вкладок, а батарея на нулі.",
            "Як морозиво в спеку — намагаюся не розтанути.",
            "Як вчитель інформатики — з усмішкою, але з внутрішнім багом.",
            "Наче серіал: нові серії виходять щодня, але ніхто не знає сюжет.",
            "Як у математиці — завжди можна скоротити проблему.",
            "Я в нормі, просто норму ще шукаю.",
        ]
        return random.choice(answers)
    return "... я не зрозумів"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text # what the user actually said
    # Log
    print(f'User ({update.message.chat.id} in {message_type}): "{text}"')
    # Handle message type
    # if message posted in group - act only if bot name mentioned. Remove Bot name from message
    if message_type =="group": 
        if BOT_USERNAME in text:
             new_text: str = text.replace(BOT_USERNAME, "").strip()
             response: str = handle_response(new_text, update, context)
        else:# do nothing in group if bot name is not in message
            return
    else:# if it's a private message, just proceed with logic
        response: str = handle_response(text, update, context)

    #Reply
    print(f"Bot {response}")
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


def main():
    print("Starting up bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("parrot", parrot_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5) # check for message every 5 seconds

if __name__ == "__main__":
    main()