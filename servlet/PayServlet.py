#coding=utf-8
import message_pb2
from dao.PayDaoImpl import *
from entity.QueryOrder import *
from entity.QueryOrderDetail import *

def pay(Id):
		# 实例化DAO
		dao = PayDaoImpl()
		# 查询订单信息
		qo = dao.getOrderById(Id)
		# 查询订单详细列表
		orders = dao.getOrderDetailList(Id)
		
		# 拼HTML页面展示
		head = "<!DOCTYPE HTML PUBLIC \"-#W3C#DTD HTML 4.01 Transitional#EN\">\n"
		body = "<HTML>\n" + "  <HEAD></HEAD>\n" + "  <BODY>\n<table>"
		line = "<tr><th>订单编号</th>" +\
				"<th>下单时间</th>" +\
				"<th>服务员</th>" +\
				"<th>人数</th>" +\
				"<th>桌号</th></tr>" +\
				"<tr><td>" + Id + "</td>" +\
				"<td>" + qo.getOrderTime() + "</td>" +\
				"<td>" + qo.getName() + "</td>" +\
				"<td>" + qo.getPersonNum() + "</td>" +\
				"<td>" + qo.getTableId() + "</td></tr>"
			
		content ="<tr><th>菜名</th>" +\
				"<th>价格</th>" +\
				"<th>数量</th>" +\
				"<th>总计</th>" +\
				"<th>备注</th></tr>"
			
		for qod in orders:
			name = qod.getName()
			price = qod.getPrice()
			num = qod.getNum()
			total = qod.getTotal()
			remark = qod.getRemark()
			
			content += "<tr><td>" + name + "</td>" +\
				"<td>" + price + "</td>" +\
				"<td>" + num + "</td>" +\
				"<td>" + total + "</td>" +\
				"<td>" + remark + "</td></tr>"
			
		end = "</table>  </BODY>\n</HTML>\n"

		msg = head + body + line + content 

		return msg
