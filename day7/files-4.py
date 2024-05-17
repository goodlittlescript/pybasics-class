# File names have several parts
# which can be accessed in a variety
# of ways.
#
# https://docs.python.org/3/library/os.path.html

import os

filename = "stock-prices.csv"
print(f"filename: {filename}")

abspath = os.path.abspath(filename)
print(f"absolute path: {abspath}")

dirname = os.path.dirname(abspath)
print(f"dirname: {dirname}")

basename = os.path.basename(abspath)
print(f"basneame: {basename}")

root, extname = os.path.splitext(abspath)
print(f"root: {root}")
print(f"extname: {extname}")

if os.path.exists(filename):
    print("the file exists")
else:
    print("the file does not exist")

if os.path.isfile(filename):
    print("the file is a file")
else:
    print("the file is not a file")

if os.path.isdir(filename):
    print("the file is a dir")
else:
    print("the file is not a dir")
