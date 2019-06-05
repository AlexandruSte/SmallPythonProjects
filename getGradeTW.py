from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import winsound

elevi_trecuti = 0
note = []


def start_operation():
    global elevi_trecuti
    global note
    page = urlopen(
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vR37jb_Pt7X6z2NAq2ccjSn7r4GtwGnK_G82D5vSFS6QXeiGwQGo84B5G37VhQa9KOACXGeGI41i-Pd/pubhtml#')
    soup = BeautifulSoup(page, 'html.parser')
    for index, div in enumerate(soup.find('div', {'id': 'sheets-viewport'}).find_all('div', recursive=False), 1):
        # iau doar anul 2 si grupele de engleza
        if index < 3:
            tbody = div.find('div').find('table').find('tbody')
            for index_tr, tr in enumerate(tbody.find_all('tr'), 1):
                # sar peste primele 2 linii goale
                t = e = p = a = s = 0.0
                calculeaza_nota = True
                if index_tr > 2:
                    for index_td, td in enumerate(tr.find_all('td'), 1):
                        if 4 <= index_td <= 6 and td.text.strip():
                            t = t + float(td.text)
                        if index_td == 10:
                            if float(td.text.strip()) <= 5:
                                calculeaza_nota = False
                                break
                            else:
                                e = float(td.text.strip())
                        if index_td == 11:
                            if td.text.strip():
                                if float(td.text.strip()) >= 5:
                                    p = float(td.text.strip())
                                else:
                                    calculeaza_nota = False
                                    break
                            else:
                                break
                        if index_td == 12:
                            if td.text.strip():
                                if float(td.text.strip()) >= 5:
                                    a = float(td.text.strip())
                                else:
                                    calculeaza_nota = False
                                    break
                            else:
                                calculeaza_nota = False
                                break
                        if index_td == 13:
                            if td.text.strip():
                                if float(td.text.strip()) >= 5:
                                    s = float(td.text.strip())
                                else:
                                    calculeaza_nota = False
                                    break
                            else:
                                calculeaza_nota = False
                                break

                    if calculeaza_nota:
                        nota_elev = getGrade(t, e, p, a, s)
                        note.append(nota_elev)
                        elevi_trecuti = elevi_trecuti + 1


def getGrade(t, e, p, a, s):
    grade = t * 0.2 + e * 0.1 + p * 0.1 + a * 0.2 + s * 0.5
    return grade


def main():
    global note
    global elevi_trecuti
    start_operation()
    for nota in note:
        print(nota)
    print('In total sunt ' + str(elevi_trecuti) + ' studenti care au trecut.')


if __name__ == "__main__":
    main()
