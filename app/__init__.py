from app import syntax, distortion
from PIL import Image


def make_tee(file_name, code, save_to, dark=False):
    tokens = [i for i in syntax.tokenize(file_name, code)]
    img = syntax.show_pic(iter(tokens), "paraiso-dark" if dark else "paraiso-light")
    tjpg = Image.open("web/shirt/plain/tee.jpg")
    tjpg.paste("#000" if dark else "#fff", [0, 0, tjpg.size[0], tjpg.size[1]])
    tjpg.paste(img, (750, 500), img)
    tjpg.save(save_to)
