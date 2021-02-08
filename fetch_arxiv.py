import os, sys, urllib, platform
import feedparser
from datetime import datetime
import database_manipulation
import pandas as pd

QUERY_INPUT = 'search_query_list.txt'
DB_OUTPUT = 'dummydatabase.pkl'
HTML_OUTPUT = 'arxiv_crawler.html'

# easy way to publish: run on a TUD desktop and save it to the university personal page
if platform.system() == 'Windows':
    HTML_DIR = 'H:/www'
else:
    HTML_DIR = '~/Desktop'


def query_arxiv_org(debug_mode=True, query_input=QUERY_INPUT):
    """Search for query items on arXiv and return the list of results"""

    def _convert_time(val):
        """Changes the date-time string format"""
        date = datetime.strptime(val,'%Y-%m-%dT%H:%M:%SZ')
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def _remove_newlines(val):
        """Strips line breaks from the title string"""
        return val.replace('\n  ', ' ')

    def _join_authors(val):
        """Makes a single string as the author list"""
        return ', '.join([val[i]['name'] for i in range(len(val))])

    # Construct elements of the query string sent to arxiv.org:
    # Base api query url
    base_url = 'http://export.arxiv.org/api/query?'
    # each search item
    with open(query_input) as file:
        search_keywords = file.readlines()
    # some options
    start = 0
    max_results = 50 # see arXiv API for max result limits
    sorting_order = '&sortBy=submittedDate&sortOrder=descending'

    result_list = []

    # search for the keywords/authors one by one
    for search_query in search_keywords:
        query = 'search_query=%s&start=%i&max_results=%i' % (search_query.rstrip(),
                                                            start,
                                                            max_results)

        d = feedparser.parse(base_url+query+sorting_order) # actual querying

        for entry in d.entries:
            dic_stored = {}
            dic_stored['id'] = entry.id.split('/')[-1].split('v')[0]
            dic_stored['author_list'] = _join_authors(entry.authors)
            dic_stored['title'] = _remove_newlines(entry.title)
            dic_stored['arxiv_primary_category'] = entry.arxiv_primary_category['term']
            dic_stored['published'] = _convert_time(entry.published)
            dic_stored['link'] = entry.link
            result_list.append(dic_stored)

    return result_list


def main(debug_mode=True, db_output=DB_OUTPUT, html_dir=HTML_DIR, html_output=HTML_OUTPUT):

    if debug_mode:
        print('Beginning query: ', datetime.now())
    result_list = query_arxiv_org()
    if debug_mode:
        print('Query successful: ', datetime.now())

    # create a new empty data frame if failed to read an existing DB with the same name
    try:
        old_db = pd.read_pickle(db_output)
    except: 
        old_db = pd.DataFrame()
    
    new_db = pd.DataFrame(result_list)
    updated_db = database_manipulation.update_database(old_db, new_db)
    if debug_mode:
        print('Database updated: ', datetime.now())

    pd.to_pickle(updated_db, db_output)
    if debug_mode:
        print('pkl written: ', datetime.now())

    database_manipulation.create_html(updated_db, os.path.join(html_dir, html_output))
    print('Done writing HTML: ', datetime.now())


if __name__ == '__main__':
    main()
