# config.py
import os

class Config:
    DEBUG = True
    PORT = 5000
    HOST = '0.0.0.0'
    LOG_FILE = 'logs/tvc.log'
    LOG_LEVEL = 'INFO'
    
    # Caminhos dos dados
    DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
