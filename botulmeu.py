
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '$')
@bot.event
async def on_ready():
    print("The bot is ready!")
    activity = discord.Activity(name='Filme porno', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.event
async def on_member_join(member):
    print('{} intra in pizda'.format(member))

@bot.event
async def on_member_remove(member):
    print(f'{member} s-a dus pe pula')

@bot.event
async def on_message(message):
    print(f'{message.channel}:{message.author}:{message.author.name}:{message.author.id}:{message.content}')

    if 'hello' in message.content.lower():
        await message.channel.send('hi')
    if 'hatz' in message.content.lower():
        await message.channel.send('JOHNULEEEE')
    if message.author.id == 323882802275942403:
        await message.channel.send('taci darius')
    if message.author.id == 327085239518232576:
        await message.channel.send('SORIN SUGE PULA')


bot.run('NjExNjUxMDE1NjE5NjQxMzYy.XVXY4w.-CCtQSCh1AKnbIK3SPP9NGbolOY')
