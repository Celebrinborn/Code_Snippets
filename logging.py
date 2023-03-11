import logging
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(os.path.join('logs', f'{os.path.basename( sys.argv[0])}.log'))
c_handler.setLevel(logging.WARNING) # Change me to change console messages
f_handler.setLevel(logging.WARNING) # Change me to change file messages

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)




# source: https://medium.com/pythoneers/master-logging-in-python-73cd2ff4a7cb