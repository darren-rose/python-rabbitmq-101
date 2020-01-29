import os
import pika
from time import sleep

host = os.getenv('RABBITMQ_HOST', 'localhost')
port = os.getenv('RABBITMQ_PORT', '5672')
user = os.getenv('RABBITMQ_DEFAULT_USER', 'admin')
password = os.getenv('RABBITMQ_DEFAULT_PASS', 'password')

print('host port', host, port)
sleep(15)

credentials = pika.PlainCredentials(user, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=int(port), credentials=credentials))

channel = connection.channel()

queue = 'publications'

channel.queue_declare(queue=queue)

message = """
    {
        "name" : "john",
        "age" : 47
    }
"""

for i in range (0, 5000):
    channel.basic_publish(exchange='', routing_key=queue, body=message)

connection.close()

print("Done")

