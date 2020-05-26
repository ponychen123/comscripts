#!/usr/bin/python
#usage:this sript transforme the xtb dumped scoord.* file ######
###    during md process to fin.vasp visulized by VESTA ########
###    JUST TYPE ./xtbmdcoord2vasp.py scoord.*          ########
###    author:ponychen                                  ########
###    time:20200526                                    ########

import sys

with open(sys.argv[1],'r') as f:
    s = f.readline()
    if s.strip() == '$coord':
        atoms = {}
        while True:
            s = list(f.readline().split())
            if s[0].strip() == '$periodic':
                dim = int(s[1])
                break
            if s[3].strip() in list(atoms.keys()):
                atoms[s[3].strip()].append(list(map(float,s[:3])))
            else:
                atoms[s[3].strip()]=[list(map(float,s[:3]))]
        if dim == 3:
            s = list(f.readline().split())
            if s[1].strip() == 'bohr':
                cell = []
                for i in range(3):
                    cell.append(list(map(float,f.readline().split())))
            else:
                sys.exit('Ooops, the unit of axis should be bohr!!!')
        else:
            cell = [[60,0,0],[0,60,0],[0,0,60]]
    else:
        sys.exit('Oooops, the coord file outputed by md should start with $coord!!!!'+s)

with open('fin.vasp','w') as ff:
    print('transformed by ponychen',file=ff)
    print('1',file=ff)
    for i in range(3):
        listtmp = list(map(lambda x:x*0.5292,cell[i]))
        print('{:<12.8f} {:<12.8f} {:<12.8f}'.format(listtmp[0],listtmp[1],listtmp[2]),file=ff)
    for ele in atoms.keys():
        print('{:<7}'.format(ele),file=ff,end=' ')
    print(file=ff)
    for ion in atoms.values():
        num = len(ion)
        print('{:<7d}'.format(num),file=ff,end=' ')
    print(file=ff)
    print('Cartesian',file=ff)
    for ion in atoms.values():
        for j in range(len(ion)):
            iontmp = list(map(lambda x:x*0.5292,ion[j]))
            print('{:<12.8f} {:<12.8f} {:<12.8f}'.format(iontmp[0],\
                    iontmp[1],iontmp[2]),file=ff)


