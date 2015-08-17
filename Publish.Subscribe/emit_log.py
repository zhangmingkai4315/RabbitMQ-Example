import pika
import secret
import sys


connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')
messages=' '.join(sys.argv[1:]) or 'Info: Hello world'

channel.basic_publish(exchange='logs',routing_key='',body=messages)
print "[x] Sent %r"%(messages,)
connection.close()
