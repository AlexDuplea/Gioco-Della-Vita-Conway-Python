from random import *
import time
import os

verde = "\033[32m"
reset = "\033[0m"

#funzione che crea una lista bidimensionale
def get_check(altezza, lunghezza):
    return [[" " for i in range(lunghezza)] for j in range(altezza)]


#fa si che il che il cursore vada in alto allo schermo in modo tale da stampare nel terminale l'animazione
def move_cursor_top():
    print("\033[H", end="")
#pulisce il terminale
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#genera casualmente delle cellule vive
def genera_vita(lv, cord, numero_iniziale):
    random_cord = cord.copy()
    shuffle(random_cord)
    random_cord = random_cord[:numero_iniziale]
    for cr1 in random_cord:
        lv[cr1[0]][cr1[1]] = "■"
    return lv

#per ogni cellula vede conta quante cellule ha intorno (funzione presa dalla funzione numeri campo minato)
def conta_vita(xi, yi, lc, altezza, lunghezza):
    n_vita = 0
    cord_nuove = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    for x2, y2 in cord_nuove:
        nx = xi + x2
        ny = yi + y2
        if 0 <= nx < altezza and 0 <= ny < lunghezza:
            if lc[nx][ny] == "■":
                n_vita += 1
    return n_vita

#modifica le cellule secondo le regole di gioco
#è presente una seconda lista che viene aggiornata in modo tale che l'aggiornamento delle cellule non influenzi
#l'aggiornamento successivo
def calcolo_vita(l, x, y, n_vita, l2):
    if l[x][y] == "■":
        if n_vita < 2 or n_vita > 3:
            l2[x][y] = " "
        else:
            l2[x][y] = "■"
    elif l[x][y] == " ":
        if n_vita == 3:
            l2[x][y] = "■"
    return l2

#susseguirsi dell'ordine di gioco e gestione delle generazioni
def gioco(altezza, lunghezza, ng, nr):
    clear_screen()
    lim = get_check(altezza, lunghezza)
    cord = [(i, j) for i in range(altezza) for j in range(lunghezza)]

    lim = genera_vita(lim, cord, nr)

    for i in range(ng):
        move_cursor_top()
        l2 = get_check(altezza, lunghezza)


        for xi in range(altezza):
            for yi in range(lunghezza):
                n_vita = conta_vita(xi, yi, lim, altezza, lunghezza)
                l2 = calcolo_vita(lim, xi, yi, n_vita, l2)

        lim = l2

        for riga in lim:
            print(" ".join(riga))
        print()
        #sennò è troppo veloce e non si può capire granché
        time.sleep(0.08)





#funziona sul mio monitor da 32 pollici o sullo schermo del mio portatile da 16 pollici
def preset():
    x = input("ti trovi su monitor o pc?(M/P) ")
    if x.upper() == "M":
        h = 49
        l = 105
        numero_generazioni = 1000
        numero_iniziale = 2500
        gioco(h, l, numero_generazioni, numero_iniziale)
        print(""*3)
    elif x.upper() == "P":
        h = 39
        l = 78
        numero_generazioni = 100
        numero_iniziale = 600
        gioco(h, l, numero_generazioni, numero_iniziale)
        print(""*3)
    else:
        print("Errore nell'inserimento riprovare")

#utilizzare questa funzione per trovare la grandezza giusta
def grandezza_schermo():
    x = ""
    while x.upper() != "N":
        h1 = int(input("inserisci altezza: "))
        l1 = int(input("inserisci larghezza: "))

        check = [["□" for i in range(l1)] for j in range(h1)]
        clear_screen()
        for riga in check:
            print(" ".join(riga))
        x = input("continuare? S/N: ")

def converti_bitmap(lista):
    lista_bitmap = []
    for riga in lista:
        nuova_riga = []
        for elemento in riga:
            if elemento == " ":
                nuova_riga.append(0)
            elif elemento == "\u25a0":
                nuova_riga.append(1)
        lista_bitmap.append(nuova_riga)
    return lista_bitmap

def converti_per_terminale(lista):
    lista_terminale = []
    for riga in lista:
        nuova_riga = []
        for elemento in riga:
            if elemento == 0:
                nuova_riga.append(" ")
            elif elemento == 1:
                nuova_riga.append("\u25a0")
        lista_terminale.append(nuova_riga)
    return lista_terminale

def salva_griglia(dizionario,filename2):
    with open(filename2, "w") as file2:
        json.dump(dizionario, file2)

def fetch_iterazione(n_generazione,filename):
    with open(filename, "r") as file1:
        data = json.load(file1)

        l_imp = data[str(n_generazione)]

        return l_imp

def tester(altezza, lunghezza, ng_test, nr_test,numero_iterazioni):
    dictio = {}
    for iterazioni in range(numero_iterazioni):

        clear_screen()
        lim = get_check(altezza, lunghezza)
        cord = [(i, j) for i in range(altezza) for j in range(lunghezza)]

        lim = genera_vita(lim, cord, nr_test)

        dictio[iterazioni] = converti_bitmap(lim)

        for i in range(ng_test):
            move_cursor_top()
            l3 = get_check(altezza, lunghezza)

            for xi in range(altezza):
                for yi in range(lunghezza):
                    n_vita = conta_vita(xi, yi, lim, altezza, lunghezza)
                    l3 = calcolo_vita(lim, xi, yi, n_vita, l3)

            lim = l3

            for riga in lim:
                print(" ".join(riga))
            print()
            # sennò è troppo veloce e non si può capire granché
            #time.sleep(0.08)

    salva_griglia(dictio,"test.json")
    fetch_input = input("desideri salvare un iterazione? Se si, inserisci il numero della iterazione (ricorda che partono da 0)\n")
    fetch = fetch_iterazione(fetch_input,"test.json")
    outfile = open("test2.json", "r")
    dati = json.load(outfile)
    if len(dati) > 0:
        n = int(list(dati.keys())[-1])
        dati[n+1] = fetch
    elif len(dati) == 0:
        dati[0] = fetch
    else:
        print("Errore di lettura")
    salva_griglia(dati,"test2.json")
    outfile.close()











#preset()
#gioco(0,0,0,0)
#grandezza_schermo()
#tester(39,78,100,600,10)









