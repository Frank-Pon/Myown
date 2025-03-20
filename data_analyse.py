import pandas as pd
import random

try:
    df = pd.read_excel('DailyExcel.xlsx')
except:
    print('找不到DailyExcel.xlsx,請再次確認')
    exit()

columns = ['Customer','Product','Month']
option = input('請輸入分組欄位名稱（Customer/Product/Month）:')
if option not in columns:
    print('輸入無效,請選擇有效的欄位名稱')
    exit()

monthlysales = df.groupby(option)['Price'].sum()

monthlysales.to_excel('sum.xlsx')

print('報表已產生')