import csv
import pandas as pd
from tabulate import tabulate
import os
import datetime

FILENAME='tracker.csv'
MONTH=f'{datetime.datetime.now().strftime('%B')}'
DIRECTORYYEAR=f'{datetime.datetime.now().strftime('%Y')}'
PARENT='DB'

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


def adauga_in_baza():
    with open(f'{DIRECTORYYEAR}/{MONTH}.csv','+a') as csvfile:
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

def printeaza_tabel():
    df = pd.read_table(FILENAME, delimiter=",")
    print(tabulate(df,headers=df.head(),tablefmt='fancy_grid'))


def meniu_aplicatie():
    while True:
        alegere=int(input('''Ce doresti sa faci ?
                        1.Creaza baza de date
                        2.Adauga in baza de date
                        3.Afiseaza baza de date sub forma de tabel
                        4.Inchide aplicatia
                        '''))
        match alegere:
            case 1:
                create_db()
            case 2:
                adauga_in_baza()
            case 3:
                printeaza_tabel()
            case 4:
                print('O zi placuta!')
                break
            case _:
                print('Introdu o actiune valida!')


def main():
    meniu_aplicatie()

if __name__ == '__main__':
    main()


