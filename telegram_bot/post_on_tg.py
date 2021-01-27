import telegram 
import pandas as pd
from telegram.ext import Updater
#DATABASE='..\data_lastday.pkl'
def post_the_message(database):
    updater = Updater(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk', use_context=True)
    dispatcher = updater.dispatcher
    import logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    bot = telegram.Bot(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk')
    data_lastday = pd.read_pickle(database)
    author_list=data_lastday['author_list']
    titles=data_lastday['title']
    published = data_lastday['published']
    links=data_lastday['link']
    ids=data_lastday['id']
    arxiv_primary_categories=data_lastday['arxiv_primary_category']
    telegram_text=" "
    for i in ids.keys():
        telegram_text=telegram_text+ published[i].strftime("%m/%d/%Y")+ "\n \n"+"'"+ titles[i]+ "'" +"\n \n"+author_list[i]+"\n"+links[i]+"\n"+arxiv_primary_categories[i] +"\n \n \n"
        bot.sendMessage(chat_id='@openmajoranachannel', text=telegram_text)
    return 
