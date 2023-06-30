from UD_functions.get_art_list import get_art_list_from_page
# from UD_functions.extract_art import get_article_page
# from UD_functions.excel_export import export_to_excel
# from UD_functions.database_export import export_to_db
from UD_functions.comined_operations import extract_transform_export
import concurrent.futures
import time

import datetime
from datetime import timedelta

if __name__=="__main__":

    start = time.time()
    num_of_days_to_scrape = 30 
    run_start_date = datetime.datetime.now().date() # date at time of program execution
    page_last_article_date = datetime.datetime.now().date() # variable definition to enter loop, will be updated after entering loop 
    last_date_for_extraction = run_start_date - timedelta(days=num_of_days_to_scrape) # last date till when article must be extracted 

    # variable initializations
    page_no = 1
    full_list_art = [] 

    while page_last_article_date >= last_date_for_extraction: # main loop | checking date for end condition
        url = 'https://www.moneycontrol.com/news/news-all/page-' + str(page_no) + '/'  # All News page URL of news website with page number  
        
        art_url_list, page_last_article_date = get_art_list_from_page(url) # get list of URLs from given page, get publish date of last article in given page

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(extract_transform_export,art_url_list)

        ### The multithreading increases the program speed by 3-4 times when compared to the for-loop below

        # for art_url in art_url_list: # loop to iterare elements in list of article URL 

        #     export_dict = get_article_page(art_url) # Scraping article URL for data

        #     if bool(export_dict): # check if empty dictionary
        #         total_num_of_articles += 1
        #         export_to_db(export_dict, DB_name='News', table_name='Articles') # export to MongoDB
        #         export_to_excel(export_dict, WB_name='News', sheet_name='Articles') # export to Excel file 
                
        print('Date processed: ', page_last_article_date, '|| Page no: ', page_no, end="\r")
        page_no += 1  # move to next page in article list page 

    print('Date processed: ', page_last_article_date, '|| Page no: ', page_no)
    total_time = time.time() - start
    print('Time taken: ', total_time//60, ' minutes, ', round(total_time%60,0), ' seconds')