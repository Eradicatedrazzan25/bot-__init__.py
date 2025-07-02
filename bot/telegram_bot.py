from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

OWNER_ID = int(os.getenv("OWNER_ID"))

# Main /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ Access Denied.")
        return

    keyboard = [
        [InlineKeyboardButton("📡 Add Channel", callback_data="add_channel")],
        [InlineKeyboardButton("📄 Show Config", callback_data="show_config")],
        [InlineKeyboardButton("💼 Add Wallet", callback_data="add_wallet")],
        [InlineKeyboardButton("📊 Show P&L", callback_data="show_pnl")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to your Solana Trading Bot. Choose an action:", reply_markup=reply_markup)

# Handle button presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "add_channel":
        await query.edit_message_text("📡 Send the channel username or ID to add:")
        # next step: add conversation handler
    elif data == "show_config":
        await query.edit_message_text("🔧 Configuration:\nProfit: 60%\nStop Loss: -30%\nBuy: 0.1 SOL")
    elif data == "add_wallet":
        await query.edit_message_text("💼 Please send your wallet seed phrase:")
    elif data == "show_pnl":
        await query.edit_message_text("📈 Total P&L tracking is under development.")

# Bot initializer
def init_bot():
    app = ApplicationBuilder().token(os.getenv("TEL_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    return app
