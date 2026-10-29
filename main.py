import asyncio
from telethon import TelegramClient, events

api_id = '24785476'
api_hash = '4089bb9a026bd4bf99904343329f'
phone = '+923469827956'
client = TelegramClient('aayco', api_id, api_hash)

@client.on(events.NewMessage())
async def handle_action(event):
    me = await client.get_me()
    try:
        if event.is_private and event.sender_id != me.id:
            async with client.action(event.chat_id, 'game'):
                await asyncio.sleep(8)
    except Exception as e:
        await event.reply(str(e))

with client:
    client.start(phone=phone)
    client.run_until_disconnected()
