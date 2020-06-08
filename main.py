"""
How it must look:
Enter your bot token: NzA5NDgzNTc2NzUxODE2NzA0.Xt57uw.EA7pbkNUle_YfPFeMHP71TJyBCE
Enter your channel id: 711919810434433105
Enter path to your file :/opt/cathook/data/chat-vlad.csv
"""
print('CATHOOK LOG-BOT')
isCorrect = False
while not isCorrect:
    print('''
+=============================+    
| 1) Create configuration file.|
| 2) Run bot                   | 
| 3) Exit                      |
+==============================+''')

    answer = int(input('--> '))
    if answer == 1:
        with open('config.py', 'w') as c:
            # bot token
            token = input('Enter your bot token: ')
            # server channel
            channel_id = input('Enter your channel id: ')
            # file path
            path = input('Enter path to your file :')
            # commands prefix
            prefix = input('Enter command prefix (like "/"): ')
            # writing data
            c.write(f'''token = "{token}"
channel = {channel_id}
file = "{path}"
prefix = "{prefix}"
            ''')
            answer = None
    elif answer == 2:
        print('[LOG] Importing discord.py...')
        try:
            import discord
            import asyncio
            from discord.ext import commands
        except ModuleNotFoundError:
            print('[ERROR] PLEASE INSTALL DISCORD.PY')

        print('[LOG] Imoprting user setting...')

        try:
            import config
        except ModuleNotFoundError:
            print('[ERROR] CREATE CONFIGURATION FILE')
            exit()
        bot = commands.Bot(command_prefix='/')  # префикс для комманд


        @bot.event
        async def on_ready():
            counter = 1
            print('[LOG] Online')
            channel = bot.get_channel(config.channel)
            await bot.change_presence(activity=discord.Game('Online!'))
            try:
                with open(config.file, 'r') as f:
                    line_on_check = f.readlines()[-1]
                while True:
                    with open(config.file, 'r') as f:
                        line = f.readlines()[-1]

                    if line != line_on_check and line != 'RELOAD':
                        line_on_check = line
                        line_on_send = line
                        line_on_send = line_on_send.replace('"', '')
                        a = line_on_send.split(',')
                        await channel.send(str(f'[LOG] {a[2]} : {a[3]}'))
                        print(f'[LOG] Message was sent ({str(counter)})')
                        counter += 1
                        with open(config.file, 'w') as f:
                            f.write('RELOAD')
                    else:
                        pass
                    await asyncio.sleep(0.5)
            except Exception as e:
                print(str(e))
        bot.run(config.token)
