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
    else:
        plt.show()


def saglaba_csv(dienas, garastavokli, fails="garastavokli.csv"):
    with open(fails, mode='w', newline='', encoding='utf-8') as f:
        rakstitajs = csv.writer(f)
        rakstitajs.writerow(["Diena", "Garastāvoklis"])
        for d, g in zip(dienas, garastavokli):
            rakstitajs.writerow([d, g])
    print(f"Dati saglabāti kā '{fails}'")


def nolasit_no_csv(fails="garastavokli.csv"):
    garastavokli = []
    try:
        with open(fails, mode='r', encoding='utf-8') as f:
            lasitajs = csv.DictReader(f)
            for rinda in lasitajs:
                garastavokli.append(int(rinda["Garastāvoklis"]))
        return garastavokli
    except FileNotFoundError:
        print("CSV fails netika atrasts.")
        return None



if __name__ == "__main__":
    dienas = ['Pirmdiena', 'Otrdiena', 'Trešdiena', 'Ceturtdiena', 'Piektdiena', 'Sestdiena', 'Svētdiena']

    print("Izvēlies darbību:")
    print("1 – Ievadīt garastāvokli manuāli")
    print("2 – Nolasīt no CSV faila")
    izvele = input("Tava izvēle (1/2): ")

    if izvele == '2':
        garastavokli = nolasit_no_csv()
        if garastavokli is None:
            exit()
    else:
        garastavokli = []
        print("\nIevadi savu garastāvokli (1–10) katrai nedēļas dienai:")
        for diena in dienas:
            while True:
                try:
                    vertiba = int(input(f"{diena}: "))
                    if 1 <= vertiba <= 10:
                        garastavokli.append(vertiba)
                        break
                    else:
                        print("Ievadi skaitli no 1 līdz 10.")
                except ValueError:
                    print("Lūdzu, ievadi derīgu skaitli.")

        saglabat_csv = input("Vai vēlies saglabāt datus CSV failā? (j/n): ").lower()
        if saglabat_csv == 'j':
            saglaba_csv(dienas, garastavokli)

    saglabat_attelu = input("Vai vēlies saglabāt grafiku kā attēlu? (j/n): ").lower()
    zime_grafiku(garastavokli, saglabat_attelu == 'j')