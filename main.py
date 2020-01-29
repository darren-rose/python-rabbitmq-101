import os
import pika

host = os.getenv('RABBITMQ_HOST', 'localhost')
port = os.getenv('RABBITMQ_PORT', '5672')
user = os.getenv('RABBITMQ_DEFAULT_USER', 'admin')
password = os.getenv('RABBITMQ_DEFAULT_PASS', 'password')

credentials = pika.PlainCredentials(user, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=int(port), credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='my-fancy-queue')

for i in range (0, 500):
    channel.basic_publish(exchange='', routing_key='my-fancy-queue', body=f'Message {i}')

print("Done")

