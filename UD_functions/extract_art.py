# Libraries for web Scraping
import requests
from bs4 import BeautifulSoup  

# import text_cleaner for textcleaning and noise removal
from UD_functions.text_cleaner import text_cleaner

def get_article_page (art_url:str):
    ''' 
    Function to extract and process news article from URL of article. 
    Extracted parameters: Title of article, Publication date, Text body of article. 
    Text body is further cleaned using text_cleaner() function.
    Returns dictionary which is ready for export and data storage. 
    Returns empty dictionary if the URL is not a news article or if any error is encountered during parsing.

    | Input: URL of article
    | Output: Dictionary with following keys: 'URL', 'Title', 'Publish_Date', Content' 
            Empty dictionary returned if any anomolous cases(mentioned above) are found
    '''

    try:
                
        article_full_content = []
        get_article = requests.get(art_url)
        
        article_soup_obj = BeautifulSoup(get_article.content,'html.parser') # parse page 
        article_title = article_soup_obj.find("h1",attrs={"class":"article_title artTitle"}).get_text() # get article title
        article_date =  article_soup_obj.find("div",attrs={"class":"article_schedule"}).find('span').get_text() # get article date
        article_body =  article_soup_obj.find("div",attrs={"class":"content_wrapper arti-flow"}) # locate article content
        article_paragraphs = article_body.findAll("p") # locate paragraphs in article content
        for i in article_paragraphs:
            article_full_content.append(i.get_text()) # extract text from paragraph

        article_full_content = ' '.join(article_full_content) # combine all paragraph contents
        
        # call text_cleaner() for processing the text content
        article_full_content = text_cleaner(article_full_content) 

        # create dictionary for export
        export_dict = {'URL': art_url, 'Title': article_title, 'Publish_Date': article_date, 'Content': article_full_content}
        return export_dict    
    except:
        return {}