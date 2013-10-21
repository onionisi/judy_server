#coding=utf-8
import message_pb2
from dao.UserDaoImpl import *
from entity.User import *

def login(obj):

	msg = message_pb2.Login()
	msg.ParseFromString(obj)

	username = msg.account
	password = msg.password
	
	dao = UserDaoImpl()
	u = dao.login(username, password)

	if (u != None):
		# 响应客户端内容，登录成功
		# TODO: need to fix login proto

		ret = message_pb2.Login()
		ret.account = u.getAccount()
		ret.password = u.getPassword()

		ret.Id = str(u.getId())
		ret.name = u.getName()

		print u.getId(), u.getName()
		ret.SerializeToString()
		return ret
	else:
		# 响应客户端内容，登录失败
		return "login failed!"
