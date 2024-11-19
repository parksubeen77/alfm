import discord, random
from discord.ext import commands
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# .env 파일에서 토큰 불러오기
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    print("토큰이 설정되지 않았습니다. .env 파일을 확인하세요.")
    exit(1)
else:
    print("토큰이 정상적으로 로드되었습니다.")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"봇 준비 완료: {bot.user}")
    # 슬래시 명령어 동기화
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

def run_discord_bot():
    print(f"Bot token: {TOKEN}")  # 토큰을 확인하기 위해 출력
    bot.run(TOKEN)

if __name__ == "__main__":
    run_discord_bot()
