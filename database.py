#coding=utf-8
import MySQLdb
import sys

class Cook:
    def __init__(self, db_name='cook'):
        self.con = MySQLdb.connect(host='localhost', user='root', passwd='')
        self.cur = self.con.cursor()

        # add database and use it
        self.cur.execute("show databases")
        dbs = self.cur.fetchall()

        db_cur = db_name,
        if not db_cur in dbs:
            db_create = "create database if not exists " + db_name
            self.cur.execute(db_create)

        db_use = "use " + db_name
        self.cur.execute(db_use)

    def table_create(self):
        with self.con:
            self.cur.execute("show tables")
            tables = self.cur.fetchall()

            # create table: UserTbl
            user = 'UserTbl',
            if not user in tables: 
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
            table = 'TableTbl',
            if not table in tables: 
     	       self.cur.execute("""create table if not exists TableTbl(
                                                        id int auto_increment, 
                                                        num int, 
                                                        flag int, 
                                                        description varchar(100),
                                                        primary key(id))""")
            # create table: MenuTbl -->foreign key(typeID)
            # MenuTbl V2: delete foreign key typeID turn to char
            menu = 'MenuTbl',
            if not menu in tables: 
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
            order = 'OrderTbl',
            if not order in tables: 
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
            orderdetail = 'OrderDetailTbl',
            if not orderdetail in tables: 
                self.cur.execute("""create table if not exists OrderDetailTbl(
                                                        id int auto_increment, 
                                                        orderId int,
                                                        menuId int,
                                                        num int,
                                                        remark varchar(200),
                                                        primary key(id),
                                                        foreign key(orderId) references OrderTbl(id),
                                                        foreign key(menuId) references MenuTbl(id))""")

                    # create procedures
    def procedure_create(self, files):
        with self.con:
            self.cur.execute("select `name` from mysql.proc where db = 'cook' and `type` = 'PROCEDURE'")
            procs = self.cur.fetchall()

            # create proc: new_proc
            new = 'new_proc',
            if not new in procs: 
                proc_line = open(files).read()
                self.cur.execute(proc_line)

    # init table
    def table_init(self, num):
        with self.con:
        	# abandon old one
            self.cur.execute("""SET FOREIGN_KEY_CHECKS=0;
                                truncate TableTbl;
                                SET FOREIGN_KEY_CHECKS=1;""")
            # for error:"Commands out of sync; you can't run this command now"
            self.cur.close()
            cur = self.con.cursor()

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
            self.cur.execute("""SET FOREIGN_KEY_CHECKS=0;
                                truncate MenuTbl;
                                SET FOREIGN_KEY_CHECKS=1;""")
            # for error:"Commands out of sync; you can't run this command now"
            self.cur.close()
            cur = self.con.cursor()

            lines = []
            for line in open(files).readlines():
                line_list = line.split()
                line_list[1].decode('utf-8').encode(sys.getfilesystemencoding())
                lines.append(line_list)

            cur.executemany("insert into MenuTbl(type, name, price) values(%s, %s, %s)", lines)

    # init user(not use this version)
    def user_init(self):
        with self.con:
            #self.cur.execute("insert into UserTbl(account, password, name,
            #		gender, permission, remark) values(%s, %s, %s, %s, %s, %s",
            #		values)
            values = ["admin", "admin", "onionisi"]
            self.cur.execute("insert into UserTbl(account, password, name) values(%s, %s, %s)", values)
            pass

    # init menu_type (should abandon!!!)
    def menu_type_init(self, files):
        pass
