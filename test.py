import main

with open("main.py") as file:
    TEST_CODE = file.read()


def test_cli():
    tokens = [i for i in main.tokenize('main.py', TEST_CODE)]
    print(main.show_cli(iter(tokens)))


def test_image():
    tokens = [i for i in main.tokenize('main.py', TEST_CODE)]
    img = main.show_pic(iter(tokens))
    img.show()
