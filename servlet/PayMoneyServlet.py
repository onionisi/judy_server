#coding=utf-8
from dao.OrderDaoImpl import *
from dao.PayDaoImpl import *

def pay_money(msg):

	# 实例化PayDao
	dao = PayDaoImpl()
	# 获得订单编号
	Id = int(msg)
	# 结算
	dao.pay(Id)

	# 实例化OrderDao
	dao2 = OrderDaoImpl()
	# 将餐桌状态更新为空位
	dao2.updateTableStatus2(Id)

	# 向客户端发送信息
	return "already paid!"
