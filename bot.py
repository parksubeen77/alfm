import discord, random
from discord.ext import commands
from dotenv import load_dotenv
import os
from flask import Flask


load_dotenv()

token = os.getenv("token")

#Flask 앱 생성
app = Flask(__name__)

@app.route("/")
def home():
    return "Discord 봇이 실행 중입니다!"

# Intents 설정
intents = discord.Intents.default()
intents.message_content = True

# commands.Bot 객체로 변경
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 준비 완료: {bot.user}")
    await bot.tree.sync()
    print("슬래시 커맨드 동기화 완료!")

# 슬래시 커맨드 등록
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


# Discord 봇 실행 함수
def run_discord_bot():
    bot.run(token)

if __name__ == "__main__":
    # Flask 앱 실행
    port = int(os.environ.get("PORT", 5000))
    
    # 봇을 별도 스레드로 실행
    from threading import Thread
    t = Thread(target=run_discord_bot)
    t.start()

    # Flask 서버 실행
    app.run(host="0.0.0.0", port=port)
