import time
import winsound
from bs4 import BeautifulSoup
from urllib.request import urlopen

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
nota = ''

for i in range(100):
    page = urlopen('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEKTIaD_1VFRyQfkjXlJU-AiKWTyOvgPtQkaGwYQKZsdvl56er2UEfG-BjOSOqkd06IFHL-XyggUCA/pubhtml#')
    soup = BeautifulSoup(page, 'html.parser')
    trs = soup.find('div', {'id' : '987831144'}).find('div').find('table').find('tbody').find_all('tr')
    for index,tr in enumerate(trs,1):
        if index == 26:
            tds = tr.find_all('td')
            for index2,td in enumerate(tds,1):
                if index2 == 21:
                    if td.text.strip():
                        print('Vezi ca s-a afisat nota!!!!!')
                        nota=td.text
                        winsound.Beep(frequency, duration)
                    else:
                        print('Inca nu s-a afisat nota.')

    print()
    time.sleep(25)
    if nota.strip():
        break

print('Nota dumneavoastra este:')

print('.............')

print('.............')

winsound.Beep(frequency, duration)
time.sleep(5)

print(nota)