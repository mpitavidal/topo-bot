def fill_message(paper, message):
    """
    Modifies the message addint to it the information about the paper.

    Parameters
    ----------
    paper : dict
        Dictionary with information about the paper, whould at least
        have the following keys:
        "title" : Title of the paper (str).
        "link" : Link to the paper in the arXiv (str).

    message : pymsteams.connectorcard
        -----

    Doesn't return anything.
    """
    title = paper["title"]
    text = ""
    for key in paper:
        text += (key + ": " + paper[key] + "\n")
    button_text = "Go to paper in arXiv"
    paper_link = paper["link"]
    color = "#40E0D0"

    # TODO: add activity elements for authors info
    
    # Add text to the message.
    message.title(title)
    message.text(f'<pre>\n{text}\n</pre>')
    message.addLinkButton(button_text, paper_link)
    message.color(color)