#!/Users/map/bin/python
# So this is being coded on a Mac w/ Anaconda 3 installed.
# Hence we are poining to ${HOME}/anaconda3/bin/python
# Change as needed.
import logging

logging.warning('Look out')
logging.error('OUCH!! Look out')

# -- debug:   detail info for diagnosis
# -- info:    confirm that things are working
# -- warning: something unexpected happened or possible future error 
# -- error:   not able to perform function due to serious problem
# -- critical: serious error, unable to continue running
# 
# NOTE: compatible with syslog
