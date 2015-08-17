import pika
import secret
import time
# #version-1 keep work not lost any task
# connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
# channel=connection.channel()
# channel.queue_declare(queue='hello');
# print "[*] Waitting for messages.To exit press CTRL+C"
#
# def callBack(ch,method,properties,body):
#     print '[x] received %r' % (body,)
#     time.sleep(body.count('.'));
#     print '[x] Done'
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#
# channel.basic_consume(callBack,queue='hello')
# channel.start_consuming()


#version-2 keep rabbit not lost any task and queue
connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()
channel.queue_declare(queue='task_durable',durable=True);
print "[*] Waitting for messages.To exit press CTRL+C"

def callBack(ch,method,properties,body):
    print '[x] received %r' % (body,)
    time.sleep(body.count('.'));
    print '[x] Done'
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callBack,queue='hello')
channel.start_consuming()
