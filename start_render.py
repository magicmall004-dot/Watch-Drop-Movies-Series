import os
import threading
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Bot is running"}

# Your bot function
def start_bot():
    while True:
        print("Bot running...")
        # If your bot has other code, you can call it here
        time.sleep(60)

threading.Thread(target=start_bot, daemon=True).start()

port = int(os.environ.get("PORT", 10000))
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=port)
