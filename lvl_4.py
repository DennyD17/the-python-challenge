import urllib.request as urllib2
import re

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
word = ''

for item in re.findall(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', str(page)):
    word += item[4]

print(word)
