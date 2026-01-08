import json
import pandas as pd
def jsonl_parqquet(df:pd.DataFrame)->None:
    dict={}
    with open("D:/spotify project/dashboard/artist_genres.jsonl","r",encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                data=json.loads(line)
                dict[data['artist']]=data['tags'][0]['name']
    df['genre']=df['master_metadata_album_artist_name'].map(dict)
    df.to_parquet('D:/spotify project/dashboard/data/df_plot_data1.parquet')

                

jsonl_parqquet(pd.read_parquet('D:/spotify project/dashboard/data/df_plot_data.parquet'))


df=pd.read_parquet('D:/spotify project/dashboard/data/df_plot_data1.parquet')
print(df.genre.value_counts())
