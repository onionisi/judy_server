#coding=utf-8
import message_pb2
from dao.UnionTableDaoImpl import *
from entity.Menu import *
from entity.UnionTable import *

def union_table():
	dao = UnionTableDaoImpl()
	
	tables = dao.getTableList()
	
	head = "<?xml version='1.0' encoding='UTF-8'?>\n"
	start = "<tablelist>\n"

	for ut in tables:
		start += "<table>\n<id>" + ut.getId() + \
			"</id>\n<num>" + ut.getNum() + \
			"</num>\n</table>\n"
		
	end = "</tablelist>\n"

	msg = head + start + end

	return msg
