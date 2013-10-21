#coding=utf-8
import message_pb2
from dao.UserDaoImpl import *
from entity.User import *

def login(obj):

	msg = message_pb2.Login()
	msg.ParseFromString(obj)

	username = msg.account
	password = msg.password
	
	u = dao.login(username, password)

	if (u != None):
		# 响应客户端内容，登录成功
		msg.Id = u.getId()
		msg.name = u.getName()
		msg.SerializePartialToString()
		return msg
	else:
		# 响应客户端内容，登录失败
		return "login failed!"
