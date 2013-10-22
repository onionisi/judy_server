#coding=utf-8
import message_pb2 
from dao.CheckTableDaoImpl import *
from entity.CheckTable import *

def check_table(arg):
	obj = message_pb2.CheckTable()

	# 实例化CheckTableDao
	dao = CheckTableDaoImpl()
	# 获得餐桌信息列表
	msg = dao.getTableList()
	# 转换为字符串
	for each in msg:
		sub = obj.subchecktable.add()
		sub.num = each.getNum()
		sub.flag = each.getFlag()
	
	# 返回给客户端
	return obj.SerializePartialToString()
