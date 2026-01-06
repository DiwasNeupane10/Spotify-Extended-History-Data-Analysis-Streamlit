
import streamlit as st
import pandas as pd
from utils import return_data,list_chart
st.set_page_config(
    page_title="ABOUT",
    layout='wide',
    page_icon='🎧'
)
st.title("SPOTIFY EXTENDED HISTORY DATA ANALYSIS",text_alignment='center')
st.sidebar.text("🎵 A visual analysis of my Spotify Extended Streaming History, highlighting trends, favorites, and listening behavior over time.")
_,df=return_data()
def convert_time(df:pd.DataFrame)->str:
    total_ms=df['ms_played_sum'].sum()
    total_seconds = total_ms / 1000
    # print(total_seconds)
    # Compute days, hours, minutes, seconds
    days = int(total_seconds // 86400)
    hours = int((total_seconds % 86400) // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    # Format as "Xd Xh Xm Xs"
    total_listening_time = f"{days}d {hours}h {minutes}m {seconds}s"
    return total_listening_time
total_listening_time=convert_time(df)
kpi=st.container(border=True,width='stretch',height='content')
kpi_info = pd.DataFrame([{
    "Name": "Diwas Neupane",
    "Time-Range": "2021 - 2025",
    "Total Listening Duration":total_listening_time
}])


with kpi :
    row1=st.container(border=True,width='stretch',height='content')
    with row1:
        col1,col2,col3=st.columns(3,width='stretch')
        with col1:
            st.subheader("Name",text_alignment='justify')
        with col2:
            st.subheader(":",text_alignment='justify')
        with col3:
            st.subheader("Diwas Neupane",text_alignment='justify')
    row2=st.container(border=True,width='stretch',height='content')
    with row2:
        col4,col5,col6=st.columns(3,width='stretch')
        with col4:
            st.subheader("Time Range",text_alignment='justify')
        with col5:
            st.subheader(":",text_alignment='justify')
        with col6:
            st.subheader("2021-2025",text_alignment='justify')
    row3=st.container(border=True,width='stretch',height='content')
    with row3:
        col7,col8,col9=st.columns(3,width='stretch')
        with col7:
            st.subheader("Listening Duration",text_alignment='justify')
        with col8:
            st.subheader(":",text_alignment='justify')
        with col9:
            st.subheader(total_listening_time,text_alignment='justify')
    row4=st.container(border=True,width='stretch',height='content')
    with row4:
        st.subheader("Total Listening Line Plot Across Time Period",text_alignment='center')
    row5=st.container(border=True,width='stretch',height='content')
    with row5:
        st.plotly_chart(list_chart(df))

