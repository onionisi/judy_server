#coding=utf-8
import MySQLdb as mdb
from DBUtil import *

class ChangeTableDaoImpl:
	def __init__(self):
		self.util = DBUtil()

	def changeTable(self, orderId, tableId):
		
		sql = " update TableTbl set flag = 0 where id = " +\
		  " (select tableId from OrderTbl  as ot where ot.id = %s)"
		sql2 = " update OrderTbl set tableId = %s where id = %s "
		sql3 = " update TableTbl set flag = 1 where id = %s"
		
		try:
			conn = self.util.openConnection()

			conn.autocommit(False)
			cur = conn.cursor()

			# update table status
			cur.execute(sql, orderId)  

			# update order
			values = [ tableId, orderId ]
			cur.execute(sql2, values)  

			# update table status again
			cur.execute(sql3, tableId)  
			
			#事务的特性1、原子性的手动提交
			conn.commit()

			cursor.close()
			conn.close()

		except mdb.Error, e:
			#如果出现了错误，那么可以回滚，就是上面的三条语句要么执行，要么都不执行
			conn.rollback()
			print "Error %d: %s" % (e.args[0],e.args[1])
