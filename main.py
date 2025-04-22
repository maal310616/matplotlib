import matplotlib.pyplot as plt
import datetime
import csv
import os


def get_mood_color(avg):
    if avg < 4:
        return 'red'
    elif avg <= 7:
        