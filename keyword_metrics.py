#import the libraries
import pandas as pd          
import matplotlib
from pytrends.request import TrendReq
pytrend = TrendReq()

keywords = ["Oil Tankers", "Oil Ships", "Oil Transport"]
time_span = 'today 12-m'
region='US'

def get_params(keywords, time_span, region):    
    #We add all the parameters we want to the request (filtered) 
    pytrend.build_payload(kw_list = keywords, cat=0, timeframe= time_span, geo= region, gprop='')

def get_time_trend(keywords, time_span, region):
    get_params(keywords, time_span, region)
    time_df = pd.DataFrame()
    time_df = pytrend.interest_over_time()
#     time_df = time_df.dropna(how='all',axis=0, inplace=True)
    # time_df.plot(figsize=(20, 12),  y= keywords, kind ='bar')
    print(time_df)

def keyword_suggestions(keywords):
    keywords = ["Algorand"]
    pytrend.build_payload(keywords, timeframe='today 12-m')
    trends_df = pd.DataFrame()

    trends_df = pytrend.related_queries()
    top_keywords = pd.DataFrame.from_dict(trends_df.get("Algorand").get('top'))
    top_keywords = trends_df.get("Algorand").get('top')
    # top_keywords = top_keywords[top_keywords['query'].str.contains('algorand', na=False)]
    print(top_keywords['query'])
    # for index, row in top_keywords.iterrows():
    #     print(row['query'])


# get_time_trend(keywords, time_span, region)

keyword_suggestions(keywords)