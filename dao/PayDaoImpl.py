#coding=utf-8
from DBUtil import *
from entity.QueryOrder import *
from entity.QueryOrderDetail import *
# coding: utf-8

class PayDaoImpl:
	def __init__(self):
		self.conn = DBUtil().openConnection()
	
	# 根据订单编号，查询订单信息
	def getOrderById(self, Id):

		# 获得连接
		with self.conn:
			# 查询SQL语句
			sql =""" 	select ot.`orderTime`,
					 	ut.`name`,
					 	ot.`personNum`,
					 	ot.`tableId` 
					 	from OrderTbl as ot
					 	left join UserTbl as ut on ot.`userID` = ut.id
					 	where ot.`id`=%s """
			# 执行查询
			result = cur.execute(sql, Id)  

			# 判断订单是否存在
			if (result == 1):
				# 获得订单信息
				row = cur.fetchone()
				orderTime = row(0)
				userName  = row(1)
				personNum = row(2)
				tableId   = row(3)

				qo = QueryOrder()
				qo.setName(userName)
				qo.setOrderTime(orderTime)
				qo.setPersonNum(personNum)
				qo.setTableId(tableId)

				return qo
		
		return null
	
	# 根据订单编号，查询订单详细列表
	def getOrderDetailList(self, Id):

		# 获得连接
		with self.conn:
			# 查询SQL语句
		 	sql ="""select mt.`name`,
					mt.`price`, 
					odt.`num`, 
					mt.price*odt.num as total, 
					odt.`remark` 
					from OrderdetailTbl as odt 
					left join MenuTbl as mt on odt.`menuId` = mt.id 
					where odt.`orderId`= %s
		
					union 
					
					select          '',
					'',
					'',
					sum(mt.price*odt.num) as total1,
					'' 
					from OrderdetailTbl as odt
					left join MenuTbl as mt on odt.`menuId` = mt.id
					where odt.`orderId`= %s """
		
			# 设置查询参数
			values = [ Id, Id ]
			# 执行查询
			rs = cur.execute(sql, value)  
			# 判断订单详细
			result = []
			rows = cur.fetchall()

			for row in rows:
				# 获得订单详细信息
				name = row(0)
				price = row(1)
				num = row(2)
				total = row(3)
				remark = row(4)
				
				qod = QueryOrderDetail()
				
				qod.setName(name)
				qod.setNum(num)
				qod.setPrice(price)
				qod.setTotal(total)
				qod.setRemark(remark)
				
				result.append(qod)
			
			return result
		
		return None
	
	
	# 结算
	def pay(self, Id):

		# 获得连接
		with self.conn:
			# 查询SQL语句
		 	sql =" update OrderTbl set isPay=1 where id = %s"
			# 执行更新
			cur.execute(sql, Id)  
