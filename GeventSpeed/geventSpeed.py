import gevent
from gevent import monkey
import urllib.request
import traceback

monkey.patch_all()
 
# 例子一：
# def test1():
#     print(12) 
#     gevent.sleep(3)
#     print (34)
 
# def test2():
#     print (56)
#     gevent.sleep(2)
#     print (78)
 
# gevent.joinall([
#     gevent.spawn(test1),
#     gevent.spawn(test2),
# ])


# 例子二：
def run_task(url):
    print("The task url:%s" % url)
    try:
        response = urllib.request.urlopen(url)
        result = response.read()
        print("done: %s" % url)
    except:
        traceback.print_exc()
        # print(e)
    pass

if __name__ == "__main__":
    urls = ['http://www.baidu.com', 'http://www.cn.bing.com', 'https://blog.csdn.net']
    greents = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greents)