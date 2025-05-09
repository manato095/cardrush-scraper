import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 出力フォルダが無ければ作成
os.makedirs("output", exist_ok=True)

url = 'https://www.cardrush-pokemon.jp/phone/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

items = []

for product in soup.select('.list_item'):
    name = product.select_one('.product_name')
    price = product.select_one('.price')

    if name and price:
        items.append({
            '商品名': name.text.strip(),
            '価格': price.text.strip()
        })

df = pd.DataFrame(items)

output_path = os.path.join('output', 'cardrush_products.xlsx')
df.to_excel(output_path, index=False)
print(f"Saved {len(df)} items to {output_path}")
