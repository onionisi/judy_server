#coding=utf-8
import zmq
import time
import signal
import message_pb2

context = zmq.Context()

# Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5555")

# Do requests, waiting each time for a response

# starttable
def start_table_test():
	print "stb test"

	stb = message_pb2.StartTable()
	stb.orderTime = str(time.time())
	stb.userId = "2"
	stb.tableId = "7"
	stb.personNum = "3"
	stb_str = stb.SerializeToString()
	request = "stb" + stb_str
	return request

req = start_table_test()
# send the request
socket.send(req)
# show the reply.
print socket.recv()
