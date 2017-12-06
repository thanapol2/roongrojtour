import json
import codecs
import configparser

PROVINCES = []
NATIONS = []
COUNTRYS = []

class province:
    with codecs.open('./backend/data/export.json', 'r', 'utf-8-sig') as data_file:
        data = json.load(data_file)
    rows = data["items"]
    for row in rows:
        PROVINCES.append(row["province_name"])
    # Nation / country
    config = configparser.ConfigParser()
    config.sections()
    config.read('./backend/data/config.ini')
    for row in config['TOUR_DETAIL']['NATION'].split(','):
        NATIONS.append(row)
    for row in config['TOUR_DETAIL']['COUNTRY'].split(','):
        COUNTRYS.append(row)


