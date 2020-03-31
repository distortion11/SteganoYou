from PIL import Image
from re import findall
def stega_decrypt():

    a=[]
    img = Image.open("newimage.png")
    pix = img.load()
    f_key = []

    f = open("keys.txt", 'r')
    for line in f.readlines():
        f_key.append(line)
    for elem in f_key:
        k = elem.find(",", 0, len(elem))
        a.append(pix[int(elem[1:k]), int(elem[k + 1:len(elem) - 2])][0])

    s = " "
    for elem in a:
        s=s+chr(elem)

    return(s)


print("you message: ", stega_decrypt())