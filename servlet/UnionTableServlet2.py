#coding=utf-8
from dao.UnionTableDaoImpl import *

def union_table2(arg):
		
	tableId1 = request.getParameter("tableId1")
	tableId2 = request.getParameter("tableId2")
	
	dao = UnionTableDaoImpl()
	
	dao.updateStatus(tableId1, tableId2)
