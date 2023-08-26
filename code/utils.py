from urllib import request
import requests as r
import pandas as pd

def download_files(data):
    for filename, url, extension in data:
        request.urlretrieve(url, f'../data/{filename}.{extension}')
        print(f"Downloaded '{filename}' to 'data/' folder.")

def extract_html_table(data, table_header=0, na_values=None):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36", "X-Requested-With": "XMLHttpRequest"}
    for filename, url, extension in data:
        webpage = r.get(url, headers=header)
        df = pd.read_html(webpage.text, header=table_header, na_values=na_values)[0].dropna()
        out = df.to_json(orient='records', lines=True)

        with open(f'../data/{filename}.{extension}', 'w') as f:
            f.write(out)
            print(f"Downloaded '{filename}' to 'data/' folder.")