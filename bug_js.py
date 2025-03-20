from selenium import webdriver
from selenium.webdriver.common.by import By
import time


option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')


driver = webdriver.Chrome(options=option)

search_url = 'https://shopee.tw/search?keyword=i%20phone16%20pro%E6%89%8B%E6%A9%9F%E6%AE%BC&trackingId=searchhint-1742202419-2eeea0bb-030f-11f0-a76c-9ee5a2c1e03e'
driver.get(search_url)

time.sleep(5)

product = driver.find_element(By.CSS_SELECTOR,'div._1NoI8_._16BAGk')
price = driver.find_element(By.CSS_SELECTOR,'div._1w9jLI.QbH7Ig.U90Nhh')
rating = driver.find_element(By.CSS_SELECTOR,'div._3yD2QU')

for i in range(len(product)):
    product_name = product[i].text
    product_price = price[i].text if i<len(price) else "無價格資訊"
    product_rating = rating[i].text if i < len(rating) else "無評價"

    print(f"商品：{product_name}")
    print(f"價格：{product_price}")
    print(f"評價：{product_rating}")

driver.quit()
