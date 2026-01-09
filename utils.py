import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

BASE_DIR=Path(__file__).parent
# print(BASE_DIR)
@st.cache_data
def return_data() ->pd.DataFrame :
    plot_data=pd.read_parquet(f'{BASE_DIR}/data/df_plot_data.parquet')
    all_yeardf=pd.read_parquet(f'{BASE_DIR}/data/df_streamliit.parquet')
    
    return plot_data,all_yeardf
@st.cache_data
def genre_df()->pd.DataFrame:
    return pd.read_parquet(f'{BASE_DIR}/data/df_plot_data1.parquet')

def ret_genre(casse:str,data:pd.DataFrame)->pd.DataFrame:
    match casse:
        case '1':
            data['total_minutes_played'] =data['ms_played_sum'] / (60000)
            g_data=data.groupby(['genre']).agg(freq=('genre','count'),total_minutes_played=('ms_played_sum','sum')).reset_index()
            top_genre = g_data.sort_values(by='total_minutes_played', ascending=False).head(10)
            # print(top_tracks)
            return top_genre
        case '2':
            g_data=data.groupby(['genre']).agg(genre_frequency=('genre','count')).reset_index()
            top_genre = g_data.sort_values(by='genre_frequency', ascending=False).head(10)
            # print(top_tracks)
            return top_genre

def ret_toptrack(casse:str,data:pd.DataFrame) -> pd.DataFrame:
    match casse:
        case '1':
            data['total_minutes_played'] =data['ms_played_sum'] / (60000)
            top_tracks = data.sort_values(by='total_minutes_played', ascending=False).head(10)
            # print(top_tracks)
            return top_tracks
        case '2':
            top_tracks = data.sort_values(by='track_frequency', ascending=False).head(10)
            # print(top_tracks)
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

def list_chart(df):

    data,labels=ret_ms_played_yearly(df)
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=labels,
            y=data,
            mode="lines+markers",
            marker=dict(size=10, symbol=["circle",'pentagon','hexagon','triangle-up-dot','diamond']),
            line=dict(width=2,color='green'),
            marker_color=['red','orange','blue','purple','yellow']
        )
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Total Minutes Played",
        # template="plotly_white"
        
    )

    return fig


def artist_filter(artist:str,df:pd.DataFrame)->pd.DataFrame:
    return df[df['master_metadata_album_artist_name']==str(artist)]


def ret_ms_played_yearly(df:pd.DataFrame)->tuple:
    df21=year_filter('2021',df)
    df22=year_filter('2022',df)
    df23=year_filter('2023',df)
    df24=year_filter('2024',df)
    df25=year_filter('2025',df)

    labels=['2021','2022','2023','2024','2025']
    data=[int(np.ceil(df21['ms_played_sum'].sum()/60000)),int(np.ceil(df22['ms_played_sum'].sum()/60000)),int(np.ceil(df23['ms_played_sum'].sum()/60000)),int(np.ceil(df24['ms_played_sum'].sum()/60000)),int(np.ceil(df25['ms_played_sum'].sum()/60000))]
    return data,labels