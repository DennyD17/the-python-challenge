from PIL import Image
import urllib.request as urllib2

img, http_obj = urllib2.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(img)
row = [img.getpixel((i, 47)) for i in range(0, img.width)]
list_of_chords = []
for item in row:
    if item[0] == item[1] == item[2]:
        list_of_chords.append(item[0])

print(''.join(map(chr, list_of_chords)))
l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in l:
    print(chr(i))