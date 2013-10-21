#coding=utf-8
import message_pb2
from dao.OrderDaoImpl import *
from entity.OrderDetail import *

def order_detail(obj):

	msg = message_pb2.OrderDetail()
	msg.ParseFromString(obj)

	orderId = msg.orderId
	menuId = msg.menuId
	num = msg.num
	remark = msg.remark
	
	dao = OrderDaoImpl()
	
	od = OrderDetail()
	
	od.setMenuId(menuId)
	od.setOrderId(orderId)
	od.setNum(num)
	od.setRemark(remark)
	
	dao.saveOrderDetail(od)
	
	return remark
