import pandas as pd

df = pd.read_csv('articles.csv')
df = df.sort_values(by='n_events', ascending=False).head(10)
df.drop(columns=['n_events', 'index', 'timestamp','contentId','authorPersonId','authorSessionId','authorUserAgent','authorRegion','authorCountry','contentType', 'lang'], inplace=True)

# convert to list of dicts
_articles = list(df.to_dict('records'))
for i in _articles:
    i['title'] = i['title'].replace('\"', ' ')
