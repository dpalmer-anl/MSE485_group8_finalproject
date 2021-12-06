# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:58:33 2021

@author: danpa
"""
import re
import numpy as np
import matplotlib.pyplot as plt

Ni85_log="/elastic_constant/Ni85-Co15/log_elastic.lammps"
Ni90_log="/elastic_constant/Ni90-Co10/log_elastic.lammps"
Ni95_log="/elastic_constant/Ni95-Co5/log_elastic.lammps"
Ni100_log="/elastic_constant/Ni100-Co0/log_elastic.lammps"

def get_mod_val(filename,string):
    with open(filename, "r") as f:
        lines=f.readlines()
        noskip=0
        for l in lines:
            if string in l:
                if noskip>0:
                    return float(re.findall(r'[-+]?[.]?[:\.\d]+',l)[0])
                noskip+=1
                
files=[Ni85_log,Ni90_log,Ni95_log,Ni100_log]
vall=np.zeros(len(files))
concentration=[0.85,0.9,0.95,1.]
string= "Poisson Ratio" #"Bulk Modulus"
for j,i in enumerate(files):
   vall[j]=(get_mod_val(i,string))

plt.plot(concentration,vall)
plt.xlabel("Ni concentration")
plt.ylabel("Poisson Ratio (GPa)")
plt.title("Poisson Ratio at various Ni-Co concentrations")
plt.show()