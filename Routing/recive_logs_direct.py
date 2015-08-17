import pika
import secret
import sys


connection=pika.BlockingConnection(pika.ConnectionParameters(host=secret.ipaddress))
channel=connection.channel()

channel.exchange_declare(exchange='logs_direct',type='direct')

result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
severities=sys.argv[1:]
if not severities:
    print >> sys.stderr, 'Usage: %s [info] [error] [warning]' %(sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='logs_direct',queue=queue_name,routing_key=severity)

print "[*] Waitting for logs.To exits press CTRL+C"

def callBack(ch,method,properties,body):
    print "[x] %r:%r"%(method.routing_key,body)

channel.basic_consume(callBack,queue=queue_name,no_ack=True)
channel.start_consuming()
