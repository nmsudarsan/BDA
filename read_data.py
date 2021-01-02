import json
import pandas as pd
import os
import numpy as np

rootdir = 'shelves_pages'
reqd_keys = ['description', 'author', 'genre', 'img_url', 'rating_average', 'title']

def shuffle(df, n=1, axis=0):     
    df = df.copy()
    for _ in range(n):
        df.apply(np.random.shuffle, axis=axis)
        return df

paths = os.listdir(rootdir)
df_array = []

for path in paths:
    if path[-4:] != 'json': continue
    with open(rootdir+'/'+path) as f:
        genre_data = json.load(f)['books']
        for data in genre_data:
            row_values = []
            for key in reqd_keys:
                if key == 'genre':
                    if path[:4] == 'busi':
                        row_values.append('Business')
                    elif path[:4] == 'non-':
                        row_values.append('Non-Fiction')
                    elif path[:4] == 'cook':
                        row_values.append('Cooking')
                    else:
                        print('skipped: ', path[:4]) 
                        continue
                else:
                    row_values.append(data[key])
            df_array.append(row_values)
    
df = pd.DataFrame(df_array, columns=['Desc', 'author', 'genre', 'url', 'rating', 'title'])
df = shuffle(df)
df.to_csv('goodreads.csv', index=False)