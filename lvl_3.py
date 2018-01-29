import urllib.request as urllib2
import re

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()


pattern = re.compile(r'[A-Za-mo-z]+')
print(' '.join(re.findall(pattern, str(page).strip())))
# e q u a l i t y
