#coding=utf-8
import zmq
import signal
from servlet.ChangeTableServlet import *
from servlet.CheckTableServlet import *
from servlet.LoginServlet import *
from servlet.OrderDetailServlet import *
from servlet.PayServlet import *
from servlet.PayMoneyServlet import *
from servlet.StartTableServlet import *
from servlet.UnionTableServlet import *
from servlet.UnionTableServlet2 import *
from servlet.UpdateServlet import *

serv = { 'cgt': change_table, 
		'ckt': check_table, 
		'lgn': login,
		'odt': order_detail, 
		'pay': pay, 
		'pmy': pay_money,
		'stb': start_table, 
		'utb': union_table, 
		'ut2': union_table2,
		'pdt': update }

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# register interrupter handler
def int_handler(signum, frame):
	print "User interrupt"
	exit()

signal.signal(signal.SIGINT, int_handler)

while True:
    #  Wait for next request from client
	msg = socket.recv()

    #  Do real work
	cmd = msg[:3]
	handler = serv[cmd]
	extra = msg[3:]
	reply = handler(extra)

    #  Send reply back to client
	socket.send(reply)
