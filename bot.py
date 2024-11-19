import os
import discord
from discord.ext import commands
from flask import Flask
import threading
import random
import time

# .env 파일 로드
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

# Flask 서버 설정
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord 봇과 Flask 서버가 동시에 실행 중입니다!"

# Discord 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 준비 완료: {bot.user}")
    await bot.tree.sync()
    print("슬래시 커맨드 동기화 완료!")

@bot.tree.command(name="생존자", description="생존자 랜덤 뽑기")
async def surviver(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice([
        '행운아','의사','변호사','도둑','정원사','마술사','모험가',
        '용병','공군','샤먼','기계공','포워드','맹인','조향사','카우보이',
        '무희','선지자','납관사','탐사원','주술사','야만인','곡예사',
        '항해서','바텐더','우편배달부','묘지기','죄수','곤충학자',
        '화가','타자','장난감상인','심리학자','환자','소설가',
        '여자아이','우는광대','교수','골동품상인','작곡가','기자',
        '항공전문가','치어리더','인형사','화재조사관','파로부인','기사']))

# Flask 서버 실행 함수
def run_flask():
    port = os.environ.get("PORT", 5000)  # Render에서 제공하는 포트 설정
    app.run(host="0.0.0.0", port=int(port))

# Discord 봇 실행 함수
async def run_discord_bot():
    await bot.run(TOKEN)

# Flask와 Discord 봇을 동시에 실행하는 함수
def run():
    # Flask 서버는 별도의 스레드에서 실행
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Discord 봇 실행
    asyncio.run(run_discord_bot())  # 봇은 메인 스레드에서 실행

if __name__ == "__main__":
    run()
