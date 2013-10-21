#coding=utf-8
import message_pb2
from dao.ChangeTableDaoImpl import *

def change_table(obj):

	msg = message_pb2.ChangeTable()
	msg.ParseFromString(obj)

	# 获得请求参数
	orderId = msg.orderId
	tableId = msg.tableId

	# 实例化ChangeTableDao
	dao = ChangeTableDaoImpl()
	# 调用转台方法
	dao.changeTable(orderId, tableId)
	# 返回客户端信息
	return ("change success!")
