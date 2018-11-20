import datetime, time

start = datetime.datetime.now()
time.sleep(3)
end = datetime.datetime.now()

# 计算时间差,格式: 时分秒
def gettimediff(start,end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff

print(gettimediff(start,end))