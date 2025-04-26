import telebot
from google import genai

# API Tokens
API_TOKEN = 'TELEGRAM_BOT_API_TOKEN'

# Initialize bot
bot = telebot.TeleBot(API_TOKEN)

# Configure Gemini
client = genai.Client(api_key="GEMINI_API_KEY")

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Hello! Welcome to RecipeBot! 🍽️\n\n"
        "I can generate delicious AI-powered recipes for you. Just send me the name of an ingredient or a dish, and I'll come up with something amazing! 😋\n\n"
        "Try typing: *Give me a recipe for pasta!* 🍝\n\n"
        "Use */help* to get the full list of commands."
    )

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        "🍽️ *RecipeBot Help* 📖\n\n"
        "Hello! I'm *RecipeBot*, your AI-powered kitchen assistant. I can generate delicious recipes for any ingredient or dish you request! 😋\n\n"
        "✨ *Here are some commands you can use:*  \n"
        "🔹 `/start` – Start the bot and get a welcome message.  \n"
        "🔹 `/help` – Show this help message with available commands.  \n"
        "🔹 `/about` – Learn more about RecipeBot.  \n"
        "🔹 `/recipe <dish>` – Get an AI-generated recipe for any dish.  \n"
        "🔹 `/random` – Get a surprise AI-generated recipe! 🎲  \n"
        "🔹 `/ingredients <ingredient>` – Get a recipe using a specific ingredient.  \n\n"
        "🍳 Just type the name of a dish or ingredient, and I'll do the rest! Happy cooking! 👨‍🍳🔥"
    )


# Handle '/about'
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(
        message,
        "🍽️ *About RecipeBot* 🤖\n\n"
        "Hey there! I'm *RecipeBot*, your AI-powered assistant that generates delicious recipes for any dish or ingredient you request! 😋 Whether you're a pro chef or just experimenting in the kitchen, I've got you covered. 🍳🔥\n\n"
        "📌 *Created by:* zeusenpai (Abhiram V.S)  \n"
        "🔗 *Connect with me:*  \n"
        "   • GitHub: [github.com/zeusenpai]  \n"
        "   • LinkedIn: [linkedin.com/in/abhiram-v-s-5490a6280/]  \n"
        "   • Instagram: [instagram.com/a.b.i999]  \n\n"
        "🚀 Feel free to reach out or contribute to the project!"
    )

# Handle '/random'
@bot.message_handler(commands=['random'])
def random(message):
    prompt = f"Generate a random brief, tasty recipe. recipe should be short"

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        recipe = response.text
        bot.reply_to(
            message, recipe)
    except Exception as e:
        bot.reply_to(message, f"Sorry, couldn't generate a recipe now 😓\nError: {str(e)}")
    

# Handle text messages for recipe generation
@bot.message_handler(func=lambda message: True)
def generate_recipe(message):
    user_query = message.text
    prompt = f"Generate a brief, tasty recipe for {user_query}."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        recipe = response.text
        bot.reply_to(message, recipe)
    except Exception as e:
        bot.reply_to(message, f"Sorry, couldn't generate a recipe now 😓\nError: {str(e)}")

print("Bot is running...")
bot.infinity_polling()
