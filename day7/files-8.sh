#
# NOTE!! This is a shell script, not python!

# You can do all the same things in your shell...

ls *.py
ls .
ls ..
ls ../..

# You can get your current directory like this:
pwd
# or 
echo $PWD

# You can write to a file like this
echo "line one" > example.txt

# You can append a file like this:
echo "line two" >> example.txt

# You can "cat" a file to read it
cat example.txt

# And remove files with rm
rm example.txt
cat example.txt

# These are redirections... which you can do with your python as well.
python files-7.py > example.txt
cat example.txt

# Use 'tee' to see and save.
python files-7.py | tee example.txt
cat example.txt
