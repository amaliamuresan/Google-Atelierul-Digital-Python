from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Firefox(executable_path='C:\\Users\\amali\\.wdm\\drivers\\geckodriver\\win64\\v0.29.1\\geckodriver.exe')
#
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2019.htm")
#
# table = browser.find_element_by_xpath('//*[@id="Data_table"]')
# table_text = table.text
#
# print(table_text)
#
# lista = table_text.split('\n')
# header_len = browser.find_element_by_xpath('//*[@id="Data_table]/table/thead/tr')
# header = header_len.text.spliy('\n')
# dictionar = {i: [] for i in header}

browser.get("https://www.bnr.ro/files/xml/nbrfxrates2019.htm")
table = browser.find_element_by_xpath('//*[@id="Data_table"]')
table_text = table.text
# print(table_text)
lista = table_text.split('\n')
header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
print(dictionar)


for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])

df = pd.DataFrame(dictionar)
df.to_csv("week5/bnr_date.xls")

browser.close()
