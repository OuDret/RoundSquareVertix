import math
from PIL import Image, ImageDraw

output_file = "out.lef"
EDGE_SIZE = 50
CORNER_RAD = 10
N_CORNER_RECTS = 20
corner_rect_width = CORNER_RAD/N_CORNER_RECTS
image = Image.new("RGB", (EDGE_SIZE*300, EDGE_SIZE*300), color="white")

def pitagoras(c1, h):
    return math.sqrt(h**2 - c1 **2)

def draw_rectangle(x1, y1, x2, y2, image):
    draw = ImageDraw.Draw(image)
    draw.rectangle([x1, y1, x2, y2], outline='red')

def write_lef(rectangles, output_file):
    f = open(output_file, "w")
    for rect in rectangles:
        x1, y1, x2, y2 = rect 
        f.write(f"RECT {round(x1,2)} {round(y1,2)} {round(x2,2)} {round(y2,2)} ;\n")
    f.close()

rectangles = []

# # # # # # # # # # # #
#
#  * 1 1 1 1 1 1 1 1 ·
#  2 1 1 1 1 1 1 1 1 3    
#  2 1 1 1 1 1 1 1 1 3   
#  2 1 1 1 1 1 1 1 1 3
#  2 1 1 1 1 1 1 1 1 3
#  2 1 1 1 1 1 1 1 1 3     
#  2 1 1 1 1 1 1 1 1 3    
#  2 1 1 1 1 1 1 1 1 3
#  2 1 1 1 1 1 1 1 1 3
#  + 1 1 1 1 1 1 1 1 -
#
# # # # # # # # # # # #

# 1
rectangles.append(( -EDGE_SIZE/2 + CORNER_RAD , -EDGE_SIZE/2 , EDGE_SIZE/2 - CORNER_RAD , EDGE_SIZE/2 ))
# 2
rectangles.append((             -EDGE_SIZE/2 ,      -EDGE_SIZE/2 + CORNER_RAD ,     -EDGE_SIZE/2 + CORNER_RAD ,     EDGE_SIZE/2 - CORNER_RAD ))
# 3
rectangles.append(( EDGE_SIZE/2 - CORNER_RAD ,      -EDGE_SIZE/2 + CORNER_RAD ,                   EDGE_SIZE/2 ,     EDGE_SIZE/2 - CORNER_RAD ))
#*+-·
for i in range (N_CORNER_RECTS):
    x1 =  corner_rect_width*(i+1)
    x2 =  corner_rect_width*(i)
    print(x1, x2)
    try:
        y2 = pitagoras(x2, CORNER_RAD)
        rectangles.append(( -EDGE_SIZE/2 + CORNER_RAD - x1,           EDGE_SIZE/2 - CORNER_RAD,        -EDGE_SIZE/2 + CORNER_RAD - x2,    EDGE_SIZE/2 - CORNER_RAD + y2))
        rectangles.append(( -EDGE_SIZE/2 + CORNER_RAD - x1,     -EDGE_SIZE/2 + CORNER_RAD - y2,        -EDGE_SIZE/2 + CORNER_RAD - x2,    -EDGE_SIZE/2 + CORNER_RAD))
        rectangles.append((  EDGE_SIZE/2 - CORNER_RAD + x2,           EDGE_SIZE/2 - CORNER_RAD,         EDGE_SIZE/2 - CORNER_RAD + x1,    EDGE_SIZE/2 - CORNER_RAD + y2))
        rectangles.append((  EDGE_SIZE/2 - CORNER_RAD + x2,     -EDGE_SIZE/2 + CORNER_RAD - y2,         EDGE_SIZE/2 - CORNER_RAD + x1,    -EDGE_SIZE/2 + CORNER_RAD))
    except:
        pass

print(rectangles)

for rect in rectangles:
    x1, y1, x2, y2 = rect
    draw_rectangle((x1+EDGE_SIZE)*100, (y1+EDGE_SIZE)*100, (x2+EDGE_SIZE)*100, (y2+EDGE_SIZE)*100, image)

write_lef(rectangles, output_file)

image.show()