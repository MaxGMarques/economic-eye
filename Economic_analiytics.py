import pandas as pd 
import requests
import urllib.request
from fredapi import Fred

fred = Fred(api_key='32e93f174922387961100acb2d768d21')

dados = pd.DataFrame({
    'Inflação': fred.get_series('CPIAUCSL'),
    'Desemprego': fred.get_series('UNRATE'),
    'GDP': fred.get_series('GDP')
})

dados = dados.dropna()

print(dados.tail())
