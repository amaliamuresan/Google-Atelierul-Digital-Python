import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
link = BeautifulSoup(r.text, 'html.parser')

title = link.find_all('div', attrs={'class': 'contentDiv'})

header = []
data_list = []
for i in title:
    for tr in i.find_all('table'):
        for td in tr.find_all('tr'):
            td_list = []
            # for th in td.find_all('th'):
            #     header.append(th.get_text())
            if td.find_all('th'):
                header = [th.get_text() for th in td.find_all('th')]
            for trd in td.find_all('td'):
                td_list.append(trd.get_text().lstrip('  '))
            data_list.append(td_list)
print(data_list)

df = pd.DataFrame(data_list, columns=header)
df.to_csv('week5/CursBNR.xls', header=header)