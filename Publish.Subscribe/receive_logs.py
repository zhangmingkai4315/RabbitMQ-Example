import pika
import secret
import sys


connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)
print "[*] Waitting for logs.To exits press CTRL+C"

def callBack(ch,method,properties,body):
    print "[x] %r"%(body,)

channel.basic_consume(callBack,queue=queue_name,no_ack=True)
channel.start_consuming()
