import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("8572237486:AAGxPeOKQo5Rg6kVieJNqYyrXV_ODYmSGe8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 *Hoş geldin!*\n\n"
        "Bu bot kripto piyasaları hakkında *canlı veriler, istatistikler* "
        "ve *faydalı kaynaklar* sunar.\n\n"
        "⚠️ _Yatırım tavsiyesi değildir._"
    )

    keyboard = [
        [InlineKeyboardButton("📈 CoinMarketCap", url="https://coinmarketcap.com")],
        [InlineKeyboardButton("📊 TradingView", url="https://tradingview.com")],
        [InlineKeyboardButton("🧠 On-Chain", url="https://cryptoquant.com")]
    ]

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
