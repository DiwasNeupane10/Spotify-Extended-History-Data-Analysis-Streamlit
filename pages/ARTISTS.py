import streamlit as st
import plotly.express as px
import pandas as pd
from plotly.express.colors import sequential as sq
from utils import return_data,artist_filter,ret_toptrack,agg_pie,ret_ms_played_yearly,list_chart
st.header("Artist Wise Filter For Drilled Down Insights")
st.set_page_config(
    page_title="ARTIST",
    layout='wide',
    page_icon='🎧'
)
st.sidebar.text('Select an artist to drill down into artist, album, and track-level insights.')
_,df=return_data()
#sort options based on frequency of the artist 
a=list(df.groupby('master_metadata_album_artist_name').agg({'track_frequency':'sum'}).reset_index().sort_values(ascending=False,by='track_frequency')['master_metadata_album_artist_name'])
artist=st.selectbox("Select an artist from the dropdown",a)
flag=st.button("Generate Insights")
filtered_df=artist_filter(artist,df)
if flag:
    row1=st.container(border=True,width='stretch',height='content')
    with row1:
        st.subheader(f"Total Listening Line Plot for {artist} Across Time Period",text_alignment='center')
    row2=st.container(border=True,width='stretch',height='content')
    with row2:
        st.plotly_chart(list_chart(filtered_df))
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
        pass
        data,labels=ret_ms_played_yearly(filtered_df)
        bar_df=pd.DataFrame({
            "Year":labels,
            "Total Minutes Played":data
        })

        st.subheader("Yearly Minutes Played",text_alignment='center')
        fig3=px.bar(bar_df,y='Total Minutes Played',x='Year',color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig3,width='content',key='fig3')       
    with chart4_col:
        st.subheader("Top Tracks Broken Down By Album",text_alignment="center")
        album_pie=agg_pie('2',filtered_df)
        fig4=px.pie(album_pie, names='master_metadata_album_album_name', values='total_minutes_played',hover_data='master_metadata_album_artist_name',labels={'master_metadata_track_name':'Track Name','total_minutes_played':'Total Minutes Played','master_metadata_album_artist_name':'Artist','master_metadata_album_album_name':'Album'},color_discrete_sequence=sq.Greens_r)
        st.plotly_chart(fig4,width='content',key='fig4')
    