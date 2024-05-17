# Typically you will use files in a "context"
# which ensures the file will be closed when
# it completes.

with open("stock-prices.csv") as f:
    data = f.read()
print(data)
