import pika
import secret
import sys
import time
# connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
# channel=connection.channel()
# channel.queue_declare(queue='hello');
# message='Message..'
# for i in range(1,100):
#     new_message="{ID: %d,Body:%r}"%(i,message)
#     channel.basic_publish(exchange='',routing_key='hello',body=new_message)
#     time.sleep(1);
#     print "[x] Send %r"%(new_message,)
#
# connection.close()



connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()
channel.queue_declare(queue='task_durable',durable=True);
message='Message.'
for i in range(1,100):
    if i%2==0:
        new_message="{ID: %d,Body:%r}"%(i,message)
    else:
        new_message="{ID: %d,Body:..%r}"%(i,message)
    channel.basic_publish(exchange='',routing_key='hello',body=new_message,properties=pika.BasicProperties(delivery_mode=2))
    time.sleep(1);
    print "[x] Send %r"%(new_message,)

connection.close()
