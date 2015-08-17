import pika
import secret
import sys


connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()

channel.exchange_declare(exchange='logs_topic',type='topic')

severity='info' if len(sys.argv)<2 else  sys.argv[1]
messages='Hello world'



channel.basic_publish(exchange='logs_topic',routing_key=severity,body=messages)
print "[x] Sent %r:%r"%(severity,messages)
connection.close()
