import urllib.request as urllib2
import zipfile
import re

z, http_obj = urllib2.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip')
zip_file = zipfile.ZipFile(z, 'r')


def get_nothing_from_zip(nothing='90052.txt', s=''):
    try:
        nothing = re.search(r'[0-9]+', str(zip_file.read(nothing))).group()
    except AttributeError:
        print(s)
        return s
    else:
        file = nothing + '.txt'
        s += zip_file.getinfo(file).comment.decode("utf-8")
        get_nothing_from_zip(nothing=file, s=s)


get_nothing_from_zip()

# HOCKEY