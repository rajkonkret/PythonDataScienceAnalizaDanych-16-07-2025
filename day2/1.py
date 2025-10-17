# data_url ='https://en.wikipedia.org/wiki/Wind_power'
# data = pd.read_html(data_url)
# data[1]

import requests
import pandas as pd
from io import StringIO
url = "https://en.wikipedia.org/wiki/Wind_power"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0 Safari/537.36"
}

resp = requests.get(url, headers=headers, timeout=20)
resp.raise_for_status()           # podniesie wyjątek, jeśli np. 403/404

html = StringIO(resp.text) # wymagane dla nowszych wersji Pandas
tables = pd.read_html(html)  # lista DataFrame’ów z tabeli na stronie
print(len(tables))
df = tables[0]                    # np. pierwsza tabela
print(df.head())
