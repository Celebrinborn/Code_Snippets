import logging.config
import yaml
import logging
import os

import os
import logging.config
import yaml


#os.environ['LOG_FILE_NAME'] = 'hello_world.log' # manually set an environ variable to demo how this code works

# Set the log file name using an environment variable if present, or a default value otherwise
log_file_name = os.environ.get('LOG_FILE_NAME', 'app.log')

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

# Configure the logging module
with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    # Update the filename in the configuration dictionary
    config['handlers']['file']['filename'] = f'./logs/{log_file_name}'
    logging.config.dictConfig(config)




logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
