#!/usr/bin/env python
# coding: utf-8

import telegram 
import pandas as pd
from telegram.ext import Updater
# directory where the file with the last updates is stored:
DATABASE='..\data_lastday.pkl'
def post_the_message(database=DATABASE):
    """
    the function:
    1)launches a telegram bot with a specific token that posts a message in a channel @openmajoranachannel
    2)reads the file with the last arxiv submitions and generates a text for humans
    3)published it in the channel

    Arguments
    ---------------
    the location of the file with the last submissions -- str

    Output
    ---------------
    outputs nothing

    """

    #launch the bot:
    updater = Updater(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk', use_context=True)
    dispatcher = updater.dispatcher
    import logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    bot = telegram.Bot(token='1598945607:AAGpjZu4t7zh4Mok6baddPQ9KxZZ2ngnCbk')
    data_lastday = pd.read_pickle(database) #the read out of the file containing the recent submissions

    #generating the text to be published (as a string called 'telegram_text' )
    author_list=data_lastday['author_list']
    titles=data_lastday['title']
    published = data_lastday['published']
    links=data_lastday['link']
    ids=data_lastday['id']
    arxiv_primary_categories=data_lastday['arxiv_primary_category']
    telegram_text=" "
    for i in ids.keys():
        telegram_text=telegram_text+ published[i].strftime("%m/%d/%Y")+ "\n \n"+"'"+ titles[i]+ "'" +"\n \n"+author_list[i]+"\n"+links[i]+"\n"+arxiv_primary_categories[i] +"\n \n \n"
       #publish the generated text
        bot.sendMessage(chat_id='@openmajoranachannel', text=telegram_text)
    return 




