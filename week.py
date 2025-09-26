from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "YOUR_BOT_TOKEN"
GAME_SHORT_NAME = "click_game"   # must be registered in BotFather

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 Play Game", callback_game=GAME_SHORT_NAME)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click below to play:", reply_markup=reply_markup)

# Set user score (Bot API call from Telegram WebView)
async def set_score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        # Example: set score 42 for the current user
        await context.bot.set_game_score(
            user_id=query.from_user.id,
            score=42,  # <-- replace with actual score from WebView
            chat_id=query.message.chat.id,
            message_id=query.message.message_id
        )
        await query.answer("✅ Score saved!")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_score))

app.run_polling()