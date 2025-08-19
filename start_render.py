import os
import asyncio
import threading
from bot.main import main as bot_main  # import your async main from bot

from flask import Flask

app = Flask(__name__)

# Start bot in background thread
def run_bot():
    asyncio.run(bot_main())

threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
