from app import syntax, distortion
from app.stylez.whtblz import Style

from PIL import Image


BASE = "/Users/nikolaykiselev/Life/shirts/language-examples/"
FILEPATH = "go.go"
with open(BASE + FILEPATH) as file:
    TEST_CODE = file.read()
TEST_CODE = '''print("Hello world")'''
tokens = [i for i in syntax.tokenize(FILEPATH, TEST_CODE)]
img = syntax.show_pic(iter(tokens), Style)
img.show()
# distortion.random_swap(img)
tjpg = Image.open("web/shirt/hw1/tee.jpg")
tjpg.paste(Style.background_color, [0, 0, tjpg.size[0], tjpg.size[1]])
tjpg.paste(img, (750, 500), img)
tjpg.save("web/shirt/tee.jpg")