import logging
import os 
from datetime import datetime

Log_dir = "logs"
os.makedirs(Log_dir, exist_ok=True)

Log_file = os.path.join(Log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    filename=Log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_logger(self):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger

