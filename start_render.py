import os
import threading
from fastapi import FastAPI
import uvicorn
import time
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Watch-Drop bot is running"}

# Function to run your bot as a separate process
def run_bot():
    try:
        # Replace with the command that normally runs your bot
        # Example if you run: python bot/main.py
        subprocess.call(["python", "bot/main.py"])
    except Exception as e:
        print("Error running bot:", e)

# Start the bot in a background thread
threading.Thread(target=run_bot, daemon=True).start()

# Start web server (must bind to Render $PORT)
port = int(os.environ.get("PORT", 10000))
uvicorn.run(app, host="0.0.0.0", port=port)
