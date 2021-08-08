from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = "1072837803908784129-Pv2y0HZlUcJVyHmePC5KtLIVM0ZHz6"
access_token_secret =  "ImJh7Q2oMhHoHyWsln2BjMFWouYQCliPik9BkE1wymk6H"
consumer_key =  "WFRKqgnMYAIXB1NkOhvttsNMY"
consumer_secret =  "X4zj67WfzYt0paiqOpukFW7wb4wWeazttwW98GNmvEyLW9tvrA"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")

/home/ubuntu/Documents/ghezloo/kafka-spark-cassandra/test.py