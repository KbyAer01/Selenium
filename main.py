import csv
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
sleep(5)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "livePreTable"))
    )
finally:
    pass
file=open('price.csv','w')
rows=element.find_elements(By.TAG_NAME,"tr")
with file:
    writer=csv.writer(file)
    writer.writerow(["name","price"])
    for row in rows[1:-1]:
        rowData=row.text.replace(',','').split(' ')
        writer.writerow([rowData[0],rowData[5]])

driver.close()