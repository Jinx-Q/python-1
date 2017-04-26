import  urllib.request
cat = urllib.request.urlopen('http://placekitten.com/300/350')
catimg = cat.read()
with open('catimgsd.jpg','wb') as f :
    f.write(catimg)
print(cat.geturl())