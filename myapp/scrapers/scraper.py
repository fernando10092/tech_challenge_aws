import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from datetime import datetime

def getData():
    response = requests.get("https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ==")

    dados = response.json()

    #data = datetime.now().strftime("%Y-%m-%d")
    data = dados["header"]["date"]
    text_data = str(data)
    text_data = text_data.replace("/", "-")

    lista = dados["results"]

    print(lista)

    return pd.DataFrame(lista).to_excel(f'{text_data}.xlsx', index=False)

    #with open(f'{data}.csv', mode="w", encoding="utf-8") as arquivo:
    #    arquivo.write(response.text)
