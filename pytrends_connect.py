import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

# Get Google Keyword Suggestions
keywords = pytrend.suggestions(keyword='covid')
df = pd.DataFrame(keywords)
print(df.head(5))