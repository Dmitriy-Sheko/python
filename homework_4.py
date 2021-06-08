#2,3
import requests
from decimal import *
from datetime import datetime
getcontext().prec = 4
def currency_rates(valute):
    valute = valute.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if valute not in response:
        return None
    val = response[response.find('<Value>', response.find(valute)) + 7:response.find('</Value>', response.find(valute))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(val.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"
# print(currency_rates('EUR'))
# print(currency_rates('USD'))

#4
import utils
print(utils.currency_rates('EUR'))

