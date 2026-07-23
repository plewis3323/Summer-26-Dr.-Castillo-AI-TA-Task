from PIL import Image

# (page, seg, y0, y1) -- full width 0-1700, independent boundaries chosen fresh
# from the rendered page images (not copied from the archived run's crops).
BOXES = [
    ("page01", "seg01", 0,    360),
    ("page01", "seg02", 260,  690),
    ("page01", "seg03", 560,  960),
    ("page01", "seg04", 850,  1300),
    ("page01", "seg05", 1150, 1650),
    ("page01", "seg06", 1550, 2200),

    ("page02", "seg01", 0,    640),
    ("page02", "seg02", 520,  1170),
    ("page02", "seg03", 1020, 1670),
    ("page02", "seg04", 1520, 2130),

    ("page03", "seg01", 0,    360),
    ("page03", "seg02", 260,  620),
    ("page03", "seg03", 520,  870),
    ("page03", "seg04", 800,  1220),
    ("page03", "seg05", 1100, 1560),
    ("page03", "seg06", 1450, 2020),

    ("page04", "seg01", 0,    460),
    ("page04", "seg02", 350,  760),
    ("page04", "seg03", 660,  1110),
    ("page04", "seg04", 1010, 1460),
    ("page04", "seg05", 1360, 1760),
    ("page04", "seg06", 1660, 2200),
]

pages = {}
for pnum in ["1", "2", "3", "4"]:
    pages[pnum] = Image.open(f"page-{pnum}.png")

for page, seg, y0, y1 in BOXES:
    pnum = page[-1]
    img = pages[pnum]
    w, h = img.size
    crop = img.crop((0, y0, w, min(y1, h)))
    crop.save(f"{page}_{seg}.png")
    print(f"{page}_{seg}.png -> {crop.size}")
