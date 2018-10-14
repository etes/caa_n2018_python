# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:35:35 2018

@author: jankhe
"""

import os

fp = os.getcwd()
isd_fil = os.path.join(fp, 'isd_filer', 'B3_22062016.isd')
isd_oppdatert = os.path.splitext(isd_fil)[0] + '_oppdatert.isd'

read = open(isd_fil)
writ = open(isd_oppdatert,'w')

cons = -0.020

for linje in read:
    if str(linje).startswith('39='):
        l = str(linje)[3:]
        l.strip('\n')
        f = float(l)
        f = f + cons
        writ.write('39='+str(f)+'\n')
    else:
        writ.write(str(linje))
        
writ.close()




def oppdater_hoyde(isd_fil, isd_oppdatert , hoyde_feil):
    cons = hoyde_feil # høyden som skal legges til
    read = open(isd_fil)
    writ = open(isd_oppdatert, 'w')
    for linje in read:
        if str(linje).startswith('39='):
            l = str(linje)[3:]
            l.strip('\n')
            f = float(l)
            f = f + cons
            writ.write('39=' + str(f) + '\n')
        else:
            writ.write(str(linje))
    writ.close()


"""
fp = os.path.dirname(__file__)
isd_mappe = os.path.join(fp, 'isd_filer')
isd_filer = [os.path.join(isd_mappe, file) for file in os.listdir(isd_mappe)]

for isd_fil in isd_filer:
    if isd_fil.endswith(".isd"):
        isd_oppdatert = os.path.splitext(isd_fil)[0] + '_oppdatert.isd'
        oppdater_hoyde(isd_fil, isd_oppdatert, -0.020)
"""