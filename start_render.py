import os
import threading
import subprocess
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Watch-Drop bot is running"}

def run_bot():
    try:
        subprocess.Popen(["python", "bot/main.py"])
    except Exception as e:
        print("Error running bot:", e)

threading.Thread(target=run_bot, daemon=True).start()

port = int(os.environ.get("PORT", 10000))
uvicorn.run(app, host="0.0.0.0", port=port)
