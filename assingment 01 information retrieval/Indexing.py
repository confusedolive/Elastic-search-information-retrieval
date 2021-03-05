import csv
import pandas as pd
from elasticsearch import helpers, Elasticsearch
from constant import INDEX_NAME , PATH
import warnings



'''Used to avoid getting the same message everytime we create an index, 
to be changed when features actually get depecrated and new implementations are updated'''
warnings.filterwarnings("ignore", category=DeprecationWarning)

es = Elasticsearch()
#no need to specify host as we are doing it locally
data_path = PATH
#path to the modified dataset containing 1000 docs

def index_data(path, ind):
    '''Uploads documents from a csv file 
    uses  helpers.bulk to upload at the same time to INDEX_NAME'''
    with open(path, encoding='utf8', mode='r') as indx:
        reader = csv.DictReader(indx)
        helpers.bulk(es, reader, index=ind)

if __name__ == '__main__':
    if es.indices.exists(index=INDEX_NAME):
        
        '''Checks if index exists
        if it does it deletes and creates again
        executes index_data() to upload files to index'''
        
        es.indices.delete(index=INDEX_NAME)
        response = es.indices.create(
          index=INDEX_NAME, 
          ignore=[400,404]
          )
        
        print(response)
        #checks index is updated correctly
        index_data(PATH, ind=INDEX_NAME)
    else:
        '''if index does not exist it creates it'''
        es.indices.create(index=INDEX_NAME)
        
        index_data(PATH, ind=INDEX_NAME)


    

