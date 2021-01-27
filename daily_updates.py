import schedule
import time
from msbot import msbot
from telegram_bot import post_on_tg
import database_upd


def do_one_run():
    """
    TODO: Add docstring
    """
    print("Updating")
    # Update database with latest relevant arXiv papers
    database_upd.database_upd(query_input='search_query_list.txt', 
                              database_output="data_lastday.pkl")
    msbot.send_msteams_update(database="data_lastday.pkl")
    post_on_tg.post_the_message()


schedule.every().day.at("12:34").do(do_one_run)
# schedule.every(1).minutes.do(do_one_run)


while True:
    schedule.run_pending()
    time.sleep(120)
