from utils.tweetFetching import tweetFetcher
from utils.couchWriter import couchWriter

import pandas as pd

from utils.pop_tweets import write_user_tweets


cw = couchWriter()

couch = cw.start_session()  #need a couch onject for querying

# pull in all users so we can get tweets for everyone
db = couch['data_profiles']

rows = db.view('_all_docs', include_docs=True)
data = [row['doc'] for row in rows]
df = pd.DataFrame(data)

for user,name in zip(df.id.values,df.Twitter.values):
    count = write_user_tweets(str(user))
    print('Grabbed {} tweets for {}'.format(count,user))
    print("!----------------------------------------------!")
