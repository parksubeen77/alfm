import os
import subprocess
import threading
from flask import Flask

app = Flask(__name__)

# Flask에서 기본 경로
@app.route('/')
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask 서버 실행 함수
def run_flask():
    port = os.environ.get("PORT", 5000)  # Render의 환경 변수로 포트 설정
    app.run(host="0.0.0.0", port=int(port))

# Discord 봇을 실행하는 함수
def run_discord_bot():
    subprocess.Popen(["python", "bot.py"])  # Discord 봇을 별도 프로세스로 실행

# Flask와 Discord 봇을 동시에 실행하는 함수
def run():
    # Flask 서버를 별도의 스레드에서 실행
    threading.Thread(target=run_flask).start()

    # Discord 봇을 별도의 프로세스로 실행
    run_discord_bot()

if __name__ == "__main__":
    run()
