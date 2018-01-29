import string

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
    "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"

def translate(a):
    b = ''
    for letter in a:
        if letter in string.ascii_letters:
            b += string.ascii_letters[string.ascii_letters.index(letter) + 2]
        else:
            b += letter
    return b

print(translate(url))
# i hope you didnt trAnslAte it By hAnd. thAts whAt computers Are for. doing it in By hAnd is inefficient
# And thAt's why this text is so long. using string.mAketrAns() is recommended. now Apply on the url.
# I think, it is more difficult
#ocr