#coding=utf-8
import MySQLdb as mdb

class DBUtil:
	def __init__(self):
		self.host = 'localhost'
		self.username = 'root'
		self.password = 'wd'
		self.db = 'python'
	
	# close the db
	def closeConn(self, conn):
		conn.close()
	
	# open the db
	def openConnection(self):
		conn = mdb.connect(self.host, self.username, self.password)
		return conn
