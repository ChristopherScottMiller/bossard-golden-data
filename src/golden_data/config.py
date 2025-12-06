# src/golden_data/config.py

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")

DATA_RAW = BASE_DIR / 'data' / 'raw'
DATA_INTERIM = BASE_DIR / 'data' / 'interim'
DATA_PROCESSED = BASE_DIR / 'data' / 'processed'
MAPPINGS_DIR = BASE_DIR / 'mappings' / ''

DATA_FILENAME = os.getenv('DATA_FILENAME', 'bossard_raw.csv')

def get_raw_data_path() -> Path:
    return DATA_RAW / DATA_FILENAME
