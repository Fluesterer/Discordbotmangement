import discord
import threading

class DiscordBot:
    def __init__(self):
        self.client = None
        self.token = None
        self.running = False
        self.activity = None

    def start_bot(self, token, activity_type=None, activity_text=None):
        self.token = token
        intents = discord.Intents.default()
        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():
            print(f'Bot is online as {self.client.user}')
            if activity_type and activity_text:
                await self.set_activity(activity_type, activity_text)

        def run():
            self.running = True
            self.client.run(token)
        
        thread = threading.Thread(target=run)
        thread.start()

    async def set_activity(self, activity_type, activity_text):
        activity_types = {
            "playing": discord.ActivityType.playing,
            "streaming": discord.ActivityType.streaming,
            "listening": discord.ActivityType.listening,
            "watching": discord.ActivityType.watching,
        }

        if activity_type in activity_types:
            activity = discord.Activity(type=activity_types[activity_type], name=activity_text)
            await self.client.change_presence(activity=activity)

    def stop_bot(self):
        if self.client:
            self.running = False
            loop = self.client.loop
            loop.call_soon_threadsafe(loop.stop)

bot_instance = DiscordBot()
