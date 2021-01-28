from utils.tweetFetching import tweetFetcher
from utils.couchWriter import couchWriter

def write_user_tweets(userid):
    """
    scrapes all available tweets for the userid and writes them to the couchdb instance
    :param userid: string of twitter user id
    :return: None
    """

    tFetcher = tweetFetcher(userid)

    # prime the pump #

    response = tFetcher.fetch_tweets_upto()
    data = list(response['response'])

    while True:

        try:
            # make request with oldest id from last response #
            response = tFetcher.fetch_tweets_upto(response['oldestid'])

            data = data + list(response['response'])
        except Exception as e:

            print('Exception encountered, halting now.')
            print('{}'.format(e))

            break

    for doc in data:
        doc['authorid'] = str(userid)
    cw = couchWriter()

    cw.save_docs(docs=data, dbname='tweetbank')

    return len(data)