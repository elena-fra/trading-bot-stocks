import logging
import os 
from config import LOG_FILE, LOG_FOLDER

def setup_logger():
    '''
    configura il sistema di logging del bot
    se la cartella logs non esiste, la crea
    '''
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)
    
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s-%(message)s"
        )
    
    return logging
    