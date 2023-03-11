import logging.config
import yaml
import logging
import os

# Check if logging configuration file exists
if not os.path.exists('logging.yaml'):
    # If it doesn't exist, print a message to the user and crash
    print("Logging configuration file not found.")
    print("Current working directory: ", os.getcwd())
    print("Files and directories in current directory: ", os.listdir())
    print("All files and directories in subdirectories: ")
    for root, dirs, files in os.walk("."):
        for name in files + dirs:
            print(os.path.join(root, name))
    raise FileNotFoundError("logging.yaml file not found.")

# Load logging configuration from file
with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)



logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
