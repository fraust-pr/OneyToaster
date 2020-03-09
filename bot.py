import discord, os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix="!")
status = cycle(['Kicking Ass', 'Kicking Ass Again', 'Kicking some more Ass', 'Kicking even more Ass', 'When can i book myself to kick Super Dragon`s Ass'])

@client.event
async def on_ready():
    change_status.start()
    print( "{0.user} IS HERE TO KICK ASS".format(client))

async def on_member_join(member):
    print(f'{member} KICK ASS KICK ASS KICK ASS')

async def on_memeber_remove(member):
    print(f'{member} YOU SUNAVA BITCH!')

async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('SUPER DRAGON MESSED WITH THIS ARGUMENT')

@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('point'):
        await message.channel.send('https://imgur.com/ZwSodOR', delete_after=10)
    if message.content.startswith('point up'):
        await message.channel.send('\U0001f446', delete_after=10)
    if message.content.startswith('oney lorcan'):
        await message.channel.send('ON THE PLANE I WAS IN THE WINDOW SEAT AND WHEN I PUT THE WINDOW SHADE DOWN LADY NEXT TO ME SAYS TO ME SHE SAYS OH NO I NEED THE SHADE UP AND I JUST LOOKED HER DIRECTLY IN THE EYES AND ASKED IF SHE HAD EVER DANCED WITH THE DEVIL IN THE PALE MOONLIGHT THEN I PUT THE SHADE UP', delete_after=15)
    if message.content.startswith('god'):
        await message.channel.send('THE WRESTLING GODS HAVE SPOKEN I MUST KICK ASS', delete_after=15)   
    if message.content.startswith('put em up'):
        await message.channel.send('https://imgur.com/o0I4n6Y \U0000261D', delete_after=10)
    if message.content.startswith('based'):
        await message.add_reaction('\U0000261D')
    if message.content.startswith('dog'):
        await message.channel.send('I LOVE MY FRIGGIN DOG THROW EM UP \U0001f446', delete_after=15)
    if message.content.startswith('Today'):
        await message.channel.send('LETS KICK TODAYS ASS THROW EM UP \U0001f446', delete_after=15)
    if message.content.startswith('kick'):
        await message.channel.send('https://www.youtube.com/watch?v=bBew7TRA5W4', delete_after=10)
    
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms', delete_after=10)



@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjcyNTQwODIzNzExMTIxNDUw.Xlqu_A.n5gXbndIzNviyQzK_J0DycQgc3c')