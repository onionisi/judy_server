#coding=utf-8
import MySQLdb

class db_init:
	def __init__(self, db_name='cook'):
		self.con = MySQLdb.connect(host='localhost', user='root', passwd='')
		self.cur = self.con.cursor()

		# add database and use it
		db_create = "create database if not exists " + db_name
		self.cur.execute(db_create)
		db_use = "use " + db_name
		self.cur.execute(db_use)

	def table_create(self):
		with self.con:
			# create table: UserTbl
			self.cur.execute("""create table if not exists UserTbl(
									id int auto_increment,
									account varchar(20), 
									password varchar(20), 
									name varchar(20), 
									gender varchar(20), 
									permission int, 
									remark varchar(200), 
									primary key(id))""")
			# create table: MenuTypeTbl
			#cur.execute("""create table if not exists MenuTypeTbl(
			#						id int auto_increment, 
			#						name varchar(20), 
			#						primary key(id))""")
			# create table: TableTbl
			self.cur.execute("""create table if not exists TableTbl(
									id int auto_increment, 
									num int, 
									flag int, 
									description varchar(100),
									primary key(id))""")
			# create table: MenuTbl -->foreign key(typeID)
			# MenuTbl V2: delete foreign key typeID turn to char
			self.cur.execute("""create table if not exists MenuTbl(
									id int auto_increment, 
									type varchar(20),
									name varchar(50),
									price int, 
									pic varchar(100),
									remark varchar(200),
									primary key(id))""")
									#foreign key(typeID) references MenuTypeTbl(id))""")
			# create table: OrderTbl -->forergn key(tableId)
			self.cur.execute("""create table if not exists OrderTbl(
									id int auto_increment, 
									orderTime varchar(30), 
									userId int,
									tableId int, 
									personNum int,
									isPay int,
									remark varchar(200),
									primary key(id),
									foreign key(tableId) references TableTbl(id))""")
			# create table: OrderDetailTbl -->forergn key(orderId, menuId)
			self.cur.execute("""create table if not exists OrderDetailTbl(
									id int auto_increment, 
									orderId int,
									menuId int,
									num int,
									remark varchar(200),
									primary key(id),
									foreign key(orderId) references OrderTbl(id),
									foreign key(menuId) references MenuTbl(id))""")
		
	# init table
	def table_init(self, num):
		with self.con:
			# abandon old one
			self.cur.execute("truncate table TableTbl")

			values = []
			for i in range(1, num+1):
				values.append((i, 0, '1: occupied, 0: empty'))  

			self.cur.executemany("insert into TableTbl(num, flag, description) values(%s, %s, %s)", values)
		
	# add table
	def table_add(self, num):
		with self.con:
			self.cur.execute("select max(num) as id from TableTbl")
			row = self.cur.fetchone()

			values = []
			for i in range(row[0]+1, row[0]+num+1):
				values.append((i, 0, '1: occupied, 0: empty'))  

			self.cur.executemany("insert into TableTbl(num, flag, description) values(%s, %s, %s)", values)

	# init menu
	def menu_init(self, files):
		with self.con:
			# abandon old one
			self.cur.execute("truncate table MenuTbl")
	
			for line in open(files).readlines():
				line_list = line.split()
				line_list[1].decode('utf-8').encode(sys.getfilesystemencoding())
				line_list.append('')
				self.cur.execute("insert into table MenuTbl(type, name, price, remark) values(%s, %s, %s, %s)", line_list)

	# init user
	def user_init(self):
		with self.con:
			#self.cur.execute("insert into table UserTbl(account, password, name,
			#		gender, permission, remark) values(%s, %s, %s, %s, %s, %s",
			#		values)
			values = ["admin", "admin", "onionisi"]
			self.cur.execute("insert into table UserTbl(account, password, name) values(%s, %s, %s)", values)
			pass

	# init menu_type (should abandon!!!)
	def menu_type_init(self, files):
		pass


db = db_init()
db.table_create()
