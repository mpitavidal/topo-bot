import schedule
import time
from msbot import msbot
from telegram_bot import post_on_tg
import database_upd


def do_one_run():
    """
    Fetch the arXive, update the database with the new relevant papers from the day
    and send update to both Teams and Telegram.
    """
    print("Started updating...")
    database_upd.database_upd(query_input='search_query_list.txt', 
                              database_output="data_lastday.pkl")
    print("Database updated at {}".format(time.time))
    msbot.send_msteams_update(database="data_lastday.pkl")
    print("Sent message to Teams at {}".format(time.time))
    post_on_tg.post_the_message(database="data_lastday.pkl")
    print("Sent message to Telegram at {}".format(time.time))


# schedule.every().day.at("12:41").do(do_one_run)
schedule.every(1).minutes.do(do_one_run)


while True:
    schedule.run_pending()
    # time.sleep(120)
    time.sleep(1)
