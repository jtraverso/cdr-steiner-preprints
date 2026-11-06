"""Draw a local example of late singleton assignment on five points."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

root = Path(__file__).parent
fonts = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
regular = ImageFont.truetype(str(fonts / "arial.ttf"), 33)
bold = ImageFont.truetype(str(fonts / "arialbd.ttf"), 36)
ink, blue, rust, gray = "#243747", "#21577d", "#9a4c2a", "#9aa3a7"

for language in ("en", "es"):
    image = Image.new("RGB", (1500, 410), "white")
    draw = ImageDraw.Draw(image)
    titles = (("Matching of u", "Matching of u′", "Closing block")
              if language == "en" else
              ("Emparejamiento de u", "Emparejamiento de u′", "Bloque de cierre"))
    for i, title in enumerate(titles):
        draw.text((250 + i * 500, 40), title, font=bold, fill=ink, anchor="mm")
    for j, (color, edges) in enumerate(((blue, [(0,1),(2,3)]), (rust, [(0,2),(1,3)]))):
        x = 140 + j * 500
        vertices = [(x,140),(x+210,140),(x,290),(x+210,290)]
        for a, b in edges:
            draw.line([vertices[a], vertices[b]], fill=color, width=7)
        for i, (vx,vy) in enumerate(vertices):
            draw.ellipse((vx-24,vy-24,vx+24,vy+24), fill="white", outline=color, width=4)
            draw.text((vx,vy), str(i+1), fill=ink, anchor="mm", font=regular)
        draw.ellipse((x+82,191,x+128,237), fill="white", outline=gray, width=3)
        draw.text((x+105,213), "v", fill=ink, anchor="mm", font=regular)
    tri = [(1140,278),(1360,278),(1250,130)]
    for src, dst, color in ((0,1,ink),(0,2,blue),(1,2,rust)):
        draw.line([tri[src],tri[dst]],fill=color,width=7)
    for (x,y), label in zip(tri, ("u","u′","v")):
        draw.ellipse((x-27,y-27,x+27,y+27), fill="white", outline=ink,width=3)
        draw.text((x,y),label,font=regular,anchor="mm",fill=ink)
    draw.text((1250,355),"reserved pair uu′" if language=="en" else "par reservado uu′",
              font=regular,fill=ink,anchor="mm")
    image.save(root / f"pairing_{language}.png", dpi=(225,225))
