import redis


# 基类，初始化redis连接
class Base(object):
    def __init__(self):
        # self.pool = redis.ConnectionPool(host='localhost', passwd='123456', port=6379, db=0, decode_responses=True)
        # self.r = redis.Redis(connection_pool=self.pool)
        self.r = redis.StrictRedis(host='localhost', password=123456, port=6379, db=1, decode_responses=True)


class TestString(Base):
    '''
    set: 设置值
    get: 获取值
    mset: 设置多个值
    mget: 获取多个值
    append: 添加字符串
    del: 删除
    incr/decr: 增加/减少 1
    '''
    def test_set(self):
        '''set: 设置值'''
        rest = self.r.set('user', 'Job')
        print(rest)

    def test_get(self):
        '''get: 获取值'''
        regt = self.r.get('user')
        print(regt)
        return regt

    def test_mset(self):
        ''' mset: 设置多个值'''
        users = {
            'user1': 'Jack',
            'user2': 'Mike',
            'user3': 'Bob'
        }
        mrest = self.r.mset(users)
        print(mrest)

    def test_mget(self):
        '''mget: 获取多个值'''
        users = ['user', 'user1', 'user2', ' user3']
        mgest = self.r.mget(users)
        print(mgest)
        return mgest

    def test_del(self):
        '''del: 删除'''
        redel = self.r.delete('user3')
        print(redel)

    def test_incr(self):
        '''incr/decr: 增加/减少 1'''
        reincr = self.r.incr('id')
        print(reincr)


class TestList(Base):
    """
    lpush/rpush: 从左/右插入数据
    lrange: 获取指定长度的数据
    ltrim: 截取一定长度的数据
    lpop/rpop: 移除最左/最右的数据
    lpushx/rpushx: key存在时才插入数据，不存在则不插入
    """
    def test_push(self):
        '''lpush/rpush: 从左/右插入数据'''
        eatlist = ('Amy','Jack','Mike')
        relpu = self.r.lpush('user_eat', *eatlist)
        print(relpu)
        relra = self.r.lrange('user_eat', 0, -1)
        print(relra)

    def test_pop(self):
        ''' lpop/rpop: 移除最左/最右的数据'''
        rerpo = self.r.rpop('user_eat')
        print(rerpo)
        relra = self.r.lrange('user_eat', 0, -1)
        print(relra)


class TestSet(Base):

    def test_sadd(self):
        '''sadd: 增加元素'''
        animals = ['dog','cat','tigger']
        resad = self.r.sadd('zoors', *animals)
        print(resad)
        resmebers = self.r.smembers('zoors')
        print(resmebers)

    def test_srem(self):
        '''srem: 删除元素'''
        resrem = self.r.srem('animals', 'dog')
        print(resrem)
        resmebers = self.r.smembers('animals')
        print(resmebers)

    def test_sinter(self):
        '''sinter: 返回几个集合的交集'''
        resinter = self.r.sinter('animals', 'zoors')
        print(resinter)

    def test_sunion(self):
        '''sunion: 返回几个集合的并集'''
        resunion = self.r.sunion('animals', 'zoors')
        print(resunion)


def main():
    # strobj = TestString()
    # strobj.test_set()
    # strobj.test_get()
    # strobj.test_mset()
    # strobj.test_mget()
    # strobj.test_del()
    # strobj.test_incr()

    # tlist = TestList()
    # tlist.test_push()
    # tlist.test_pop()

    tset = TestSet()
    # tset.test_sadd()
    # tset.test_srem()
    # tset.test_sinter()
    tset.test_sunion()


if __name__ == "__main__":
    main()



