#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
input = raw_input("Enter names of the file:")
input_list = input.split(' ')
user_input= [(x.strip()) for x in input_list]
mynumbers=[]
filename=user_input[0]
with open(filename) as fz:
    for line in fz:
        mynumbers.append([ float(n) for n in line.strip().split(' ')])
t= int(mynumbers[0][0])
n= int(mynumbers[0][1])
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
flag=0.0
no_plus=0
neg_error_side=0
pos_error_side=0
c1=0
min=111
j1=0
sign='0'
main_sign=''
while i<t:
    j=0 
    while j<n-1:
        w=j+1
        
        m=0
        sign='o'
        c1=0
        neg_error_side=0
        pos_error_side=0
        while m<=j:
            if y[m]==1:
                neg_error_side=neg_error_side+p[m]
            else:
                pos_error_side=pos_error_side+p[m]
            m=m+1
           
        while w<n:
            if y[w]==1:
                pos_error_side=pos_error_side+p[w]
            else:
                neg_error_side=neg_error_side+p[w]
                 
            w=w+1
            
        if neg_error_side < pos_error_side:
            c1=neg_error_side
            sign='G'
        else:
            c1=pos_error_side
            sign='L'
        
        if c1<min:
            min=c1
            main_sign=sign
            j1=j
        j=j+1
    
    epsilon=float(min)
    min=111
    alpha=0.5*(math.log((1-epsilon)/epsilon,2.71828))
    q_rgt=math.exp(-alpha)
    q_wrng=math.exp(alpha)
    z=2*math.sqrt((1-epsilon)*epsilon)
    aa=0
    jj=0
    jj=j1+1
    h=''
    if main_sign=='L':
        f1=f1+str(alpha)+'I(x<'+ str((x[j1]+x[j1+1])/2) + ')+'
        print'The selected weak classiﬁer: h=I(x< %f )'%((x[j1]+x[j1+1])/2)
        while aa<=j1:
            
            f[aa]=f[aa]+alpha

            if y[aa]==-1:
                p[aa]=p[aa]*q_wrng/z
            else:
                p[aa]=p[aa]*q_rgt/z
            aa=aa+1
        while jj<n:

            f[jj]=f[jj]-alpha
            if y[jj]==1:
                p[jj]=p[jj]*q_wrng/z
            else:
                p[jj]=p[jj]*q_rgt/z
            jj=jj+1
    else:
        
        f1=f1+str(alpha)+'I(x>'+ str((x[j1]+x[j1+1])/2) + ')+'
        print 'The selected weak classiﬁer: h=I(x>%f )'%((x[j1]+x[j1+1])/2)
        while aa<=j1:
            f[aa]=f[aa]-alpha
            if y[aa]==1:
                p[aa]=p[aa]*q_wrng/z
            else:
                p[aa]=p[aa]*q_rgt/z
            aa=aa+1
        while jj<n:
            f[jj]=f[jj]+alpha
            if y[jj]==-1:
                p[jj]=p[jj]*q_wrng/z
            else:
                p[jj]=p[jj]*q_rgt/z
            jj=jj+1
    w=0
    e=0 
    while w<n :
         if (f[w]>0 and y[w]==-1.0) or ( f[w]<0 and y[w]==1.0):
             e=e+1
         w=w+1
    bound=bound*z     
    print 'The error of ht: epsilon= %f'%epsilon
    print 'The weight of ht: alpha(t)=%f'%alpha
    print 'The probabilities normalization factor: Zt=%f'%z
    print 'The probabilities after normalization'
    print p
    print 'The boosted classiﬁer: ft:%s'%f1
    print 'The error of the boosted classiﬁer: E=%f'%(float(e)/n)
    print 'The bound on Et=%f'%bound
    print '--------------------------------------------------'
    i=i+1
