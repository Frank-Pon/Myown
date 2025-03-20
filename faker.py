import pandas as pd 
import random

data = {
    'OrderID' : range(1,21),
    'Customer':random.choices(['Adam','Alan','Abner','Bob','Benson','Bill','Charlie','Cindy','Cyrus','Dan','Darius','David'],k=20),
    'Product':random.choices(['Laptop','Lamp','Table','Chair','Phone','Charger','Keyboard','Monitor'],k=20),
    'Quantity':[random.randint(1,5) for _ in range(20)],
    'Price':[random.randint(500,25000) for _ in range(20)],
    'Month':random.choices(['1月','2月','3月'],k=20)
}

df=pd.DataFrame(data)
df.to_excel('DailyExcel.xlsx',index = False)
print('Excel文件已生成')