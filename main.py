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