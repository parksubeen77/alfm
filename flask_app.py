# flask_app.py
from flask import Flask
from discord_bot import run_discord_bot  # 봇 코드 import
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask 서버 실행 함수
def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # 봇을 별도의 스레드로 실행
    t_bot = Thread(target=run_discord_bot, daemon=True)
    t_bot.start()

    # Flask 서버를 별도의 스레드로 실행
    print("Flask 서버가 시작되었습니다.")
    run_flask()
