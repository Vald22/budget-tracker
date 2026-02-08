import csv
import pandas as pd
from tabulate import tabulate
import os
import datetime

MONTH=f'{datetime.datetime.now().strftime('%b')}'
DIRECTORYYEAR=f'{datetime.datetime.now().strftime('%Y')}'
PARENT='DB'
FILENAME=f'{PARENT}/{DIRECTORYYEAR}/{MONTH}.csv'

def creazafoldermama():
    try:
        os.mkdir(PARENT)
        print(f"Directory '{PARENT}' created successfully.")
    except FileExistsError:
        print(f"Directory '{PARENT}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{PARENT}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def creaza_directoare():
    try:
        os.mkdir(f'{PARENT}/{DIRECTORYYEAR}')
        print(f"Directory '{DIRECTORYYEAR}' created successfully.")
    except FileExistsError:
        print(f"Directory '{DIRECTORYYEAR}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{DIRECTORYYEAR}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



def create_db():
    if not os.path.isdir(f'{PARENT}'):
        creazafoldermama()
    if not os.path.isdir(f'{PARENT}/{DIRECTORYYEAR}'):
        creaza_directoare()    
    if os.path.isfile(f'{PARENT}/{DIRECTORYYEAR}/{MONTH}.csv'):
        print('Exista baza de date')
    else:
        header=['Nume achizitie','Categorie','Data achizitiei','Pret']
        with open(f'{PARENT}/{DIRECTORYYEAR}/{MONTH}.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile,delimiter=',')
            writer.writerow(i for i in header)

def alege_ce_vrei_sa_vezi():
    print(os.listdir(f'{PARENT}'))
    try:
        anul=int(input('Alege anul pe care vrei sa il vezi '))
        print(os.listdir(f'{PARENT}/{anul}'))
    except FileNotFoundError:
        print('Alege un an valid!')
        return
    try: 
        luna=input('Alege luna pe care vrei sa o vezi ')
        printeaza_tabel(f'{PARENT}/{anul}/{luna.capitalize()}.csv')
    except FileNotFoundError:
        print('Alege o luna valida!')
        return


def adauga_in_baza():
    with open(f'{PARENT}/{DIRECTORYYEAR}/{MONTH}.csv','+a') as csvfile:
        new_line=[]
        nume_achititie=input('Ce ai cumparat ?')
        categorie=input('''Alege o categorie: 
                        1.Supermarket
                        2.Restaurant
                        3.Divertisment
                        4.Altele
                        5.Transport
                        6.Numerar
                        ''')
        data_achizitiei=datetime.datetime.now()
        pret=int(input("cat costa?: "))
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerow([nume_achititie,categorie,data_achizitiei,pret])

def printeaza_tabel(fisier=FILENAME):
    df = pd.read_table(fisier, delimiter=",")
    print(tabulate(df,headers=df.head(),tablefmt='fancy_grid'))


def meniu_aplicatie():
    while True:
        alegere=int(input('''Ce doresti sa faci ?
                        1.Creaza baza de date
                        2.Adauga in baza de date
                        3.Afiseaza luna curenta
                        4.Alege o luna dintr-un an 
                        5.Inchide aplicatia
                        '''))
        match alegere:
            case 1:
                create_db()
            case 2:
                adauga_in_baza()
            case 3:
                printeaza_tabel()
            case 4:
                alege_ce_vrei_sa_vezi()
            case 5:
                print('O zi placuta!')
                break
            case _:
                print('Introdu o actiune valida!')


def main():
    meniu_aplicatie()

if __name__ == '__main__':
    main()


