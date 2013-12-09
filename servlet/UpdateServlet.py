#coding=utf-8
from dao.UpdateDaoImpl import *
from entity.Menu import *

def update_menu(arg):
    # 实例化dao
    dao = UpdateDaoImpl()
    # 获得菜谱列表
    menus = dao.getMenuList()

    # 拼XML格式数据
    head = "<?xml version='1.0' encoding='UTF-8'?>\n"
    # Menu根节点
    mstart = "<menulist>\n"

    for m in menus:
        mstart += "<menu>\n" + \
                "<id>" + str(m.getId()) + "</id>\n" + \
                "<typeId>" + str(m.getTypeId()) + "</typeId>\n" + \
                "<name>" + m.getName() + "</name>\n" + \
                "<pic>" + str(m.getPic()) + "</pic>\n" + \
                "<price>" + str(m.getPrice()) + "</price>\n" + \
                "<remark>" + str(m.getRemark()) + "</remark>\n" + \
                "</menu>\n"

    mend = "</menulist>\n"

    msg = head + mstart + mend
    return msg
