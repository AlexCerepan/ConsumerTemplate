consumer_conf = {
    'bootstrap.servers': '172.28.1.7:9092',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'client',
    'sasl.password': 'your_password',
    'group.id': 'your_consumer_group',
    'auto.offset.reset': 'smallest',
}
consumer_subscriptions = ["topic1", "topic2", "topic3"]
