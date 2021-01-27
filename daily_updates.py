import schedule
import time
import msbot
import database_upd

schedule.every().day.at("10:10").do(do_one_run())


def do_one_run():
    database_upd.database_upd()  # Update database with latest relevant arXiv papers
    msbot.send_msteams_update()
    telegram_bot.send_telegram_update()
    time.sleep(120)
