import requests


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

    def fetch_tweets_since(self, tweetid=None):

        if tweetid:
            url = self.url + 'until_id='.format(str(tweetid))

        else:
            url = self.url

        response = requests.request("GET",
                                    url,
                                    headers=self.headers,
                                    data=self.payload)

        if str(response.status_code) != '200':
            print('Unsuccessful response. Code:{}'.format(str(response.code)))
            print('!----------------------------------!')
            print(response.text)
            raise EOFError
        else:

            return {
                'response': response.json()['data'],
                'oldestid': response.json()['meta']['oldest_id']
            }
