# Test

You can (and should) organize tests into multiple files so that related tests go together. This lets you run a bunch of files at once.

```shell
python -m unittest
# ...
# ----------------------------------------------------------------------
# Ran 12 tests in 0.000s
# 
# OK
```

Same as before you can use `-h` to see what you can do.

```shell
python -m unittest -h
# usage: python3 -m unittest [-h] [-v] [-q] [--locals] [-f] [-c] [-b] [-k TESTNAMEPATTERNS] [tests ...]
# ...
```

And you can see in this form `-k` lets you specify test name patterns.

```shell
python -m unittest -k TestIntegerMethods -v
# ... Ran 8 tests in 0.000s ...
python -m unittest -k TestIntegerMethods.test_multiplication -v
# ... Ran 1 test in 0.000s ...
```

Notably I snuck in some more tests. Take a look...
