import json
import codecs
import configparser
import backend.dao as dao

class config_data:
    PROVINCES = []
    NATIONS = []
    COUNTRYS = []
    COMPANY_TYPES = []
    BANKS = []
    PAYMENT_TYPES = []
    RT_TYPE = []
    RTS_TYPE = []

    def __init__(self):
        with codecs.open('./backend/data/export.json', 'r', 'utf-8-sig') as data_file:
            data = json.load(data_file)
        rows = data["items"]
        for row in rows:
            self.PROVINCES.append(row["province_name"])
        # Nation / country
        config = configparser.ConfigParser()
        config.sections()
        config.read('./backend/data/config.ini')
        for row in config['TOUR_DETAIL']['NATION'].split(','):
            self.NATIONS.append(row)
        for row in config['TOUR_DETAIL']['COUNTRY'].split(','):
            self.COUNTRYS.append(row)
        for row in config['TOUR_DETAIL']['COMPANY_TYPE'].split(','):
            self.COMPANY_TYPES.append(row)
        for row in config['PAYMENT_DETAIL']['BANK'].split(','):
            self.BANKS.append(row)
        for row in config['INVOICE_DETAIL']['RT'].split(','):
            self.RT_TYPE.append(row)
        for row in config['INVOICE_DETAIL']['RTS'].split(','):
            self.RTS_TYPE.append(row)

        self.PAYMENT_TYPES = dao.getPaymentType()


