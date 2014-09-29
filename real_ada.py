#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
input = raw_input("Enter names of the file:")
input_list = input.split(' ')
user_input= [(x.strip()) for x in input_list]
filename=user_input[0]
mynumbers=[]
with open(filename) as fz:
    for line in fz:
        mynumbers.append([ float(n) for n in line.strip().split(' ')])
t= int(mynumbers[0][0])
n= int(mynumbers[0][1])
epsilon=mynumbers[0][2]
x=mynumbers[1]
y=mynumbers[2]
p=mynumbers[3]
i=0
f1=''
f=[0]*n
bound=1
i=0
j=0
m=0
no_plus=0
min=1
j1=0
sign='0'
main_sign=''
min_G=10000
rp=0
rn=0
wp=0
wn=0
while i<t:
    j=0    
    while j<n:
        w=j+1
        m=0
        sign='o'
        G1=0
        G2=0
        p_r_plus=0
        p_w_neg=0
        p_w_plus=0
        p_r_neg=0
        while m<=j:
            if y[m]==1:
                p_r_plus=p_r_plus+p[m]
            else:
                p_w_neg=p_w_neg+p[m]
            m=m+1
           
        while w<n:
            if y[w]==1:
                p_w_plus=p_w_plus+p[w]
            else:
                p_r_neg=p_r_neg+p[w]
                 
            w=w+1
        G=math.sqrt(p_r_plus*p_w_neg)+math.sqrt(p_w_plus*p_r_neg)
        
        if G<min_G:
            rp=p_r_plus
            wn=p_w_neg
            wp=p_w_plus
            rn=p_r_neg
            min_G=G
            j1=j
        j=j+1
    
    cp=0.5*(math.log((rp+epsilon)/(wn+epsilon),2.71828))
    cn=0.5*(math.log((wp+epsilon)/(rn+epsilon),2.71828))
    z=2*min_G
    aa=0
    jj=j1+1
    h=''
    
    while aa<=j1:
            
            f[aa]=f[aa]+cp
            p[aa]=(p[aa]*(math.exp(-y[aa]*cp)))/z
            aa=aa+1
            
    while jj<n:

            f[jj]=f[jj]+cn
            p[jj]=(p[jj]*(math.exp(-y[jj]*cn)))/z
            jj=jj+1
    
    w=0
    e=0 
    while w<n :
         if ((f[w]>0) and (y[w]==-1.0)) or ( (f[w]<0) and (y[w]==1.0)) or f[w]==0.0:
             e=e+1
         w=w+1
    bound=bound*z
    print 'The selected weak classifier ht :%f'%((x[j1]+x[j1+1])/2)
    print 'The error of ht: epsilon= %f'%min_G
    print 'The weight of ht: c+=%f'%cp
    print 'The weight of ht: c-=%f'%cn
    print 'The probabilities normalization factor: Zt=%f'%z
    print 'The probabilities after normalization'
    print p
    print 'The values ft(xi) for each one of the examples:'
    print f
    print 'The error of the boosted classifier Et:%f'%(float(e)/n) 
    print 'bound:'
    print bound
    j1=0
    print '--------------------------------------------------'
    min_G=111
    
    i=i+1
