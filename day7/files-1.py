# Reading files is straightforward
file = open("stock-prices.csv")
data = file.read()
file.close()

print(data)
