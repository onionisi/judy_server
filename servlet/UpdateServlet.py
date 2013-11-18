#coding=utf-8
from dao.UpdateDaoImpl import *
from entity.Menu import *
from entity.Table import *

def update(arg):
    # 实例化dao
    dao = UpdateDaoImpl()
    # 获得菜谱列表
    menus = dao.getMenuList()
    tables = dao.getTableList()

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
    # Table根节点
    tstart = "<tablelist>\n"

    for t in tables:
        tstart += "<table>\n" + \
                "<id>" + str(t.getId()) + "</id>\n" + \
                "<num>" + str(t.getNum()) + "</num>\n" + \
                "<description>" + t.getDesc() + "</description>\n" + \
                "</table>\n"

    tend = "</tablelist>\n"

    msg = head + mstart + mend + tstart + tend
    return msg
