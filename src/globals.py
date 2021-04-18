import logging
from pathlib import Path

# LOGGING
log_fmt = '%(asctime)s - %(message)s'
log_datefmt = '%Y-%m-%d %I:%M:%S'
log_defaultlvl = 'INFO'
logging.basicConfig(format=log_fmt, datefmt=log_datefmt, level=log_defaultlvl)


# DIRECTORIES
project_dir = Path(__file__).resolve().parents[1]
raw_data_dir = project_dir / 'data' / 'raw'
interim_data_sir = project_dir / 'data' / 'interim'
processed_data_dir = project_dir / 'data' / 'processed'

