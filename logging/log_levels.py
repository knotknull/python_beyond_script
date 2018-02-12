#!/Users/map/bin/python
# So this is being coded on a Mac w/ Anaconda 3 installed.
# Hence we are poining to ${HOME}/anaconda3/bin/python
# Change as needed.
import logging

## logging.basicConfig() default threshold is logging.WARNING
## ignores everything less than logging.INFO
## logging.basicConfig(level=logging.INFO) 

## set logging to a file
## logging.basicConfig(filename="log.txt")   # appends to file
## or overwrite
## logging.basicConfig(filename="log.txt", filemode="w")   # appends to file


logging.debug('small detail, useful info ')
logging.info('informative data ')
logging.warning('This is a warning message ')
logging.error('Error Message !!')
logging.critical('Critical Message')

# -- debug:   detail info for diagnosis
# -- info:    confirm that things are working
# -- warning: something unexpected happened or possible future error 
# -- error:   not able to perform function due to serious problem
# -- critical: serious error, unable to continue running
# 
# NOTE: compatible with syslog

## Two meaning of log level
## 1. severity of message (debug, info, error, etc.)
## 2. threshold for ignore messages


