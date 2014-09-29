#!/usr/bin/python
import math
input = raw_input("Enter names of the files dataset input-partition output-partition separated by single space: ")
input_list = input.split(' ')
user_input= [(x.strip()) for x in input_list]
def ENTROPY(p_zero,p_one):
             p_zero_deno=float(1)
             p_one_deno=float(1)
             
             if p_zero == 0:
                 p_zero_deno=1
             else:
                p_zero_deno=p_zero
                
             if p_one  == 0:
                p_one_deno=1
             else:
                p_one_deno=p_one
             p_part=p_zero*(math.log(1.0/p_zero_deno,2))+p_one*(math.log(1.0/p_one_deno,2))
             return p_part

filename = user_input[0]
filename1= user_input[1]
filename2= user_input[2]
mynumbers = []
mynumbers1= []
mynumbers2=[]
max_F=float(0)
max_F_part_selected_feature=1
selected_part=1

with open(filename) as f:
    for line in f:
        mynumbers.append([int(n) for n in line.strip().split(' ')])
for pair in mynumbers:
    try:
        no_features=mynumbers[0][1]-1
        no_dataentry=mynumbers[0][0]
    except IndexError:
        print "A line in the file doesn't have enough entries."
counter=1

with open(filename1) as f1:
    for line in f1:
        mynumbers1.append([ n for n in line.strip().split(' ')])
for pair in mynumbers1:
    try:
          F=0     
          j=len(pair)-1
          x=float(j)
          part_name=pair[0]
          i=1
          no_zero=0
          no_one=0
          temp=0
          while i <= j:
                  #print pair[i]   
                  temp=int(pair[i])
                  if mynumbers[temp][no_features]==0:
                      no_zero=float(no_zero+1)
                  else:
                      no_one=float(no_one+1)
                  i=i+1

          p_zero=float(no_zero/j)
          p_one=float(no_one/j)
          main_ent_eachpart=ENTROPY(p_zero,p_one)
          #print main_ent_eachpart
          q=0
          i=1
          gain=0
          check=0
          max_gain_feacture=1

          while q < no_features:
            iz=float(0)
            it=float(0)
            io=float(0)
            iztz=float(0)
            izto=float(0)
            iotz=float(0)
            ioto=float(0)
            ittz=float(0)
            itto=float(0)
            i=1

            while i <= j:
                  temp=int(pair[i])
                  if mynumbers[temp][q]==0:
                      iz=iz+1
                      if mynumbers[temp][no_features]==0:
                          iztz=iztz+1
                      else:
                          izto=izto+1
                  elif mynumbers[temp][q]==1:
                      io=io+1
                      if mynumbers[temp][no_features]==0:
                          iotz=iotz+1
                      else:
                          ioto=ioto+1
                  else:
                      it=it+1
                      if mynumbers[temp][no_features]==0:
                          ittz=ittz+1
                      else:
                          itto=itto+1
                  i=i+1;
                         
            if iz==0:
                 iz_deno=1
            else:
                 iz_deno=iz
            if io==0:
                 io_deno=1
            else:
                 io_deno=io
            if it==0:
                 it_deno=1
            else:
                 it_deno=it 
           
            etrophy_featurevise=iz/j*ENTROPY(iztz/iz_deno,izto/iz_deno)+io/j*ENTROPY(iotz/io_deno,ioto/io_deno)+it/j*ENTROPY(ittz/it_deno,itto/it_deno)
            #print "Entrpy and gain of %dth features"% (q+1)
            #print etrophy_featurevise
            gain1=main_ent_eachpart-etrophy_featurevise
            if gain1>gain:
                gain=gain1
                max_gain_feacture=q+1;
                check=i-1
            q=q+1

          F=gain*(x/no_dataentry)  
          #print "F:%f"%(F)
          #print max_gain_feacture
          if F>max_F:
              max_F=F;
              max_F_part_selected_feature=max_gain_feacture
              selected_part=counter
          counter=counter+1    
    except IndexError:
        print "A line in the file doesn't have enough entries."

#print max_F
#print max_F_part_selected_feature
#print selected_part
p=0
n=1
i=1
z1=[]
z2=[]
z3=[]
f=open(filename2,"a")
f1=open(filename1)
my=[]
j=1
s=''
for pair in mynumbers1:
            if n==selected_part:
                 t1=pair[0]
                 while i<=check:
                    temp=int(pair[i])
                    if mynumbers[temp][max_F_part_selected_feature-1]==0:
                           z1.append(temp)
                    elif mynumbers[temp][max_F_part_selected_feature-1]==1:
                          z2.append(temp)
                    else:
                          z3.append(temp)                        
                    i=i+1        

                 if z1:
                    s1=pair[0]+'%d '%j 
                    f.write(s1)
                    for x in z1:
                        f.write(str(x)+' ')
                    f.write('\n')
                    j=j+1
                    s+=s1
                 if z2:
                    s2=pair[0]+'%d '%j 
                    f.write(s2)
                    for x in z2:
                        f.write(str(x)+' ')
                    f.write('\n')
                    j=j+1
                    s+=s2
                 if z3:
                    s3=pair[0]+'%d '%j 
                    f.write(s3)
                    for x in z3:
                        f.write(str(x)+' ')
                    f.write('\n')
                    j=j+1
                    s+=s3 
            else:       
                    t=f1.readline()
                    f.write(t)                
            n=n+1
print 'Partition %s was replaced with partitions %s using Feature %d'%(t1,s,max_F_part_selected_feature)
 
f.close()
f1.close()
