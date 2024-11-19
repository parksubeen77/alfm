# flask_app.py
from flask import Flask
from discord_bot import run_discord_bot
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask와 Discord 봇을 각각 별도의 스레드로 실행
def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # 봇을 별도의 스레드로 실행
    t_bot = Thread(target=run_discord_bot)
    t_bot.start()

    # Flask 서버를 별도의 스레드로 실행
    t_flask = Thread(target=run_flask)
    t_flask.start()
