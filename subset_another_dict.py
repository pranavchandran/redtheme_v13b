# you want to make a dictionart that is a subset of anthoer dictionary
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# make a dictionary of all prices over 200
p1 = {key:value for key,value in prices.items() if value > 200}
print(p1)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

# creating a sequence of tuples 
p1_t = dict((key,value)for key,value in prices.items() if value>200)
print(p1_t)

p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)

