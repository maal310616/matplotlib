import matplotlib.pyplot as plt
import datetime
import csv
import os


def noteikt_krasu(vid):
    if vid < 4:
        return 'red'
    elif vid <= 7:
        return 'orange'
    else:
        return 'green'
    
def zime_grafiku(garastavokli, saglabat_attelu=False):
    dienas = ['Pirmdiena', 'Otrdiena', 'Trešdiena', 'Ceturtdiena', 'Piektdiena', 'Sestdiena', 'Svētdiena']
    videjais = sum(garastavokli) / len(garastavokli)
    krasa = noteikt_krasu(videjais)
    plt.figure(figsize=(10, 5))
    plt.plot(dienas, garastavokli, marker='o', linestyle='-', color=krasa)
    plt.title('Mans garastāvokļa grafiks')
    plt.xlabel('Nedēļas dienas')
    plt.ylabel('Garastāvoklis (1–10)')
    plt.ylim(1, 10)
    plt.grid(True)

    if saglabat_attelu:
        sodiena = datetime.date.today().isoformat()
        faila_nosaukums = f"garastavokla_grafiks_{sodiena}.png"
        plt.savefig(faila_nosaukums)
        print(f"Grafiks saglabāts kā '{faila_nosaukums}'")