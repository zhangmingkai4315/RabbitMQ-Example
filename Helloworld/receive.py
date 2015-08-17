import pika
import secret
connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()
channel.queue_declare(queue='hello');
print "[*] Waitting for messages.To exit press CTRL+C"

def callBack(ch,method,properties,body):
    print '[x] received %r' % (body,)
channel.basic_consume(callBack,queue='hello',no_ack=True)
channel.start_consuming()
