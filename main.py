import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8572237486:AAGxPeOKQo5Rg6kVieJNqYyrXV_ODYmSGe8"
# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 *Hoş geldin!*\n\n"
        "Bu bot, kripto para piyasalarını daha bilinçli takip edebilmen için\n"
        "📊 *canlı veriler*\n"
        "📈 *güncel fiyatlar*\n"
        "🧠 *piyasa istatistikleri*\n"
        "sunar.\n\n"
        "🔍 *Komutlar:*\n"
        "• /market → Genel piyasa & coin fiyatları\n\n"
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

# ---------------- MARKET ----------------
async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        global_url = "https://api.coingecko.com/api/v3/global"
        price_url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum,binancecoin,solana,ripple"
            "&vs_currencies=usd"
        )

        global_data = requests.get(global_url, timeout=10).json()
        prices = requests.get(price_url, timeout=10).json()

        total_market_cap = global_data["data"]["total_market_cap"]["usd"]
        volume_24h = global_data["data"]["total_volume"]["usd"]

        message = (
            "🌍 *Kripto Piyasası (Anlık)*\n\n"
            f"💰 *Toplam Market Değeri:*\n${total_market_cap:,.0f}\n\n"
            f"📊 *24s Hacim:*\n${volume_24h:,.0f}\n\n"
            "🔥 *Popüler Coinler:*\n"
            f"• BTC: ${prices['bitcoin']['usd']:,}\n"
            f"• ETH: ${prices['ethereum']['usd']:,}\n"
            f"• BNB: ${prices['binancecoin']['usd']:,}\n"
            f"• SOL: ${prices['solana']['usd']:,}\n"
            f"• XRP: ${prices['ripple']['usd']:,}"
        )

        await update.message.reply_text(message, parse_mode="Markdown")

    except Exception:
        await update.message.reply_text(
            "⚠️ Piyasa verileri şu an alınamıyor, lütfen biraz sonra tekrar dene."
        )

# ---------------- MAIN ----------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("market", market))

    app.run_polling()

if __name__ == "__main__":
    main()
