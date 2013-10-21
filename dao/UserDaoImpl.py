#coding=utf-8
from DBUtil import *
from entity.User import *

class UserDaoImpl:
	
	def __init__(self):
		self.conn = dbutil().openconnection()

	def login(self, account, password):
		# 查询SQL语句
		sql = " select id,account,password,name,permission,remark "+\
						" from UserTbl "+\
						" where account=%s and password=%s "
		with self.conn:
			cur = self.conn.cursor()

			values = [ account, password ]
			# 执行查询
			cur.execute(sql, values)  

			row = cur.fetchone()

			Id = row(0)
			name = row(3)
			permission = row(4)
			remark = row(5)
			# 封装用户信息
			u = User()
			
			u.setId(Id)
			u.setAccount(account)
			u.setPassword(password)
			u.setName(name)
			u.setPermission(permission)
			u.setRemark(remark)
			
			return u
		return None
