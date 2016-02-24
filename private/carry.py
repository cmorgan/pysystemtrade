# flake8:noqa
import Quandl
import pandas as pd
import os


CONTRACT_CODE = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
# british pound
BP = ['H', 'M', 'U', 'Z']

# 'https://www.quandl.com/api/v3/datasets/CME/CME/BPH2014.csv'
'''


'''


def contract_string(code, year, month):
    index = month - 1
    return '{}{}{}'.format(code, CONTRACT_CODE[index], year)


# british pound
def bp(month, year):
    source = 'CME'
    return source, contract_string('BP', year, month)


def get():
    year = 1984
    month = 9
    print('{}{:02d}'.format(year, month))
    source, contract = bp(month, year)
    dataset = source + '/' + contract
    print(dataset)
    return Quandl.get(dataset)


def csv():
    legacycsv = os.path.join('..', 'sysdata', 'legacycsv')
    csv_file = 'GBP_carrydata.csv'
    csv_path = os.path.join(legacycsv, csv_file)
    return pd.read_csv(csv_path)
