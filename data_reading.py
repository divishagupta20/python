import pandas as pd
from io import StringIO
data = '''{
  "Divisha": {
    "year": 2023,
    "holidays": 12
  },
  "Zaara": {
    "year": 2022,
    "holidays": 10
  },
  "Aniket": {
    "year": 2023,
    "holidays": 8
  }
}'''

df = pd.read_json(StringIO(data))

print(df)
print(df.to_json())

url = "https://www.w3schools.com/html/html_tables.asp"

d = pd.read_html(url)
print(d)

'''url = "https://en.wikipedia.org/wiki/Mobile_country_code"
d = pd.read_html(url,match="Country",header=0)[0] #list
print(d)'''