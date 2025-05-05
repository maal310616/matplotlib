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