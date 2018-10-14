# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:41:21 2015

@author: ermiasbt
"""
# import bibliotekene
import pandas as pd
import matplotlib.pyplot as plt

# statistikk av fotoliste
ipad54 = pd.read_excel("ipad54_foto_03102017.xlsx", header = 0)     #lese excel filen
ipad54.head()                           # sjekk hvordan dataene ser ut

plt.style.use('ggplot')                 # bruk ggplot for bedre grafikk

fotograf_counts = pd.Series(ipad54['Fotograf']).value_counts()
fotograf_counts.plot('bar') # tegnes grafisk søylediagram (bar chart)
plt.show()

# Skrive ut til fil
fil_output = 'ipad54_foto.csv'      # spesifiser hvor det skal lagres filen
ipad54.to_csv(fil_output, sep=';', encoding='cp1252')      # lagre csv
