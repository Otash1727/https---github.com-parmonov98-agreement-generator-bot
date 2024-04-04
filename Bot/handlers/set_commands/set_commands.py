from Bot.create_bot import bot,dp 
from aiogram.types import BotCommand,BotCommandScopeChat





async def set_commands(message):
    return await  bot.set_my_commands([BotCommand(command='start',description='run the bot'),BotCommand(command='menu',description='Menu')],BotCommandScopeChat(chat_id=message))
