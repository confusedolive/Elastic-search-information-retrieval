from Indexing import es
from constant import INDEX_NAME, PROCESSED_INDEX
import pandas as pd
import numpy as np


def get_source_items(query, indx=PROCESSED_INDEX):
    ''' converts index obtained from 
    elastic search by querying
    match all into a pandas dataframe'''
    
    res = es.search(index=indx, body=query, size=1000)
    data = res['hits']['hits']

    '''Code based on blog available at:
    https://kb.objectrocket.com/elasticsearch/how-to-use-elasticsearch-data-using-pandas-in-python-349
    written by Rockets Admin june 10/2019'''

    fields = {}
    for doc in data:
        source_data = doc['_source']
        for key, val in source_data.items():
            try:
                fields[key] = np.append(fields[key], val)
            except :
                fields[key] = np.array([val])

    
    return pd.DataFrame(fields)

def test1(indx):
    
    while True:
        question = input('press enter to continue or type quit to exit:\n -->')
        if question == 'quit':
            break
        field = input('what field would you like to search:\n--> options: abstract, title, journal:\n--> ')
        search = input('what are you looking for> \n -->')
        
        query = {
            "query": {
                "match":{f"{field}": f"{search}"}
            }
        }
        try:
            res = es.search(index=indx, body=query, size=1000)
            response = get_source_items(query)[field].values
            print(f'Total found: {len(response)}')
            for n, item in enumerate(response[:5]):
                print(f'match {n+1}:\n {item}\n')
        except :
            print('no matches')

specify_query()

