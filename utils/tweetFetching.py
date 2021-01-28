import requests
import time

class tweetFetcher:
    """
    what is my purpose?
    You fetch tweets
    [defeated] Oh my god.
    """

    def __init__(self,
                 userid,
                 payload={},
                 headers={
                     'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAEhtMAEAAAAAHfK0FC55xEmzHqWJBiFsrltb%2Fko%3DV7T7qccL9QQM17H2qZFqjeiySOmNi9q5bQzdUggSPIvZUDVgyG',
                     'Cookie': 'guest_id=v1%3A161159767509161000; personalization_id="v1_kgQY5ZcY+Qo7QzTK1th10Q=="'
                 }
                 ):
        self.user = userid
        self.payload = payload
        self.headers = headers
        self.url = 'https://api.twitter.com/2/users/{}/tweets?'.format(userid)

    def fetch_tweets_upto(self, tweetid=None):
        """
        makes https request to twitter api v2 endpoint /users/USER/tweets
        where USER is the userid inherited from tweetFetcher
        :param tweetid: tweet id to get texts up until
        :return: {
            'response': json response of the request
            'oldestid':oldest id in the response for use in recursive requests
        }
        """

        # if tweetid is given, we add the until parameter #
        if tweetid:
            url = self.url + 'until_id={}'.format(str(tweetid))
        # gets left bare, else #
        else:
            url = self.url

        response = requests.request("GET",
                                    url,
                                    headers=self.headers,
                                    data=self.payload)

        if str(response.status_code)=='200':

            return {
                'response': response.json()['data'],
                'oldestid': response.json()['meta']['oldest_id']
            }

        # adding this to handle api metering #
        elif str(response.status_code)=='429':
            print('request limit reached')
            time.sleep(15*60) # sleep for 15 minutes to rest the window
            response = requests.request("GET",
                                    url,
                                    headers=self.headers,
                                    data=self.payload)

            return {
                'response': response.json()['data'],
                'oldestid': response.json()['meta']['oldest_id']
            }

        else:

            print('Unsuccessful response. Code:{}'.format(str(response.status_code)))
            print('!----------------------------------!')
            print(response.text)
            raise Exception