from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import winsound

page = urlopen('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEKTIaD_1VFRyQfkjXlJU-AiKWTyOvgPtQkaGwYQKZsdvl56er2UEfG-BjOSOqkd06IFHL-XyggUCA/pubhtml#')
soup = BeautifulSoup(page, 'html.parser')

total_studenti_trecuti = 0
pozitia_mea = 0

nota_mea = 357
ok = 0

for i in range(1000):
    new_ok = 0
    total_studenti_trecuti = 0
    pozitia_mea = 0
    for index,group in enumerate(soup.find('div', {'id' : 'sheets-viewport'}).find_all('div', recursive = False),1):
        #am intrat pe fiecare grupa
        if index<16:
            div_group = group.find('div').find('table').find('tbody')
            for index_tr,tr in enumerate(div_group.find_all('tr'),1):
                #iau fiecare rand din tabel
                nota = 0
                if index_tr>1:
                    #iau fiecare coloana din tabel
                    for index_td,td in enumerate(tr.find_all('td'),1):
                        if index_td == 1 and not td.text.strip():
                            break
                        if index_td == 22:
                            nota = td.text.strip()
                        if index_td == 23:
                            if td.text=='Promovat materie' or td.text=='Passed':
                                total_studenti_trecuti = total_studenti_trecuti + 1
                                if int(nota) < nota_mea:
                                    pozitia_mea = pozitia_mea + 1

    procentajul_meu = round(pozitia_mea/total_studenti_trecuti*100,2)

    print('Acum esti al ' + str(pozitia_mea) + 'lea din ' + str(total_studenti_trecuti) + ', cu un procentaj de ' + str(procentajul_meu) + '%.')

    if procentajul_meu < 5:
        print('Momentan am 10.')
        new_ok = 1
    elif procentajul_meu < 15:
        print('Nota 9 este foarte buna.')
        new_ok = 2
    elif procentajul_meu < 35:
        print('Bravo toto ai 8.')
        new_ok = 3
    elif procentajul_meu < 65:
        print('7 nu e cel mai bun lucru din lume.')
        new_ok = 4
    elif procentajul_meu < 90:
        print('In mediocritate cu 6.')
        new_ok = 5
    else:
        print('Abia ai trecut fratele meu.')
        new_ok = 6

    if ok<new_ok:
        winsound.PlaySound('D:/sadd.wav', winsound.SND_ALIAS)
    elif ok>new_ok:
        winsound.PlaySound('D:/shitt.wav', winsound.SND_ALIAS)
    ok = new_ok
    print()
    time.sleep(120)
