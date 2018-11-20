import redis


# 基类，初始化redis连接
class Base(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', passwd='123456', port=6379, db=0, decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)


class List_Test(Base):
    pass


