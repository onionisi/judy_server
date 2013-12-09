#coding=utf-8
from dao.UpdateDaoImpl import *
from entity.Table import *

def update_table(arg):
    # 实例化dao
    dao = UpdateDaoImpl()
    # 获得桌号列表
    tables = dao.getTableList()

    # 拼XML格式数据
    head = "<?xml version='1.0' encoding='UTF-8'?>\n"
    # Table根节点
    tstart = "<tablelist>\n"

    for t in tables:
        tstart += "<table>\n" + \
                "<id>" + str(t.getId()) + "</id>\n" + \
                "<num>" + str(t.getNum()) + "</num>\n" + \
                "<description>" + t.getDesc() + "</description>\n" + \
                "</table>\n"

    tend = "</tablelist>\n"

    msg = head + tstart + tend
    return msg
