import requests
from bs4 import BeautifulSoup


r = requests.get("https://lpf.ro/liga-1")
s1 = BeautifulSoup(r.text, "html.parser")

f = open("week5/programariliga1.html", "w", encoding='utf-8')

rand = s1.table.find('tr')
f.write("<html><head>Clasament</head></body><table><thead><<tr style = 'color:red'>")

for tr in s1.table.select('tr')[:1]:
    for td in tr.select('td'):
        f.write(f"<th>{td.text}</th>")
f.write('</tr></thead></tbody>')


for tr in s1.table.select('tr')[1:]:
    f.write('<tr>')
    for td in tr.select('td'):
        f.write(f'<td style="background-color: grey; border-radius: 2px solid black> {td.text} </td>')
    f.write('</tr>')

f.write('</table></body></html>')

# print(rand)
