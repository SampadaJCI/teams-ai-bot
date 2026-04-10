import os
from dotenv import load_dotenv
from botbuilder.core import BotFrameworkAdapter, ConversationState, MemoryStorage
from botbuilder.schema import Activity

load_dotenv()

class TeamsAIBot:
    def __init__(self):
        self.app_id = os.getenv("BOT_ID")
        self.app_password = os.getenv("BOT_PASSWORD")
        self.adapter = BotFrameworkAdapter(self.app_id, self.app_password)
        
    async def on_message_activity(self, turn_context):
        await turn_context.send_activity("Hello from Teams AI Bot!")

async def main():
    bot = TeamsAIBot()
    print("Teams AI Bot started successfully!")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
