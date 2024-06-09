from turtle import Screen, bgpic, done

from PIL import Image

scr = Screen()
im = Image.open("fon.png")
x, y = im.size
x0, y0 = (x - 768) // 2, (y - 648) // 2
im_n = im.crop((x0, y0, x0 + 768, y0 + 648))
im_n.save("f.png")
scr.setup(startx=0, starty=0)
scr.bgpic("f.png")
done()


