import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from copy import copy


def boundaries(f):
    
    #### Locate maxima and minima ####
    u=[]
    u_i=[]
    l=[]
    l_i=[]

    u_i.append(0)
    l_i.append(0)
    u.append(f[0])
    l.append(f[0])

    for i in range(1,f.shape[0]-1):
        if (f[i-1]<f[i])and(f[i]>f[i+1]):
            u.append(f[i])
            u_i.append(i)
        if (f[i-1]>f[i])and(f[i]<f[i+1]):
            l.append(f[i])
            l_i.append(i)
        
    u_i.append(f.shape[0])
    l_i.append(f.shape[0])
    u.append(f[-1])
    l.append(f[-1])
    
    #### Upper Boundary ####
    rate_u=[]
    for i in range(len(u)-1):
        rate_u.append((u[i+1]-u[i])/(u_i[i+1]-u_i[i]))
    
    
    upper=[]
    temp=copy(f[0])
    c=-1
    for i in range(f.shape[0]):
        if i in u_i:
            upper.append(u[u_i.index(i)])
            temp=copy(u[u_i.index(i)])
            c+=1
            #print('f',i)
        else:
            #print('nf',i)
            upper.append(temp+rate_u[c])
            temp=copy(temp+rate_u[c])

    #### Lower Boundary ####
    
    rate_l=[]
    for i in range(len(l)-1):
        rate_l.append((l[i+1]-l[i])/(l_i[i+1]-l_i[i]))
    
    
    lower=[]
    temp=copy(f[0])
    c=-1
    for i in range(f.shape[0]):
        if i in l_i:
            lower.append(l[l_i.index(i)])
            temp=copy(l[l_i.index(i)])
            c+=1
            #print('f',i)
        else:
            #print('nf',i)
            lower.append(temp+rate_l[c])
            temp=copy(temp+rate_l[c])
    
    #### return bountaries ####
    
    return upper,lower



class EMD():
    
    def decompose(self,ts,n):
        self.ts = ts
        self.n = n
        
        self.c=[]
        #self.c.append(self.ts)
        r=copy(self.ts)
        for i in range(self.n):
            u,l=boundaries(r)
            u,l=np.array(u),np.array(l)
            m=(u+l)/2
            self.c.append(r-m)
            r=copy(m)
            
        self.c.append(r)
            
        return self.c 
            
        
        
        
    
        