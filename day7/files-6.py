# A common way to get a list of files is to "glob" for them.
# In a glob a '*' matches anything.

from pathlib import Path

files = Path().glob("*.py")
for file in files:
    print(f"found: {file}")
