import pymysql
import traceback

class MysqlHelper:
    def __init__(self, host, user, password, port, database, charset):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.charset = charset
        self.db = None
        self.curs = None

    # 数据库连接
    def openmysql(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, database=self.database, charset=self.charset)
        self.curs = self.db.cursor()

    # 数据库关闭
    def closemysql(self):
        self.curs.close()
        self.db.close()
        
    # 数据增删改
    def cud(self, sql):
        self.openmysql()
        try:
            self.curs.execute(sql)
            self.db.commit()
            # print("cud ok")
        except:
            print('error!!')
            self.db.rollback()
            traceback.print_exc()
        self.closemysql()

    # 数据查询
    def find(self, sql):
        self.openmysql()
        try:
            self.curs.execute(sql)
            results = self.curs.fetchall()
            self.closemysql()
            # print("find ok")
            return results
        except:
            print('error!!')
            traceback.print_exc()
