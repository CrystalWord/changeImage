from PIL import Image

while True:
    n = input("请选择图片：")
    im = Image.open('%s' % n)
    print("图片类型为：")
    print(im.format)
    print("图片大小为：")
    print(im.size)

    w = int(input("请选择要转换成的宽度："))
    h = int(input("请选择要转换成的高度："))

    img=im.resize((w, h), Image.ANTIALIAS)
    if w == 16 and h == 16 or w == 32 and h == 32:
        img.save("%dx%d.jpg" % (w, h))
    else:
        img.save("%dx%d.jpg" % (w, h))
    img.show()
    
