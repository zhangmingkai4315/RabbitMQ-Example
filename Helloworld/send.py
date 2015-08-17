import pika
import secret
connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()
channel.queue_declare(queue='hello');
channel.basic_publish(exchange='',routing_key='hello',body='Hello World')
print "[x] Send 'Hello world!'"

connection.close()
