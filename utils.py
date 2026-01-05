import streamlit as st
import pandas as pd
@st.cache_data
def return_data() ->pd.DataFrame :
    plot_data=pd.read_parquet('D:/spotify project/dashboard/data/df_plot_data.parquet')
    all_yeardf=pd.read_parquet('D:/spotify project/dashboard/data/df_streamliit.parquet')
    return plot_data,all_yeardf

def ret_toptrack(casse:str,data:pd.DataFrame) -> pd.DataFrame:
    match casse:
        case '1':
            data['total_minutes_played'] =data['ms_played_sum'] / (60000)
            top_tracks = data.sort_values(by='total_minutes_played', ascending=False).head(10)
            print(top_tracks)
            return top_tracks
        case '2':
            top_tracks = data.sort_values(by='track_frequency', ascending=False).head(10)
            print(top_tracks)
            return top_tracks
    
def agg_pie(casse:str,plot_data:pd.DataFrame)->pd.DataFrame:
    top_tracks=plot_data.sort_values(by='total_minutes_played',ascending=False)
    match casse:
        case '1':
            artist_pie = (
            top_tracks
            .groupby('master_metadata_album_artist_name', as_index=False).agg( {'total_minutes_played':'sum'})

            .sort_values('total_minutes_played', ascending=False)
            .head(10)
            )
            return artist_pie
        case '2':
            album_pie = (
            top_tracks
            .groupby(['master_metadata_album_album_name','master_metadata_album_artist_name','master_metadata_track_name'], as_index=False).agg( {'total_minutes_played':'sum'})

            .sort_values('total_minutes_played', ascending=False)
            .head(10)
            )
            return album_pie
        case '3':
            album_pie = (
            top_tracks
            .groupby(['master_metadata_album_album_name','master_metadata_album_artist_name','master_metadata_track_name'], as_index=False).agg( {'track_frequency':'sum'})

            .sort_values('track_frequency', ascending=False)
            .head(10)
            )
            return album_pie
        case '4':
            album_pie = (
            top_tracks
            .groupby(['master_metadata_album_album_name','master_metadata_album_artist_name','master_metadata_track_name'], as_index=False).agg( {'total_minutes_played':'sum'})

            .sort_values('total_minutes_played', ascending=False)
            .head(10)
            )
            return album_pie
        
def year_filter(year:str,allyear_df:pd.DataFrame)->pd.DataFrame:
    # print(f'{year}:class:{type(year)}')
    # print(type(allyear_df.iloc[0].year))
    # print(allyear_df.year.value_counts())
    filtered_df=allyear_df[allyear_df['year'] ==str(year)]
    return filtered_df