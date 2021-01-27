import schedule
import time
from msbot import msbot
# from telegram_bot import ???
import database_upd


def do_one_run():
    """
    TODO: Add docstring
    """
    database_upd.database_upd()  # Update database with latest relevant arXiv papers
    msbot.send_msteams_update()
    # telegram_bot.send_telegram_update()
    time.sleep(120)

schedule.every().day.at("12:26").do(do_one_run())

