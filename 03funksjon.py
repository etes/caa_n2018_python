# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        03funksjon.py
# Purpose:
#
# Author:      ermiasbt
#
# Created:     14.10.2018
# Copyright:   (c) ermiasbt 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def printer ():
    """Skrives ut 'Hello CAA-Norge 2018!'"""
    print ("Hello CAA-Norge 2018!")      # skriver funksjon

# kaller 'printer' funksjonen opprettet ovenfor
printer ()

def print_sum (x, y):
    """Skrives ut summen av to argumenter x og y"""
    sum = x + y     # beregner summen
    print (sum)      # skrive ut resultatet

print_sum (5, 6)