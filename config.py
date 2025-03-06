consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'client',
    'sasl.password': 'client-secret',
    'group.id': 'foo',
    'auto.offset.reset': 'smallest',
}
consumer_subscriptions = ["topics"]
