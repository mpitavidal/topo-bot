def fill_message(paper, message):
    """
    .......

    Parameters
    ----------
    paper : dictionary
        ----
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