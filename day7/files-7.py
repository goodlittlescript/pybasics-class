# Some special characters...
#
# "." is interpreted as the current directory
# ".." is interpreted as "one directory up"
#

from pathlib import Path

result = Path(".").resolve()
print(f".\t{result}")

result = Path("..").resolve()
print(f"..\t{result}")

result = Path("../..").resolve()
print(f"../..\t{result}")
