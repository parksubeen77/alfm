# flask_app.py
from flask import Flask
from discord_bot import run_discord_bot  # 봇 코드 import
from threading import Thread
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask 서버 실행 함수
def run_flask():
    app.run(host="0.0.0.0", port=5000)

def run():
    # Flask 서버 실행
    thread_flask = Thread(target=run_flask)
    thread_flask.start()

    asyncio.run(run_discord_bot())

if __name__ == "__main__":
    run()
