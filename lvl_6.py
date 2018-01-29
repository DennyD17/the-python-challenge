import pickle
import urllib.request as urllib2

peack_hill = pickle.loads(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read())

for item in list(peack_hill):
    s = ''
    for points in item:
        s += points[0] * int(points[1])
    print(s)

