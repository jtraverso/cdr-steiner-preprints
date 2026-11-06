"""Draw the seven blocks of the packaged (1,2,4) witness."""
from pathlib import Path
from math import sqrt
from itertools import combinations
from PIL import Image, ImageDraw, ImageFont

blocks = [(0,1,2),(0,3,4),(0,5,6),(1,3,6),(1,4,5),(2,3,5),(2,4,6)]
assert len({p for block in blocks for p in combinations(sorted(block),2)}) == 21
im = Image.new("RGB",(1020,660),"white")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf",33)
x,y,r=510,388,177
points={0:(x,y-2*r),1:(x-r*sqrt(3),y+r),3:(x+r*sqrt(3),y+r),5:(x,y)}
for i,a,b in [(2,0,1),(4,0,3),(6,1,3)]:
    points[i]=tuple((a1+b1)/2 for a1,b1 in zip(points[a],points[b]))
for a,b in [(0,1),(0,3),(1,3),(0,6),(1,4),(3,2)]:
    draw.line((points[a],points[b]),fill="#49545e",width=4)
draw.ellipse((x-r,y-r,x+r,y+r),outline="#49545e",width=4)
for i,(px,py) in points.items():
    j=0 if i==0 else 1 if i<3 else 2
    fill=["#e8ba58","#a4d0df","#dac5e2"][j]
    draw.ellipse((px-33,py-33,px+33,py+33),fill=fill,outline="#263441",width=3)
    draw.text((px,py),str(i),font=font,fill="#17232c",anchor="mm")
im.crop((135,0,885,615)).save(Path(__file__).with_name("fano.png"),dpi=(220,220))
