from tfidf import tokenized_data
import os
from Indexing import es, index_data
from constant import PROCESSED_INDEX, PATH_FINAL


'''Final step processed dataset is indexed into elasaticsearch '''

fields = ['tokens', 'keywords', 'stemmed tokens']

for f in fields:
    tokenized_data[f] = tokenized_data[f].apply(" ".join)
    #alters all relevant processed fields to be treated as one strign instead of a list

if __name__ == '__main__':

    preprocessed_path = PATH_FINAL
    tokenized_data.to_csv(preprocessed_path, index=False)

    if es.indices.exists(index=PROCESSED_INDEX):
        
        '''Checks if index exists
        if it does it deletes and creates again
        executes index_data() to upload files to index'''
        
        es.indices.delete(index=PROCESSED_INDEX)
        
        response = es.indices.create(
          index=PROCESSED_INDEX,
          ignore=[400,404])
          
        print(response)
        #checks index is updated correctly
        index_data(preprocessed_path, PROCESSED_INDEX)
       
    else:
        '''if index does not exist it creates it'''
        es.indices.create(index=PROCESSED_INDEX, 
                        ignore=[400,404])

        index_data(preprocessed_path, PROCESSED_INDEX)



