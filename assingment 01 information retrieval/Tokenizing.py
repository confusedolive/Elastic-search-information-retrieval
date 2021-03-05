from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars
from constant import PATH
import nltk
import pandas as pd

tokenized_data = pd.read_csv(PATH)

def tokenization_for_index(text):
    
    ''' Given a text returns a tokenized form 
        of the text with out punctuation.'''
    ''' Punctuation is a list of punctuation to ignore when tokenizing our text
    tokenized calls the nltk function word_tokenize on the text in lower key creating
    a list of tokens, tokens variable is a list comprehension of tokenized in order to ignore 
    punctuation '''
    
    punctuation = ['!', '?', '#', '*', ')','(','[',']','@',
            '~','{','}','^','.','\u2022', ':','-','_', ',','='
            '+']
    
    tokenized = word_tokenize(text.lower())
    tokens = [word for word in tokenized if word not in punctuation]
    #lower key list containing tokenized lists per document in the specified field
    
    return tokens

'''Changing the Punktlanguagevars class  to adapt to bullet points
based on code in stackoverflow written by Julius Maximilian Steen and accesible at:
https://stackoverflow.com/questions/29746635/nltk-sentence-tokenizer-custom-sentence-starters'''

class understandbulletpoints(PunktLanguageVars):
    sent_end_chars = ('.','!', '?', '\u2022')
    #\u2022 is the bullet point so our tokenizer will understand bullet points now

def sentence_splitting(data):
    tokenizer = PunktSentenceTokenizer(lang_vars=understandbulletpoints())
    return tokenizer.tokenize(data.lower())

    #creates the tokenizer taking  calling our modified class inside variable tokenizer in order to udnerstand bulletpoints

#getting tokens as new column
tokenized_data['tokens'] = tokenized_data['title'] + tokenized_data['abstract']
tokenized_data['tokens'] = tokenized_data['tokens'].apply(tokenization_for_index)



#getting sentence tokenized as new column
tokenized_data['sentences'] = tokenized_data['title'] + tokenized_data['abstract']
tokenized_data['sentences'] = tokenized_data['sentences'].apply(lambda x: sentence_splitting(x))




if __name__ == '__main__':
    'testing it works'
    
    print(f'''example word tokens
     {tokenized_data["tokens"].iloc[3]}''')
    
    print(f'''example sentence tokens : 
    {tokenized_data["sentences"].iloc[3]}''')



  

  

    
