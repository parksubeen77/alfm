import os
from flask import Flask
import subprocess
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask 서버 실행 함수
def run_flask():
    port = os.environ.get("PORT", 5000)  # 환경 변수에서 포트 번호를 가져옴
    app.run(host="0.0.0.0", port=int(port))

# Discord 봇을 실행하는 함수
def run_discord_bot():
    subprocess.Popen(["python", "bot.py"])

# Flask와 Discord 봇을 동시에 실행하는 함수
def run():
    # Flask 서버를 별도 프로세스로 실행
    threading.Thread(target=run_flask).start()

    # Discord 봇을 별도 프로세스로 실행
    run_discord_bot()

if __name__ == "__main__":
    run()
