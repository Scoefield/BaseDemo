from MysqlHelper import MysqlHelper

mysqlhelp = MysqlHelper('localhost', 'root', 'root', 3306, 'data', 'utf8')

table = 'mobile'
name = 'JACK'
# sql = "select * from mobile where name='JACK';"
sql = "select * from {} where name='{}';".format(table, name)
res = mysqlhelp.find(sql)
print(res)
