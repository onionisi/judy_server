#coding=utf-8
from dao.UpdateDaoImpl import *
from entity.Menu import *

def update(arg):
	# 实例化dao
	dao = UpdateDaoImpl()
	# 获得菜谱列表
	menus = dao.getMenuList()
	
	# 拼XML格式数据
	head = "<?xml version='1.0' encoding='UTF-8'?>\n"
	# 根节点
	start = "<menulist>\n"

	for m in menus:
		start += "<menu>\n" + \
			"<id>" + str(m.getId()) + "</id>\n" + \
			"<typeId>" + str(m.getTypeId()) + "</typeId>\n" + \
			"<name>" + m.getName() + "</name>\n" + \
			"<pic>" + m.getPic() + "</pic>\n" + \
			"<price>" + str(m.getPrice()) + "</price>\n" + \
			"<remark>" + m.getRemark() + "</remark>\n" + \
			"</menu>\n"

	end = "</menulist>\n"

	msg = head + start + end
	return msg
