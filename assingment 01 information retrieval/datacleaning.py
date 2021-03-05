import pandas as pd
from langdetect import detect
import os
from constant import ORIGINAL


data = ORIGINAL

def clean_csv(path, name_of_new_file=r'Datasets\New metadata 1000.csv'):
  
    ''' Uses pandas DataFrame structures to clean and filter the data
        drops rows on which  abstract title,authors and publish date are missing values  
        samples 2500 rows which are boolean checked to see if
        the abstract is written in English then 1000 random samples
        from that sample are used to create a new filtered dataset in a csv file
        containin 1000 rows which is saved as New metadata 1000 in a new folder in
        your current working directory called datasets returns that same dataset
        '''
    df_1 = pd.read_csv(data)
    print(f'Original length of dataset: {len(df_1)}')
    df_2 = df_1.copy()
    df_2.dropna(subset=['title','abstract',
                        'authors','publish_time',
                        'journal','source_x'], 
                        inplace=True)
    print(f'Length of dataset after dropping relevant missing values {len(df_2)}')
    df_2 = df_2.sample(n=2500)
    
    '''Langdetect throws an error if it doesnt understand
    certain characters therefore df[field].apply(detect)=='en'
    will throw errors if it encounters unknown chars
    different method had to be implemented'''

    in_english = []
    for text in df_2['abstract'].values:
        try:
            if detect(text) == 'en':
                in_english.append(text)
            else:
                continue
        except :
            continue

    df_final = df_2[df_2['abstract'].apply(lambda x: x in in_english)].copy()
  
    print(len(df_final))
    df_real = df_final.sample(n=1000).copy()
    #random sample of 1000
    df_real.to_csv(os.path.join(os.getcwd(),name_of_new_file), index=False)
    
    return df_real

if __name__ == '__main__':
    clean_csv(data)

