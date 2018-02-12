#!/Users/map/bin/python

#formatting examples

template="Your {} costs ${:0.2f}."
output = template.format("cup of coffee", 7.99)
print(output)

## in 3.6 you have f strings, cool!
## 
item="bag o' donuts"
price = 1.99
print(f"Your {item} costs ${price:0.2f}.")

## old school with % and dictionary
## The two below still used for logging moduel 
## 
template="Your %s costs %0.2f."
output = template % ("cup of tea", 2.99)
print(output)

data = {"item": "burger", "price": 4.95}
print ("Your %(item)s costs $%(price)0.2f." % data)
