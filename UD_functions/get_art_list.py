# Libraries for web Scraping
import requests
from bs4 import BeautifulSoup  

# Libraries for date operations
from dateutil import parser  

def get_art_list_from_page (url: str) :
    '''
    Function to extract the links of all news article from a page (each page contains about 25 articles).
    
    | Input: URL to all news page with page number
    | Output: 1) List of article URLs in given page
            2) Publication date of the last article in the given page (to check for end of scraping) 
    '''

    art_url_list =[]
    response = requests.get(url)

    article_list = BeautifulSoup(response.text,'html.parser') # parse the news page
    links = article_list.find_all('li',attrs={'class':'clearfix'}) # extract all tags with article links
    
    for link in links:
        art_url_list.append(link.find('a').get("href")) # get link of article 
        last_article_date =  parser.parse(link.find('span').get_text(),ignoretz=True).replace(tzinfo=None).date() # get date of published article
    
    return art_url_list, last_article_date