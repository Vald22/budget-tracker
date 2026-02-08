import csv
import pandas as pd
from tabulate import tabulate
import os
import datetime
FILENAME='tracker.csv'


def create_db():
    if os.path.isfile('tracker.csv'):
        print('Exista baza de date')
    else:
        header=['Nume achizitie','Categorie','Data achizitiei','Pret']
        with open('tracker.csv','r+',newline='') as csvfile:
            writer=csv.writer(csvfile,delimiter=',')
            writer.writerow(i for i in header)

def adauga_in_baza():
    with open('tracker.csv','+a') as csvfile:
        new_line=[]
        nume_achititie=input('Ce ai cumparat ?')
        categorie=input('''Alege o categorie: 
                        1.Supermarket
                        2.Restaurant
                        3.Divertisment
                        4.Altele
                        5.Transport
                        6.Numerar''')
    


df = pd.read_table(FILENAME, delimiter=",")
print(tabulate(df,headers=df.head(),tablefmt='fancy_grid'))




