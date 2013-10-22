#coding=utf-8
import message_pb2
from dao.UnionTableDaoImpl import *

def union_table2(obj):
		
	msg = message_pb2.UnionTable2()
	msg.ParseFromString(obj)

	tableId1 = msg.tableId1
	tableId2 = msg.tableId2
	
	dao = UnionTableDaoImpl()
	
	dao.updateStatus(tableId1, tableId2)

	return "union success"
