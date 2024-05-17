# Files can be opened in "write" mode
# or "append" mode. What is the content
# of the file at the end of this?

with open("example.txt", "w") as f:
    f.write("line one\n")
    f.write("line two\n")

with open("example.txt", "w") as f:
    f.write("line uno\n")
    f.write("line dos\n")

with open("example.txt", "a") as f:
    f.write("line tres\n")
