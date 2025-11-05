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
        f"Привіт!! {user.mention_html()}! Давай поспілкуємося?"
    )

"""Send a message when the command /help is issued."""
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html("Це бот для навчання")

"""Send an image of parrot when the command /parrot is issued."""
async def parrot_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parrot_photos = [
        "https://cdn.britannica.com/35/3635-050-96241EC1/Scarlet-macaw-ara-macao.jpg",
        "https://www.lpzoo.org/wp-content/uploads/2023/01/parrot-tall-750x1203.png",
        "https://img.freepik.com/free-photo/closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head_488145-3540.jpg?semt=ais_hybrid&w=740&q=80",
        "https://www.marylandzoo.org/wp-content/uploads/2017/10/african_grey_web-1024x683.jpg",
        "https://senecaparkzoo.org/wp-content/uploads/2023/04/Indian-Ring-neck-Parakeet-IMG_9280-2-768x768.jpg"
    ]
    await update.message.reply_photo(random.choice(parrot_photos), caption="Диви яка папужка!")

def handle_response(text: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    processed: str = text.lower()
    if "привіт" in processed:
        return "Привіт!"
    elif "python" in processed:
        return "Python (Пайтон) — це мова програмування, проста у вивченні й дуже популярна. 🐍\nКоротко:\n👉 Її використовують для створення сайтів, програм, ігор, штучного інтелекту, аналізу даних тощо.\n👉 Вона легко читається, тому навіть новачки швидко починають писати код."
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
    elif ("анекдот" in processed) or ("жарт" in processed):
        answer = [
            "— Чому ти запізнився на урок?\n— Та я повільно біг!🐌",
            "— Докторе, я постійно забуваю, що ви мені радите!\n— Добре, тоді я вам пораджу записувати.\n— А що записувати?🤔",
            "У бібліотеці:\n— У вас є книга “Як швидко розбагатіти”?\n— Так, але вона зараз на руках у працівників податкової 😏",
            "— Ти ходиш у спортзал?\n— Так, але не всередину. Просто проходжу повз — надихає.🚶‍♂️‍➡️",
            "В останній час сплю як вбитий. Пару разів навіть крейдою обводили!..🤪",
            "Дуже важко шукати роботу своєї мрії, якщо твоя мрія - не працювати!🤔",
            "Найнеприємніше в житті, це коли тобі заважають нічого не роботи!😊"
        ]
        return random.choice(answer)
    elif ("факт" in processed) or ("цікавинка" in processed) or ("цікаво" in processed):
        facts = [
            "У середньому людина за життя проходить близько 120 000 км — це приблизно тричі навколо Землі!",
            "Половина населення Землі (а за деякими підрахунками навіть дві третини) ніколи не бачили снігу.",
            "Кубик Рубіка – товар, який найбільше продається у світі. На другому місці – iPhone.",
            "На шоломах астронавтів є спеціальний пристрій, щоб чухати носа.",
            "Ймовірність стати президентом у кожної людини вища, ніж виграти в лотерею. До речі, померти на шляху до лотерейного квитка теж більш імовірно, ніж перемогти.",
            "Лимон містить більше цукру, ніж полуниця, хоча його смак значно кисліший.",
            "Офіційна назва \"Біг-Бену\" – Вежа Єлизавети (Elizabeth Tower), перейменована так у 2012 році на честь королеви Єлизавети II.",
            "Довжина Великої Стіни становить майже 9 тисяч кілометрів. Без малого 8852 кілометри, якщо точніше. Це робить її найбільшою спорудою в історії.",
            "Клеопатра жила ближче за часом до створення iPhone, ніж до будівництва піраміди Хеопса.",
            "У Львові є вулиця, що офіційно складається з однієї адреси – це вулиця Вірменська, 35, де розташований Вірменський собор."
        ]
        return random.choice(facts)
    elif context.user_data["math_index"] == 1:
        math_answer = context.user_data["math_answer"]
        context.user_data["math_index"] = 0
        if update.message.text == str(math_answer):
            return("✅ Правильно!")
        else:
            return(f"❌ Ні! Правильна відповідь: {math_answer}")
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


# Level UP

# --- Список запитань ---
QUIZ_QUESTIONS = [
    {
        "question": "Яка мова програмування названа на честь гумориста?",
        "options": ["Python", "Java", "C++", "Ruby"],
        "correct": 0
    },
    {
        "question": "Хто написав \"Фауст\"?",
        "options": ["Фрідріх Шиллер", "Йоган Вольфганг фон Гете", "Генріх Гейне", "Альберт Ейнштейн"],
        "correct": 1
    },
    {
        "question": "Яка країна має найбільшу кількість сусідів (межує з найбільшою кількістю інших держав)?",
        "options": ["Україна", "Індія", "ДР Конго", "Китай"],
        "correct": 3
    },
    {
        "question": "Скільки кісток у тілі дорослої людини?",
        "options": ["206", "210", "198", "216"],
        "correct": 0
    },
]

# --- Функція для старту вікторини ---
async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["quiz_index"] = 0
    await send_question(update, context)

# --- Функція для надсилання питання ---
async def send_question(update_or_query, context: ContextTypes.DEFAULT_TYPE):
    index = context.user_data.get("quiz_index", 0)
    question_data = QUIZ_QUESTIONS[index]

    buttons = []
    for i, option in enumerate(question_data["options"]):
        buttons.append([InlineKeyboardButton(option, callback_data=str(i))])

    keyboard = InlineKeyboardMarkup(buttons)

    # якщо це перше питання через /quiz
    if hasattr(update_or_query, "message"):
        await update_or_query.message.reply_text(question_data["question"], reply_markup=keyboard)
    else:  # якщо після вибору відповіді
        await update_or_query.edit_message_text(question_data["question"], reply_markup=keyboard)

# --- Обробник натискання кнопок ---
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    index = context.user_data.get("quiz_index", 0)
    question_data = QUIZ_QUESTIONS[index]
    chosen = int(query.data)

    if chosen == question_data["correct"]:
        await query.edit_message_text("✅ Правильно!")
    else:
        await query.edit_message_text(f"❌ Ні! Правильна відповідь: {question_data['options'][question_data['correct']]}")

    # наступне питання, якщо є
    context.user_data["quiz_index"] = index + 1
    if context.user_data["quiz_index"] < len(QUIZ_QUESTIONS):
        await send_question(query, context)
    else:
        await query.message.reply_text("Кінець вікторини! Молодець ")

# --- Функція для старту прикладів з математики ---
async def math_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["math_index"] = 0
    context.user_data["math_answer"] = 0
    await send_math_example(update, context)

# --- Функція для надсилання прикладу по математиці ---
async def send_math_example(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question_data = ""
    result = 0
    action = random.randint(0, 2)
    if (action == 0):
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        result = number1 + number2
        question_data = f"{number1} + {number2} = ???"
    if (action == 1):    
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        result = number1 - number2
        question_data = f"{number1} - {number2} = ???"
    if (action == 2):    
        number1 = random.randint(-10, 10)
        number2 = random.randint(-10, 10)
        result = number1 * number2
        question_data = f"{number1} * {number2} = ???"

    context.user_data["math_answer"] = result
    context.user_data["math_index"] = 1
    await update.message.reply_text(question_data)

def main():
    print("Starting up bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    # Homework
    app.add_handler(CommandHandler("parrot", parrot_command))
    #Level Up
    app.add_handler(CommandHandler("quiz", quiz_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(CommandHandler("math", math_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5) # check for message every 5 seconds

if __name__ == "__main__":
    main()