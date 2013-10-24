#coding=utf-8
from DBUtil import *
from entity.UnionTable import *

class UnionTableDaoImpl:
	
	def __init__(self):
		self.conn = DBUtil().openConnection()

	def getTableList(self):
		# 查询SQL语句
		sql =" select id,num from TableTbl where flag = 1 "

		with self.conn:
			cur = self.conn.cursor()
			cur.execute(sql)  

			# 判断订单详细
			result = []
			rows = cur.fetchall()
			for row in rows:
				# 获得菜单信息
				Id = row[0]
				num = row[1]
				
				ut = UnionTable()
				ut.setId(Id)
				ut.setNum(num)
				
				result.append(ut)
			
			return result
		return None
	
	def updateStatus(self, tableId1, tableId2):
		with self.conn:
			cur = self.conn.cursor()

			prepare = "new_proc"
			values = [ tableId1, tableId2 ]

			cur.callproc(prepare, values)
