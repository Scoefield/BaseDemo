# from dbfread import dbf
from dbfread1 import DBF

#数据表文件名
table = DBF('2018dbf.dbf')

#遍历数据表中（没加删除标志）的记录
for record in table:
    for field in record:
        print(field, "=", record[field], end = ",")
    print("-------------------------------------")
    print()

#遍历数据表中（加了删除标志）的记录
# for record in table.deleted:
#     for field in record:
#         print(field, "=", record[field], end = ",")
#     print("-------------------------------------")
#     print()





