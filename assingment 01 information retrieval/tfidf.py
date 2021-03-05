import numpy as np
from itertools import chain
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from stopwordsandstemming import tokenized_data


def return_10_keywords():

    '''converts al the lists in the field token into one list
    in order to be fitted in the tfidf vectorizer from the sklearn library
    iterates throught every document in the tokens field fits the document 
    the tfidf algorithim and returns the ten highest ranking words per document in 
    a list of lists ready to be introduced as a new field to the dataset'''

    docs = list(chain.from_iterable(tokenized_data['tokens'].to_list()))
    #converts list of lists to one list 

    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    #creates vectorizer instance, analyzer and stop words are irrelevant
    #as the items are already tokenized but it will throw an error with out it
   
    tfidf_1 = tfidf.fit_transform(docs)
    #fit_transforms all documents

    lista = []
    for item in tokenized_data['tokens'].values:
        
        '''Code adapted from a stack overflow question availabel at:
        https://stackoverflow.com/questions/34232190/scikit-learn-tfidfvectorizer-how-to-get-top-n-terms-with-highest-tf-idf-score
         '''

        respons = tfidf.transform([" ".join(item)])
        #joins item into one string and transform it into the algorithm
        feature_arr = np.array(tfidf.get_feature_names())
        #features into an np array
        sorted_tfidf = np.argsort(respons.toarray()).flatten()[::-1]
        #argsort used to sort in descending order

        top_10 = feature_arr[sorted_tfidf][:10]
        
        lista.append(top_10)
   
    return lista


'''adds a new field with 10 keywords per document based in tfidf weights'''
tokenized_data['keywords'] = return_10_keywords()

if __name__ == '__main__':
    
    '''test it works'''

    print(f'example keywords:\n{tokenized_data["keywords"].iloc[4]}')