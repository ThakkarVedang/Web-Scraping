from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("C:/Users/vedang/Desktop/Semester 7/DS(Data Science)/Prac1/chromedriver")
products=[]
prices=[]
driver.get("https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A1389432031%2Cp_85%3A10440599031%2Cp_36%3A400000-1000000&pd_rd_r=67b37192-12f5-443d-a571-2c12224ee356&pd_rd_w=CMTUy&pd_rd_wg=0ziES&pf_rd_p=04635875-775c-4bf0-b81d-c9df5ebfba3d&pf_rd_r=M4F0Y5X8TZENK95EM25N&qid=1626802564&rnid=1318502031&ref=pd_gw_unk")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',attrs={'class':'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'}):
    name=a.find('h2', attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
    price=a.find('span', attrs={'class':'a-price'})

    try:
        products.append(name.text)
        prices.append(price.text)

    except:
        continue

df = pd.DataFrame({'Product Name': products,'Price': prices})
df.to_csv('product.csv', index=False, encoding='utf-8')
df.transpose()

