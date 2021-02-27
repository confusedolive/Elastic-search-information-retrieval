import csv
from elasticsearch import helpers, Elasticsearch
from constants import name_index, docu_type

es = Elasticsearch()
#no need to specify host as we are doing it locally
es.indices.delete(index=name_index)
es.indices.create(index=name_index, ignore=400)
with open(r'C:\Users\jeron\OneDrive\Desktop\university\CE306\Elastic_search\modified set.csv', encoding='utf8', mode='r') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader,index=name_index, doc_type=docu_type)
    

