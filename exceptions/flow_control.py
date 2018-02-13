import logging
try:
    from speedyjson import load
except ImportError:
    from json import load


# Built-in Exceptions
# - KeyError for dictionaries
# - IndexError for lists
# - TypeError for incompatible type
# - ValueError for bad value
# - NameError for unkown identifier

user_input = ''
# Multiple Except Blocks
try:
    value = int(user_input)
except ValueError:
    logging.error("Bad Vlue from %r", user_input)
except TypeError:
    logging.critical("Bad Vlue from %r", user_input)
finally:
    logging.error("Yep, hit finnaly")
