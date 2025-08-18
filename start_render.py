import os
import threading
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Watch-Drop bot is running"}

# Function to run your existing bot
def run_bot():
    # Replace this with your main bot file
    # If your bot is bot/main.py:
    try:
        exec(open("bot/main.py").read())
    except Exception as e:
        print("Error running bot:", e)

# Start bot in background thread so web server keeps running
threading.Thread(target=run_bot, daemon=True).start()

# Bind to Render port
port = int(os.environ.get("PORT", 10000))
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=port)
