from PIL import Image

img = Image.open('cave.jpg')

w, h = img.size

odd = Image.new('RGB', (w, h))
even = Image.new('RGB', (w, h))

for i in range(0, w):
    for j in range(0, h):
        px = img.getpixel((i, j))
        if (i + j) % 2:
            even.putpixel((i, j), px)
        else:
            odd.putpixel((i, j), px)

odd.save('odd.jpg')
even.save('even.jpg')

# "evil" on the odd image
