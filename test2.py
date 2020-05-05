from app import syntax, distortion
from app.syntax import MegaSexyStyle

from PIL import Image


BASE = "/Users/nikolaykiselev/Life/shirts/language-examples/"
FILEPATH = "go.go"
with open(BASE + FILEPATH) as file:
    TEST_CODE = file.read()
tokens = [i for i in syntax.tokenize(FILEPATH, TEST_CODE)]
img = syntax.show_pic(iter(tokens))
# distortion.random_swap(img)
tjpg = Image.open("web/shirt/tee.jpg")
tjpg.paste(MegaSexyStyle.background_color, [0, 0, tjpg.size[0], tjpg.size[1]])
tjpg.paste(img, (750, 500), img)
tjpg.save("web/shirt/tee.jpg")