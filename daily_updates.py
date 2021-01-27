import schedule
import time
from msbot import msbot
# from telegram_bot import ???
import database_upd


def do_one_run():
    """
    TODO: Add docstring
    """
    database_upd.database_upd(query_input='search_query_list.txt', database_output="data_lastday.pkl")  # Update database with latest relevant arXiv papers
    msbot.send_msteams_update(database="data_lastday.pkl")
    # telegram_bot.send_telegram_update()
    time.sleep(120)

print("Testing")
schedule.every().day.at("12:26").do(do_one_run())

