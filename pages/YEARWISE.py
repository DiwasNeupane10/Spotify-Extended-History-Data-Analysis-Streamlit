import streamlit as st
from utils import year_filter,ret_toptrack,return_data,agg_pie
import plotly.express as px
from plotly.express.colors import sequential as sq
st.header("Yearwise Filter For Drilled Down Insights")
st.set_page_config(layout='wide')
input_container=st.container()
with input_container:
    year=st.selectbox("Select a year",[2021,2022,2023,2024,2025])
    flag=st.button("Generate Insights")
_,all_yeardf=return_data()
# print(all_yeardf.head(5))
if flag:
    filtered_df=year_filter(year,all_yeardf)
    # print("XXX"*10)
    # print(filtered_df.head(5))
    chart1_col,chart2_col=st.columns(2,border=True,width='stretch')
    with chart1_col:
        st.subheader("Top 10 Tracks: Minutes Played",text_alignment="center")
        top_tracks_df=ret_toptrack('1',filtered_df)
        fig1=px.bar(top_tracks_df,y='master_metadata_track_name',x='total_minutes_played',color='master_metadata_album_artist_name',labels={'master_metadata_track_name':"Track Name",'total_minutes_played':'Minutes Played','master_metadata_album_artist_name':'Artist'},color_discrete_sequence=sq.Greens_r)
        fig1.update_layout(legend_title_text=None)
        # print(filtered_df.shape)
        st.plotly_chart(fig1,width='content',key='fig1')

    with chart2_col:    
        st.subheader("Top 10 Tracks: Frequency",text_alignment="center")
        top_tracks_df=ret_toptrack('2',filtered_df)
        fig2=px.bar(top_tracks_df,y='master_metadata_track_name',x='track_frequency',color='master_metadata_album_artist_name',labels={'master_metadata_track_name':"Track Name",'track_frequency':'Track Frequency','master_metadata_album_artist_name':'Artist'},color_discrete_sequence=sq.Greens_r)
        fig2.update_layout(legend_title_text=None)
        st.plotly_chart(fig2,width='content',key='fig2')

    chart3_col,chart4_col=st.columns(2,border=True,width='stretch')
    with chart3_col:
        st.subheader("Top 100 Tracks Broken Down By Artist",text_alignment="center")
        artist_pie=agg_pie('1',filtered_df)
        fig3=px.pie(artist_pie, names='master_metadata_album_artist_name', values='total_minutes_played',hover_data='master_metadata_album_artist_name',labels={'master_metadata_track_name':"Track Name",'total_minutes_played':'Total Minutes Played','master_metadata_album_artist_name':'Artist'},color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig3,width='content',key='fig3')
    with chart4_col:
        st.subheader("Top 100 Tracks Broken Down By Album",text_alignment="center")
        album_pie=agg_pie('2',filtered_df)
        fig4=px.pie(album_pie, names='master_metadata_album_album_name', values='total_minutes_played',hover_data='master_metadata_album_artist_name',labels={'master_metadata_track_name':'Track Name','total_minutes_played':'Total Minutes Played','master_metadata_album_artist_name':'Artist','master_metadata_album_album_name':'Album'},color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig4,width='content',key='fig4')
    #Row 3
    chart5_col,chart6_col=st.columns(2,border=True,width='stretch')
    with chart5_col:
        st.subheader("Top 10 Frequent Tracks in Top Album",text_alignment="center")
        fig5 = px.sunburst(agg_pie('3',filtered_df
), path=['master_metadata_album_artist_name','master_metadata_album_album_name','master_metadata_track_name'], values='track_frequency',color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig5,width='content',key='fig5')
    with chart6_col:
        st.subheader("Top 10 Tracks in the Top Album",text_alignment="center")
        fig5 = px.sunburst(agg_pie('4',filtered_df
), path=['master_metadata_album_artist_name','master_metadata_album_album_name','master_metadata_track_name'], values='total_minutes_played',color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig5,width='content',key='fig6')