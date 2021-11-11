stock_prices = {}
with open("stock_prices.csv", "r") as f:
    for i in f:
        tokens = i.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices)