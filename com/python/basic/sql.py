# coding:utf-8
"""
    解析慢sql的excle
"""
import time
import string
import datetime
import hashlib
import xlrd
from jira import JIRA

"""
    生成jira的描述模板
"""
descriptiontemp = string.Template('''
 数据库：mysql:$dbip（物理IP）
 执行总次数:$selectallcount
 平均执行时间: $selectavgtime（秒）
 样例扫描行数：$simallcount（行）
 样例SQL:$simsql
''')
cloumndict = {
    "查询账号": "account",
    "pct95查询时长": "pct95time",
    "查询最大时长": "selectmaxtime",
    "查询最小时长": "selectmintime",
    "查询平均时长": "selectavgtime",
    "查询总时长": "selectalltime",
    "查询总次数": "selectallcount",
    "样例查询时长": "simselecttime",
    "样例锁时长": "simlocktime",
    "样例返回行数": "simreturncount",
    "样例检索行数": "simallcount",
    "样例查询发生时间": "simcreatetime",
    "数据库": "dnname",
    "样例数据库IP": "dbip",
    "SQL指纹": "presql",
    "样例SQL语句": "simsql",
    "CHECKSUM": "checksum"
}
# 要过滤sheet
sheetfileter = {"clover2": "clover2", "clover:": "clover"}

# 这里输入你登录jira的用户名与密码
jac = JIRA('http://jira.jd.com/', basic_auth=('user', 'passwd'))


def func_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("call %s, time: %f" % (func.__name__, end - start))
        return result

    return wrapper


@func_time
def parsexcle(exclepath):
    """
    解析excle
    :param exclepath: excle路径
    :return:
    """
    sqlsheets = xlrd.open_workbook(filename=exclepath)
    contacts = {}
    for sheet in sqlsheets.sheets():
        if sheet.name in sheetfileter:
            continue
        slist = []
        rownum = sheet.nrows
        colnum = sheet.ncols
        for i in range(1, rownum):
            sqldict = {}
            for j in range(colnum):
                title = sheet.cell_value(0, j)
                value = sheet.cell_value(i, j)
                sqldict[trancolumnname(title)] = value
            slist.append(sqldict)
        contacts[sheet.name] = slist
    return contacts


def sortslowsql(slowlist):
    """
    排序筛选出拉来TOP1,这个地方可以根据自己的需求进行修改
    :param slowlist:
    :return:
    """
    return sorted(slowlist, key=lambda e: (e.__getitem__('selectavgtime'), e.__getitem__('selectallcount')))[-1:]


def calcslowsql(showdict):
    """
    通过当前的列表计算出上报的慢sql
    :param showdict:
    :return:
    """
    showsqllist = []
    for k, v in showdict.items():
        showsqllist = showsqllist + sortslowsql(v)
    return showsqllist


def trancolumnname(scolumn):
    """
    转换列头到自定义的字段
    :param scolumn:
    :return:
    """
    return cloumndict[scolumn]


@func_time
def isexists_issues(reporter, sqlhash):
    """
    根据报告人与sql的hash判断当前的sql是否是提交过的
    :param reporter:报告人
    :param sqlhash:sql hash
    :return:
    """

    issues = jac.search_issues(
        'project=GYLCP and reporter=' + reporter + ' and summary ~ ' + sqlhash + '',
        maxResults=1)
    return len(issues)


@func_time
def createslowsql_issues(summary, description, projectname, modulename, assignee):
    """
    创建issues
    :param summary: 摘要
    :param description:描述
    :param projectname:项目名称
    :param modulename:Component
    :param assignee:经办人
    :return:
    """
    issue_dict = {
        "project": "GYLCP",
        "summary": summary,
        "issuetype": "慢SQL",
        "description": description,
        "customfield_11207": {"value": "性能"},
        "priority": {"name": "Minor"},
        "customfield_10025": {"value": "轻微"},
        "customfield_10107": projectname,
        "components": [{"name": modulename}],
        "customfield_10102": "技术发展部",
        "customfield_10103": "供应链产品研发部",
        "customfield_10104": "运营研发组",
        "customfield_10201": "系统维护",
        "assignee": {'name': assignee}
    }
    jac.create_issue(issue_dict)


if __name__ == '__main__':
    slowsqllist = calcslowsql(parsexcle("showsql.xlsx"))
    datestr = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
    # 注意这里需要修改
    reporter = "pengdawei"
    assignee = "zhangbin201"
    modulename = "运营研发组"
    projectname = "2020年618备战项目"
    for sql in slowsqllist:
        description = descriptiontemp.substitute(sql)
        sqlhash = hashlib.md5(sql["presql"].encode(encoding='UTF-8')).hexdigest()
        summary = "【上海亚一 %s 慢sql】【%s】【%s】" % (sql["dnname"], datestr, sqlhash)
        # 根据报告人与sql的MD5判断当前的sql是否提交过
        if not isexists_issues(reporter, sqlhash):
            createslowsql_issues(summary, description, projectname, modulename, assignee)