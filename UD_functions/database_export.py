# Libraries for export to database
from pymongo import MongoClient

def export_to_db(dict_to_db:dict, DB_name:str, table_name:str):
    ''' 
    Function to export dictionary containing article details to MongoDB. 

    | Input: dictionary for export, Database name, Table name
    '''

    client=MongoClient('mongodb://192.168.1.2:27017') # connect to database
    db=client[DB_name] # access database, if not exist then create database
    collection = db[table_name] # access table/collection, create it not exist

    collection.insert_one(dict_to_db) # store dictionary in table/collection