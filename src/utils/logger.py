# src/utils/logger.py
import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 1️⃣ Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 2️⃣ Configure log file name
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# 3️⃣ Create a universal logger function
def get_logger(name="UniversalLogger"):
    """
    Creates and returns a logger instance.
    
    :param name: Name of the logger (use module name for tracking).
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    
    if logger.hasHandlers():
        return logger  # Prevent duplicate handlers if called multiple times

    logger.setLevel(logging.DEBUG)  # Log everything from DEBUG and above

    # 4️⃣ Format the log messages
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 5️⃣ Console Handler (Print logs in terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Only show INFO+ in terminal
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # 6️⃣ File Handler (Save logs to file with rotation)
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when="midnight", interval=1, backupCount=7  # Rotate logs daily, keep 7 days
    )
    file_handler.setLevel(logging.DEBUG)  # Save all logs in file
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger