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

# orderdetail
def order_detail_test():
	print "odt test"

	odt = message_pb2.OrderDetail()
	odt.menuId = "2"
	odt.orderId = "9"
	odt.num = "2"
	odt.remark = "acid"

	odt_str = odt.SerializeToString()
	request = "odt" + odt_str
	return request

# changetable
def change_table_test():
	print "cgt test"

	cgt = message_pb2.ChangeTable()
	cgt.orderId = 10
	cgt.tableId = 1

	cgt_str = cgt.SerializeToString()
	request = "cgt" + cgt_str
	return request

# checktable
def check_table_test():
	print "ckt test"

	cgt = message_pb2.CheckTable()

	socket.send("ckt")
	cgt_str = socket.recv()
	cgt.ParseFromString(cgt_str)

	for sub in cgt.subchecktable:
		print "table number %d, flag %d" % (sub.num, sub.flag)

	return 0

#req = start_table_test()
#req = order_detail_test()
#req = change_table_test()
check_table_test()

## send the request
#socket.send(req)
## show the reply.
#print socket.recv()
