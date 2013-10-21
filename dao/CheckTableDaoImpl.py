#coding=utf-8
from DBUtil import *
from entity.CheckTable import *

class CheckTableDaoImpl:

	def __init__(self):
		self.conn = DBUtil().openConnection()

	# 获得餐桌列表
	def getTableList(self):
		# 查询SQL语句
		sql =" select num,flag from TableTbl"
		with self.conn:
			cur = self.conn.cursor()

			cur.execute(sql)  

			# 获得预定义语句
			rows = cur.fetchall()
			result = []
			for row in rows:
				num = row[0]
				flag = row[1]

				ct = CheckTable()
				ct.setFlag(flag)
				ct.setNum(num)

				result.append(ct)
			
			return result
		return None
