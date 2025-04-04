# Kafka Consumer Template

A Python-based Kafka consumer template that provides a simple way to consume messages from Kafka topics with SASL authentication.

## Project Structure

- `config.py`: Configuration for the consumer
- `consumer.py`: Abstract base consumer class for easy extension
- `main.py`: Main script for running the consumer

## Features

- SASL PLAINTEXT authentication
- Configurable consumer group and topics
- Abstract base consumer class for easy extension
- Graceful error handling and shutdown
- Customizable message processing

## Prerequisites

- Python 3.x
- confluent-kafka Python package

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install confluent-kafka
```

## Configuration

The configuration is stored in `config.py`. You can modify the following settings:

```python
consumer_conf = {
    'bootstrap.servers': '172.28.1.7:9092',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'client',
    'sasl.password': 'your_password',
    'group.id': 'your_consumer_group',
    'auto.offset.reset': 'smallest',
}
```

## Usage

### Basic Usage

The template provides a base `DefaultConsumer` class that can be extended to implement custom message processing logic:

```python
from consumer import DefaultConsumer
from config import consumer_conf, consumer_subscriptions

class MyConsumer(DefaultConsumer):
    def msg_process(self, msg):
        # Implement your message processing logic here
        print(msg.value().decode('utf-8'))

if __name__ == "__main__":
    consumer = MyConsumer(consumer_conf, consumer_subscriptions)
    consumer.start_consume()
```

### Extending the Consumer

To create your own consumer, extend the `DefaultConsumer` class and implement the `msg_process` method:

1. Create a new class that inherits from `DefaultConsumer`
2. Implement the `msg_process` method to handle incoming messages
3. Initialize your consumer with the desired configuration and subscriptions