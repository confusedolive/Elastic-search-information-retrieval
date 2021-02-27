import pandas as pd
from langdetect import detect

df = pd.read_csv('metadata.csv')
df1 = df.copy()

def clean_csv(df_1=df1):
    df_1.dropna(subset=['title','abstract'], inplace=True)
#   df_1.dropna(subset=['title', 'abstract'], inplace=True)
    df_1.fillna('nan',inplace=True)
#length of dataset is 107028, dropping missing values in columns title and abstract
#filtering by articles written in 2020 and published by WHO
#random sample of 5000 to ease the computing process
    df_1 = df_1.sample(n=5000)
    df_final = df_1[df_1['title'].apply(detect) == 'en']
#filter choosing only articles which titles are at least in english 
    df_real = df_final.sample(n=1000).copy()
#random sample of 1000
    df_real.to_csv('modified set.csv', index=False)

clean_csv()

