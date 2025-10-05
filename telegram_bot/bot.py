import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
logging.basicConfig(level=logging.INFO)


load_dotenv()

API = os.getenv("API_BASE_URL", "http://localhost:8000/api")
ALLOWED = [int(x) for x in os.getenv("ALLOWED_TELEGRAM_USER_IDS", "").split(",") if x]
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def allowed(user_id: int) -> bool:
    return True
    #return not ALLOWED or user_id in ALLOWED


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Productivity Agent Bot! Use /help to see available commands.")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Available commands:\n"
        "/add <task> – add new task\n"
        "/list – list all tasks\n"
        "/done <id> – mark task done\n"
        "/categories – list categories\n"
        "/focus_start [25|deep] – start focus session\n"
        "/focus_stop – stop focus session\n"
        "/coach <question> – ask the AI coach"
    )
    await update.message.reply_text(text)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update.effective_user.id):
        return await update.message.reply_text("Access denied.")
    title = " ".join(context.args)
    if not title:
        return await update.message.reply_text("Usage: /add <task>")
    r = requests.post(f"{API}/tasks/", json={"title": title})
    msg = "✅ Task added" if r.ok else f"❌ Error: {r.text}"
    await update.message.reply_text(msg)


async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.get(f"{API}/tasks")
    if not r.ok:
        return await update.message.reply_text("❌ Failed to fetch tasks.")
    tasks = r.json()
    if not tasks:
        return await update.message.reply_text("No tasks found.")
    lines = [f"{t['id']}. {'✅' if t['completed'] else '⬜'} {t['title']}" for t in tasks]
    await update.message.reply_text("\n".join(lines))


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("Usage: /done <id>")
    task_id = context.args[0]
    r = requests.post(f"{API}/tasks/{task_id}/done")
    msg = "✅ Marked done" if r.ok else "❌ Task not found"
    await update.message.reply_text(msg)


async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.get(f"{API}/categories")
    if not r.ok:
        return await update.message.reply_text("❌ Failed to fetch categories.")
    cats = r.json()
    text = "\n".join([f"{c['id']}. {c['name']}" for c in cats]) or "No categories."
    await update.message.reply_text(text)


async def focus_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.args[0] if context.args else "25"
    r = requests.post(f"{API}/focus/start", params={"type": mode})
    msg = "▶️ Focus started" if r.ok else "❌ Failed"
    await update.message.reply_text(msg)


async def focus_stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.post(f"{API}/focus/stop", params={"session_id": 1})
    msg = "⏹ Focus stopped" if r.ok else "❌ Failed"
    await update.message.reply_text(msg)


async def coach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        return await update.message.reply_text("Usage: /coach <question>")
    r = requests.post(f"{API}/coach/", json={"prompt": question})
    if r.ok:
        ans = r.json().get("answer", "")
        await update.message.reply_text(ans)
    else:
        await update.message.reply_text("❌ Error contacting coach.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_tasks))
    app.add_handler(CommandHandler("done", done))
    app.add_handler(CommandHandler("categories", categories))
    app.add_handler(CommandHandler("focus_start", focus_start))
    app.add_handler(CommandHandler("focus_stop", focus_stop))
    app.add_handler(CommandHandler("coach", coach))

    print("Bot running…")
    app.run_polling()


if __name__ == "__main__":
    main()
