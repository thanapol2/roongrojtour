import configparser
import cx_Oracle
import os

class dao:
    os.environ["NLS_LANG"] = ".UTF8"
    config = configparser.ConfigParser()
    config.sections()
    config.read('./backend/data/database.ini')
    USER = config['CONFIG']['USER']
    PASS = config['CONFIG']['PASS']
    DB_URL = config['CONFIG']['DB_URL']