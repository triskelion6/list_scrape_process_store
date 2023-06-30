# Libraries for text cleaning and niose removal
import unidecode
import re

def text_cleaner(input_text:str):
    ''' 
    Function for noise removal and text cleaning.
    Operations: lower casing, remove non-unicode characters, remove links, remove numbers, remove extra spaces. 

    | Input: raw text
    | Output: processed text
    '''
    
    input_text = unidecode.unidecode(input_text) # removes non-breaking white spaces

    input_lower = input_text.lower() # lower case all characters

    clean1 = re.sub(r"(@[a-z0-9]+)|([^a-z \t])|(\w+:\/\/\S+)|\bwww\.[^\s]+|http.+?", "", input_lower)
    # @[A-Za-z0-9] matches @ mentions, email addresses
    # [^0-9A-Za-z \t] matches non alphabet characters
    # \w+:\/\/\S+ matches URLs
    # \bwww\.[^\s] matches web addresses starting with www
    # http.+? matches URL starting with http

    processed_text = re.sub("(\s){2,}", " ", clean1) # remove extra spaces

    return processed_text
