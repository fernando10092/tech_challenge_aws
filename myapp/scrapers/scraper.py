import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from datetime import datetime

def getData():
    response = requests.get("https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ==")

    dados = response.json()

    data = dados["header"]["date"]
    text_data = str(data).replace("/", "-")

    lista = dados["results"]
    df = pd.DataFrame(lista)

    # Salvar em formato Parquet
    df.to_parquet(f"data_extract/{text_data}.parquet", index=False)

    # Salvar em Excel (comentado caso queira usar)
    # df.to_excel(f'{text_data}.xlsx', index=False)

    return df
