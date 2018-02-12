#!/Users/map/bin/python
import logging
# log formatting examples
item = "shoes"
price = 2.99

# good way
logging.info("Your %s costs $%0.2f.", item, price)

# good way
logging.info("Your %s costs $%0.2f." % (item, price))  ## There is a computation cost because the 
                                                       ## log message is formatted before throwing away 


## fstring can't be used in logging module !!
