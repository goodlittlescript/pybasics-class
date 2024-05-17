# The pathlib module provides a generally-easier
# way to work with paths.  You'll see both so
# it's good to know them both.
#
# https://docs.python.org/3/library/pathlib.html

from pathlib import Path

filename = Path("stock-prices.csv")
print(f"filename: {filename}")

abspath = filename.resolve()
print(f"absolute path: {abspath}")

dirname = abspath.parent
print(f"dirname: {dirname}")

basename = abspath.stem
print(f"basneame: {basename}")

extname = abspath.suffix
print(f"extname: {extname}")

if filename.exists():
    print("the file exists")
else:
    print("the file does not exist")

if filename.is_file():
    print("the file is a file")
else:
    print("the file is not a file")

if filename.is_dir():
    print("the file is a dir")
else:
    print("the file is not a dir")
