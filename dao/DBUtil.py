#coding=utf-8
import MySQLdb as mdb

class DBUtil:
	def __init__(self):
		self.host = 'localhost'
		self.username = 'root'
		self.password = ''
		self.db = 'cook'
	
	# close the db
	def closeConn(self, conn):
		conn.close()
	
	# open the db
	def openConnection(self):
		conn = mdb.connect(self.host, self.username, self.password, self.db)
		return conn
