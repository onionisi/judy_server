#coding=utf-8
from DBUtil import *
from entity.Order import *
from entity.OrderDetail import *
# coding: utf-8

class OrderDaoImpl:
	def __init__(self):
		self.conn = DBUtil().openConnection()

	# save table info, return order_id
	def saveOrder(self, order):

		with self.conn:
			cur = self.conn.cursor()

			sql = " insert into OrderTbl(orderTime,userId,tableId,personNum)values(%s,%s,%s,%s) "
			# set arg
			value = [ order.getOrderTime(),
					order.getUserId(),
					order.getTableId(),
					order.getPersonNum() ]
			# execute
			cur.execute(sql, value);  

			# return order_id
			sql2 = " select max(id) as id from OrderTbl "
			cur.execute(sql2) 

			row = cur.fetchone()
			return row[0]
	
	#save order list
	def saveOrderDetail(self, od):

		with self.conn:
			cur = self.conn.cursor()
			sql = " insert into OrderdetailTbl(orderId,menuId,num,remark)values(%s,%s,%s,%s) "

			value = [ od.getOrderId(),
					od.getMenuId(),
					od.getNum(),
					od.getRemark() ]
			# execute
			cur.execute(sql, value);  
	
	# using: update table status
	def updateTableStatus(self, table_id):

		with self.conn:
			cur = self.conn.cursor()

			sql = " update TableTbl set flag=1 where id = %s "
			cur.execute(sql, table_id)  
		
	
	# empty: update table status
	def updateTableStatus2(self, order_id): 

		 with self.conn:
			cur = self.conn.cursor()

			sql = " update TableTbl set flag = 0 where id = " +\
							" ( select tableId from OrderTbl where id = %s) "
			cur.execute(sql, order_id)  
