import pandas as pd
import msbot
import pymsteams

DATABASE = '..\data_lastday.pkl'
# Define Microsoft Webhook URL
ADDRESS_GENERAL = "https://tud365.webhook.office.com/webhookb2/b30f04eb-e52a-4b70-9920-d9e52953b8ca@096e524d-6929-4030-8cd3-8ab42de0887b/IncomingWebhook/9f828c3733af424a8fdb5875c373b239/e21735a8-e851-494f-99ba-2e0e9cfe3b6d"
ADDRESS_ARXIV = "https://tud365.webhook.office.com/webhookb2/b30f04eb-e52a-4b70-9920-d9e52953b8ca@096e524d-6929-4030-8cd3-8ab42de0887b/IncomingWebhook/e8044a75137048fcb8eb0d604c097e2e/e21735a8-e851-494f-99ba-2e0e9cfe3b6d"

def send_msteams_update(database=DATABASE, address=ADDRESS_ARXIV):
    """
    For each of the papers in a database, sends a message to a teams channel
    containing information about the paper.

    Parameters
    ----------
    database : str
        File containing the database.

    address : str
        Address to the Microsoft Webhook for the channel of interest.

    Doesn't return anything.

    """
    
    data_lastday = pd.read_pickle(database)

    n_papers = len(data_lastday["title"])   # Number of papers in the dataframe

    for i in range(n_papers):
        
        # Create the connectorcard object with the Microsoft Webhook 
        message = pymsteams.connectorcard(address)
        fill_message(data_lastday, i, message)
        message.send()



def fill_message(data_lastday, index_paper, message):
    """
    Modifies the message adding to it the information about a paper.

    Parameters
    ----------
    data_lastday : pandas.core.frame.DataFrame
        Should at least have the following elements:
        "title" : Title of the paper (str).
        "link" : Link to the paper in the arXiv (str).

    index_paper : int
        Index of the paper in the dataframe.

    message : pymsteams.connectorcard
        Message to update with the information of the paper.

    Doesn't return anything.
    """
        
    title = data_lastday["title"][index_paper]
    text = ""
    for key in data_lastday:
        text += (key + ": " + str(data_lastday[key][index_paper]) + "\n")

    button_text = "Go to paper in arXiv"
    paper_link = data_lastday["link"][index_paper]
    color = "#40E0D0"

    # TODO: add activity elements for authors info
    
    # Add text to the message.
    message.title(title)
    message.text(f'<pre>\n{text}\n</pre>')
    message.addLinkButton(button_text, paper_link)
    message.color(color)