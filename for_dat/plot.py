import matplotlib.pyplot as plt
import scienceplots
import numpy as np

plt.style.use(['science','nature'])
iterate1=[]
costFunction1=[]
costFunction2=[]
costFunction3=[]
costFunction4=[]
costFunction5=[]
costFunction6=[]

f_P_16x16=open('/Users/ueda/code/研究室/NSFluid/example/optimalControl/results_Re=200_loop=1000_alpha=0.23973885_Alpha=2e0_Data16x16/costFunction.dat', 'rt')
f_16x16=open('/Users/ueda/code/研究室/OptimalControl_NS_QUAD/example/optimalControl/results_Re=200_loop=2000_alpha=0.23973885_Alpha=1e2_Data16x16/costFunction.dat', 'rt')


f_P_8x8=open('/Users/ueda/code/研究室/NSFluid/example/optimalControl/results_Re=200_loop=1000_alpha=1e0_Alpha=2e0_Data8x8/costFunction.dat', 'rt')
f_8x8=open('/Users/ueda/code/研究室/OptimalControl_NS_QUAD/example/optimalControl/results_Re=200_loop=2000_alpha=1e0_Alpha=3e1_Data8x8/costFunction.dat', 'rt')


f_P_4x4=open('/Users/ueda/code/研究室/NSFluid/example/optimalControl/results_Re=200_loop=1000_alpha=4.70683635_Alpha=2e0_Data4x4/costFunction.dat', 'rt')
f_4x4=open('/Users/ueda/code/研究室/OptimalControl_NS_QUAD/example/optimalControl/results_Re=200_loop=2000_alpha=4.70683635_Alpha=6e0_Data4x4/costFunction.dat', 'rt')

for line in f_16x16:
    data=line[:-1].split(' ')

    iterate1.append(int(data[0]))
    costFunction1.append(float(data[4]))





for line in f_P_16x16:
    data=line[:-1].split(' ')

    costFunction2.append(float(data[4]))


plt.plot(iterate1, costFunction2,lw=3,label = "$O_{1}$")
plt.plot(iterate1, costFunction1, lw=3,label = "$O_{2}$")



for line in f_8x8:
    data=line[:-1].split(' ')

    costFunction3.append(float(data[4]))








for line in f_P_8x8:
   data=line[:-1].split(' ')

   costFunction4.append(float(data[4]))


#plt.plot(iterate1, costFunction4, lw=3, label ="$O_{1}$")
#plt.plot(iterate1, costFunction3, lw=3, label ="$O_{2}$")


for line in f_4x4:
    data=line[:-1].split(' ')

    costFunction5.append(float(data[4]))





for line in f_P_4x4:
    data=line[:-1].split(' ')

    costFunction6.append(float(data[4]))


#plt.plot(iterate1, costFunction6, lw=3, label ="$O_{1}$")
#plt.plot(iterate1, costFunction5, lw=3, label ="$O_{2}$")





plt.legend(loc='upper right',prop={"size": 30})

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.set_xlim(0,2000)

ax.set_yscale('log')

'''横軸と縦軸のラベル付け'''
plt.xlabel('Iteration[-]',fontsize=30)
plt.ylabel('Cost function[-]',fontsize=30)
plt.tick_params(labelsize=30)

'''グリッド線を引く'''
plt.grid(True)

'''表示'''
plt.show()