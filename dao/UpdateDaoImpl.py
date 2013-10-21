#coding=utf-8
from DBUtil import *
from entity.Menu import *

class UpdateDaoImpl:

	def __init__(self):
		self.conn = dbutil().openconnection()

	# 获得菜单列表
	def getMenuList(self):
		# 查询SQL语句
		sql =" select id,typeId,price,name,pic,remark from MenuTbl "

		with self.conn:
			cur = self.conn.cursor()

			# 执行查询
			cur.execute(sql)  
			# 判断订单详细
			rows = cur.fetchall()
			result = []
			for row in rows:
				# 获得菜单信息
				Id     = row(0)
				typeId = row(1)
				price  = row(2)
				name   = row(3)
				pic    = row(4)
				remark = row(5)
				
				m = Menu()
				m.setId(Id)
				m.setName(name)
				m.setPic(pic)
				m.setPrice(price)
				m.setRemark(remark)
				m.setTypeId(typeId)
				
				result.append(m)
			
			return result
		return None
	
	# 获得餐桌列表
	def getTableList(self):

		return None
