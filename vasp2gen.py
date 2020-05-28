#!/usr/bin/env python
########################################################################
###usage:this script transform the POSCAR file into gen file used by####
###DFTB+.just type ./vasp2gen.py nameofposcar                       ####
###the generated gen file is named output.gen                       ####
### ponychen  20200528                                              ####
########################################################################

import sys

with open(sys.argv[1],'r') as f:
    poscar = f.readlines()

# read cell parameters
cell = []
for i in range(2,5):
    cell.append(list(map(float,poscar[i].split())))

# read element stmbol
atoms = {}
for i in poscar[5].split():
    atoms[i] = []

# read atom coordination
count = 7
atomcount = 0
elecount = 0

for i in atoms.keys():
    elecount += 1
    for j in list(map(int,poscar[6].split())):
        for k in range(j):
            atomcount += 1
            count += 1
            tmp = list(map(float,poscar[count].split()))
            tmp.insert(0,elecount)
            tmp.insert(0,atomcount)
            atoms[i].append(tmp)

# print to output.gen
with open('output.gen','w') as ff:
    print("    {:<8d} {}".format(sum(map(int,poscar[6].split())),"F"),\
            file=ff)
    for i in atoms.keys():
        print("    {:<8}".format(i),file=ff,end=' ')
    print(file=ff)
    for i in atoms.keys():
        for j in atoms[i]:
            print("    {:<4d} {:<4d} {:<12.8f} {:<12.8f} {:<12.8f}".format(\
                    j[0],j[1],j[2],j[3],j[4]),file=ff)
    print("    {:<12.8f} {:<12.8f} {:<12.8f}".format(0.0,0.0,0.0),file=ff)
    for i in range(3):
        print("    {:<12.8f} {:<12.8f} {:<12.8f}".format(cell[i][0],\
                cell[i][1],cell[i][2]),file=ff)
