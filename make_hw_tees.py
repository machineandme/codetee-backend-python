from app import make_tee
from pathlib import Path


CODES = Path("codes")
make_tee('bash.bash', 'echo', 'scrap.jpg', True)
make_tee('bash.bash', 'echo', 'scrap.jpg', False)
for file_name in CODES.iterdir():
    with open(str(file_name)) as file:
        code = file.read()
    for dark in [True, False]:
        folder = Path('web/shirt') / (file_name.name.split(".")[-1] + ('_dark' if dark else '_light'))
        folder.mkdir(parents=True, exist_ok=True)
        print(folder)
        make_tee(file_name, code, folder / 'tee.jpg', dark)
