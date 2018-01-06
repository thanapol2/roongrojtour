import backend.dao as dao
from datetime import datetime
import configparser
import backend.config_data as pro

print(dao.getPaymentDetail("1600002","Y"))