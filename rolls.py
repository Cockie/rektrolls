# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:28:22 2016

@author: yorick
"""
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
a=[0,1/6,1/6,2/6,3/6,4/6,5/6,6/6]
b=["-2","-1","+0","+1","+2","+3","+4","+5"]
fi = open('res', 'w')
fi.write('[[table style="align:left"]] [[row]] [[cell]]'+'\n')
fi.write("|| Mod\Attempts || 1 || 2 || 3 || 4 || 5 ||"+'\n')
#thing=
for n in range(0,8):
    temp="|| "+b[n]+" || "
    for i in range(1,6):
        for j in range(1,i+1):
            print(nCr(i,j))
            temp+=str(round(100*nCr(i,j)* ((a[n])**(i*j)) * (1-(a[n])**i)**(i-j) ,2))+" % chance of "+str(j)
            if j==1:
                temp+=" success"+" _"+'\n'
            else:
                temp+=" successes"+" _"+'\n'
        temp+=str(round(100*(1-(1-(a[n])**i)**i) ,2))+" % chance of at least 1 succes"
        temp+=" || "
    temp+='\n'
    fi.write(temp)
    temp=""
fi.write('[[/cell]][[/row]][[/table]]'+'\n')
fi.close()
