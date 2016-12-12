
import tweepy

consumer_key = 'oYUtZaF4sLujKloa3SWcKFLls'
consumer_key_secret = 'p1LIhz1FSHkVmntb0c4ynYhswUqpwCoB6sCHTZG4YERrU15N3d'
access_token = '2792724169-wxOaeaik5A0EvsDrqDFF2Uw6BxSmWMZzxJ9YbWe'
access_token_secret = 'SCUPBQ5g67YmqNtBaaC7dgTHNZsqOwYJuop5LqgSJ73GI'

class TweetListener(tweepy.StreamListener):
    def on_status(self,status):
        print('Tweet text: ' + status.text)
        return True

    def on_error(self,status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout..')
        return True

if __name__ == '__main__':
    listener = TweetListener()
    auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    stream = tweepy.Stream(auth,listener)
    stream.filter(follow=[],track=['#SFGiants','#Athletics'])



    

