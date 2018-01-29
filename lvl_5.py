import urllib.request as urllib2
import re


def get_nothing(nothing='66831'):
    page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    try:
        nothing = re.search(r'[0-9]+', str(urllib2.urlopen(page + nothing).read())).group(0)
    except AttributeError:
        return str(urllib2.urlopen(page + nothing).read())
    if nothing != '':
        print(nothing)
        get_nothing(nothing)

print(get_nothing())
# peak.html
