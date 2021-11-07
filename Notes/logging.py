

Notes = \
"""
import logging (Requires importing the logging module)

# Logging Levels:
    1. DEBUG
    2. INFO
    3. WARNING
    4. ERROR
    5. CRITICAL

# One of the most used Logging Format: %(asctime)s - %(name)s - %(levelname)s - %(message)s

# Basic Logging -  This is Helpfull for small Projects and might get messy for large projects. 

    => print(logging.info("This is a Info Message.")) to simply print out lines


    # Simple Logging in a file.
    => logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


# Advanced Logging by setting up handler mannualy

    # Create a logger
    => logger = logging.getLogger(__name__)

    # Set the logging level
    => logger.setLevel(logging.INFO)

    # Create a Formatter
    => formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

    # Create a file handler
    => file_handler = logging.FileHandler('log_test.log')
    => file_handler.setFormatter(formatter)

    # Create a stream handler (Helps By Printing in the Console)
    => stream_handler = logging.StreamHandler()

    # Add the handlers to the logger
    => logger.addHandler(file_handler)
    => logger.addHandler(stream_handler)

Note: Logging Levels are set in the order of: DEBUG, INFO, WARNING, ERROR, CRITICAL
"""

print(Notes)
