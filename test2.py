from app import syntax, distortion

import os

BASE = "/Users/nikolaykiselev/Life/shirts/language-examples/"
for i in os.listdir(BASE):
    FILEPATH = i
    with open(BASE + FILEPATH) as file:
        TEST_CODE = file.read()
    tokens = [i for i in syntax.tokenize(FILEPATH, TEST_CODE)]
    img = syntax.show_pic(iter(tokens))
    # distortion.random_swap(img)
    img.save("tests/"+FILEPATH+".png")
    print(FILEPATH)