from django.core.management.base import BaseCommand
from Bot.create_bot import dp,bot
from Bot.handlers import main

class Command(BaseCommand):
    help='Otabek'
    def handle(self,*args, **kwargs):
        print('Bot online....')
        dp.include_router(main.router)
        dp.run_polling(bot)