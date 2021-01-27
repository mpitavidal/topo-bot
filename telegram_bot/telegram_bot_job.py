path_arxiv_crawler = "C:\\Users\\tesya\\OneDrive\\Документы\\GitHub\\arxiv_majorana_crawler"
import sys
sys.path.append(path_arxiv_crawler)
import fetch_arxiv
import feedparser
import datetime

import pandas as pd
QUERY_INPUT = 'C:\\Users\\tesya\\OneDrive\\Документы\\GitHub\\arxiv_majorana_crawler\\search_query_list.txt'

def bot_job():
    data_upd=fetch_arxiv.query_arxiv_org(query_input=QUERY_INPUT)


    data=pd.DataFrame(data_upd)
    def _convert_time(val):
        date = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        return date
    data['published'] = data['published'].apply(_convert_time)

   
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=2)
    

    data_lastday = pd.DataFrame.to_dict(data.loc[data['published'] > (now - delta)])
    author_list=data_lastday['author_list']
    titles=data_lastday['title']
    published = data_lastday['published']
    links=data_lastday['link']
    ids=data_lastday['id']
    arxiv_primary_categories=data_lastday['arxiv_primary_category']
    telegram_text=" "
    for i in list(ids):
        telegram_text=telegram_text+ published[i].strftime("%m/%d/%Y")+ "\n \n"+"'"+ titles[i]+ "'" +"\n \n"+author_list[i]+"\n"+links[i]+"\n"+arxiv_primary_categories[i] +"\n \n \n"


  
    import telegram 
    from telegram.ext import Updater
    updater = Updater(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk', use_context=True)
    dispatcher = updater.dispatcher
    import logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    bot = telegram.Bot(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk')

    bot.sendMessage(chat_id='@openmajoranachannel', text=telegram_text)
    return 







