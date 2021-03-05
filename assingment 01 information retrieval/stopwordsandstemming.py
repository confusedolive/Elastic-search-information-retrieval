import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
import numpy as np
from constant import PATH
from Tokenizing import tokenized_data
from itertools import chain


#################removing stopwords########################
def remove_words(data, field, words_to_keep=['covid-19']):
    
    '''obtains the already tokenized text finds the most
    common 25 words excluding any selected words we want to keep
    and replaces the tokenized field with tokens not including those words'''

    stop = set(stopwords.words('english'))
    
    tokens = data[field].values

    one_list = list(chain.from_iterable(tokens))
    #joins all values in the selected field into one list
    freq = nltk.FreqDist(one_list)
    #creates a list of tuples containing word:frequency
    frequency = [x for x in freq.most_common(25)]
    
    stopped = [word for word, frq 
                in freq.most_common(25 + len(words_to_keep))
                if word not in words_to_keep]
   
    words_stopped= []

    for text in tokens:
        tkn = [word for word in text if word not in stopped and word not in stop]
        words_stopped.append(tkn)
    #filters the words and only keeps the ones that are not in stopwords
    
    data[f'{field}'] = words_stopped
    #replaces the field with the original fieldcontents without the stopwords
    
    #returns the term_frequency and stop words to be used later to filter the query
    return frequency, stopwords

#######################stemming#############################

def stemm_docs(data):
    '''uses nltk's PorterStemmer to stem words 
    in the selected field, creates a new field in the dataset
    with the stemmed words'''

    stemmer = PorterStemmer()

    stemmed_list = [stemmer.stem(word) for word in data]
  
    return stemmed_list


'''executes the functions, adding the required fields into the dataset'''

stopwords = remove_words(tokenized_data, 'tokens')
#provides the list of stopwords used should be used in the future for querying purposes

tokenized_data['stemmed tokens'] = tokenized_data['tokens'].apply(stemm_docs)
#creates stemmed tokesn fields applying  the stemm_docs function to the tokens field

if __name__ == '__main__': 
    
    '''testing it works'''
   
    print(f'example stemmer: {tokenized_data["stemmed tokens"].iloc[3]}')
    #print(tokenized_data['tokens'].iloc[3])



    
