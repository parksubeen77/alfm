# flask_app.py
from flask import Flask
import subprocess
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord 봇이 실행 중입니다!"

# Flask 서버 실행 함수
def run_flask():
    app.run(host="0.0.0.0", port=5000)

# Flask와 Discord 봇을 동시에 실행하는 함수
def run():
    # Flask 서버를 별도 프로세스로 실행
    threading.Thread(target=run_flask).start()

    # Discord 봇을 별도 프로세스로 실행
    subprocess.Popen(["python", "bot.py"])

if __name__ == "__main__":
    run()
