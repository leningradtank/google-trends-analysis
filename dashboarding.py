import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns       
import matplotlib
from pytrends.request import TrendReq

pytrend = TrendReq()
kw_list=["Algorand", "Aave", "Solana"]
#We add all the parameters we want to the request (filtered) 
pytrend.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='US', gprop='')
time_df = pytrend.interest_over_time()


st.title('Google Search Popularity for Keywords')
st.text('This is a web app to allow exploration of Recession Data')
# st.subheader('Dataset')
# st.dataframe(time_df)
# st.subheader('Data Numerical Statistic')
# st.dataframe(time_df.describe())
st.subheader('12 Month Historical Search Popularity & Trends for Keywords')
st.line_chart(data=time_df, y=kw_list, use_container_width=True)

