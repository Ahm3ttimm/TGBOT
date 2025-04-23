import os
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)

# .env dosyasını yükle
load_dotenv("key.env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API_URL = "https://api.github.com"

# Başlangıç
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Proje Ara", callback_data="search")],
        [InlineKeyboardButton("👤 Hesap Durumu", callback_data="status")],
        [InlineKeyboardButton("📁 Repos", callback_data="repos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Selam! GitHub Yardım Botu 🛠️ hazır.\nAşağıdan ne yapmak istediğini seç:",
        reply_markup=reply_markup
    )

# Inline butonlara cevap
async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "search":
        await query.edit_message_text("🔍 Lütfen `/search <proje_adı>` komutunu kullan.")
    elif query.data == "status":
        await query.edit_message_text("👤 Lütfen `/status <kullanıcı_adı>` komutunu kullan.")
    elif query.data == "repos":
        await query.edit_message_text("📁 Lütfen `/repos <kullanıcı_adı>` komutunu kullan.")

# Proje Arama
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Kullanım: `/search fastapi`", parse_mode="Markdown")
        return

    query = " ".join(context.args)
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    res = requests.get(f"{GITHUB_API_URL}/search/repositories?q={query}", headers=headers)

    if res.status_code == 200:
        data = res.json().get("items", [])
        if data:
            msg = f"🔍 *'{query}'* için bulunan projeler:\n\n"
            for repo in data[:5]:
                msg += f"🔹 [{repo['full_name']}]({repo['html_url']})\n"
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text("📭 Hiç proje bulunamadı.")
    else:
        await update.message.reply_text("🚫 GitHub API hatası.")

# Hesap Durumu
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Kullanım: `/status github_kullanici`", parse_mode="Markdown")
        return

    username = context.args[0]
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    res = requests.get(f"{GITHUB_API_URL}/users/{username}", headers=headers)

    if res.status_code == 200:
        d = res.json()
        msg = (
            f"👤 *{d['login']}*\n"
            f"📅 Oluşturuldu: {d['created_at'][:10]}\n"
            f"📂 Repo Sayısı: {d['public_repos']}\n"
            f"🔗 [Profiline Git]({d['html_url']})"
        )
        await update.message.reply_text(msg, parse_mode="Markdown")
    else:
        await update.message.reply_text("🚫 Kullanıcı bulunamadı.")

# Kullanıcının Reposu
async def repos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Kullanım: `/repos github_kullanici`", parse_mode="Markdown")
        return

    username = context.args[0]
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    res = requests.get(f"{GITHUB_API_URL}/users/{username}/repos?sort=updated", headers=headers)

    if res.status_code == 200:
        data = res.json()
        if data:
            msg = f"📂 *{username}* kullanıcısının son projeleri:\n\n"
            for repo in data[:5]:
                msg += f"🔸 [{repo['name']}]({repo['html_url']}) | 🕒 {repo['updated_at'][:10]}\n"
            await update.message.reply_text(msg, parse_mode="Markdown")
        else:
            await update.message.reply_text("📭 Kullanıcının public reposu yok.")
    else:
        await update.message.reply_text("🚫 GitHub API hatası.")

# Botu başlat
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("repos", repos))

    print("🚀 GitHub Yardım Botu Aktif!")
    app.run_polling()

if __name__ == "__main__":
    main()
