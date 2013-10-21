#coding=utf-8
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='')

with con:
	cur = con.cursor()
	# add cook database and use it
	cur.execute("create database if not exists cook")
	cur.execute("use cook")

	# create table: UserTbl
	cur.execute("""create table if not exists UserTbl(
							id int auto_increment,
							account varchar(20), 
							password varchar(20), 
							name varchar(20), 
							gender varchar(20), 
							pemission int, 
							remark varchar(200), 
							primary key(id))""")
	# create table: MenuTypeTbl
	cur.execute("""create table if not exists MenuTypeTbl(
							id int auto_increment, 
							name varchar(20), 
							primary key(id))""")
	# create table: TableTbl
	cur.execute("""create table if not exists TableTbl(
							id int auto_increment, 
							num int, 
							flag int, 
							description varchar(100),
							primary key(id))""")
	# create table: MenuTbl -->forergn key(typeID)
	cur.execute("""create table if not exists MenuTbl(
							id int auto_increment, 
							typeID int,
							name varchar(50),
							price int, 
							pic varchar(100),
							remark varchar(200),
							primary key(id),
							foreign key(typeID) references MenuTypeTbl(id))""")
	# create table: OrderTbl -->forergn key(tableId)
	cur.execute("""create table if not exists OrderTbl(
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
	cur.execute("""create table if not exists OrderDetailTbl(
							id int, 
							orderId int,
							menuId int,
							info varchar(100),
							remark varchar(200),
							primary key(id),
							foreign key(orderId) references OrderTbl(id),
							foreign key(menuId) references MenuTbl(id))""")

	# init user
	#cur.executemany("insert into TableTbl(num, flag, description) values(%s, %s, %s)", values)
	# init table
	# init menu
