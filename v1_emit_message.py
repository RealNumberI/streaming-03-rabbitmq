"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Tanya Fagaly
    Date: January 27, 2023

"""

# add imports at the beginning of the file
import pika

# create message
message = "Hello!  I am a variable."
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(" [x] Sent 'Hello World! It is here and now!'")
# close the connection to the server
conn.close()
