import pandas as pd
import os
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(data_url: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        
        df = pd.read_csv(data_url)
        logger.debug('Data loaded from %s', data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error('CSV parsing error while loading data from %s: %s', data_url, e)
        raise
    except FileNotFoundError as e:
        logger.error('File not found: %s', data_url)
        raise
    except Exception as e:
        logger.error('An error occurred while loading data from %s: %s', data_url, e)
        raise
try:
    data_url = 'your_data.csv'  # Replace with your actual CSV file path
    data = load_data(data_url)
except Exception as e:
    logger.error('Failed to load data: %s', e)
