import feedparser
import datetime
path_arxiv_crawler_1 = "../"
path_arxiv_crawler_2 = "../arxiv_majorana_crawler"
import sys
sys.path.append(path_arxiv_crawler_1)
sys.path.append(path_arxiv_crawler_2)

#from arxiv_majorana_crawler import fetch_arxiv
import fetch_arxiv
import pandas as pd

QUERY_INPUT='search_query_list.txt'
DATABASE_OUTPUT='data_lastday.pkl'

def database_upd(query_input=QUERY_INPUT, database_output=DATABASE_OUTPUT):
    """
    Update the database of interesting papers and save it.
    
    Parameters
    ----------
    query_input : str
        File containing the imput to the arXiv query.

    database_output : str
        File on which the generated database is saved.

    Doesn't return anything
    """
    
    data_upd=fetch_arxiv.query_arxiv_org(query_input)

    data=pd.DataFrame(data_upd)
    def _convert_time(val):
        date = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        return date
    data['published'] = data['published'].apply(_convert_time)

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=4) #the time window of update, has to be 1 when not in test mode
    
    data_lastday = data.loc[data['published'] > (now - delta)]
    pd.to_pickle(data_lastday, database_output)
