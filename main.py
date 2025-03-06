from consumer import DefaultConsumer
from config import consumer_conf, consumer_subscriptions

class MyConsumer(DefaultConsumer):
    def msg_process(self, msg):
        print(msg.value().decode('utf-8'))

if __name__ == "__main__":
    consumer = MyConsumer(consumer_conf, consumer_subscriptions)
    consumer.start_consume()

