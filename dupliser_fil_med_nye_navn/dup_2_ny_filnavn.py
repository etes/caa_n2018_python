# -*- coding: utf-8 -*-
"""
Created on Fri Mar 02 13:24:16 2018

@author: jankhe
"""

import os
import shutil

fp = os.path.dirname(__file__)

copy_fil = os.path.join(fp,'filemakerfil.fmp12') # masterfil Filemaker

x= [20]
x=x + range(47,65)

ipad = ['ipad'+str(val)+'_skjema.fmp12' for val in x] #liste med nye filnavn
for name in ipad:
    ny_path = os.path.join(fp,name)
    shutil.copy2(copy_fil,ny_path)
