from UD_functions.extract_art import get_article_page
from UD_functions.excel_export import export_to_excel
from UD_functions.database_export import export_to_db

def extract_transform_export(art_url:str):
        
        export_dict = get_article_page(art_url) # Scraping article URL for data

        if bool(export_dict): # check if empty dictionary
            # total_num_of_articles += 1
            export_to_db(export_dict, DB_name='News', table_name='Articles') # export to MongoDB
            export_to_excel(export_dict, WB_name='News', sheet_name='Articles')