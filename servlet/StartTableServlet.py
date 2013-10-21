#coding=utf-8
import message_pb2
from entity.Order import *
from dao.OrderDaoImpl import *

def start_table(obj):

	msg = message_pb2.StartTable()
	msg.ParseFromString(obj)

	# 点餐时间
	orderTime = msg.orderTime
	# 操作员编号
	userId = msg.userId
	# 桌号
	tableId = msg.tableId
	# 人数
	personNum = msg.personNum

	# 获得DAO接口
	dao = OrderDaoImpl()
	# 实例化订单类
	o = Order()
	# 设置订单属性
	o.setOrderTime(orderTime)
	o.setPersonNum(personNum)
	o.setUserId(userId)
	o.setTableId(tableId)
	# 返回订单ID
	Id = dao.saveOrder(o)
	
	# 更新餐桌状态为 有人
	dao.updateTableStatus(tableId)

	# 返回ID
	return Id
