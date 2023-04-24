import matplotlib.pyplot as plt
import numpy as np
import scienceplots


plt.style.use(['science','ieee'])

resolution=[]
InFlow_o1=[]
InFlow_o2=[]
InFlow_exact=[]


f=open('/Users/ueda/Result/Re=500/InletFlow.dat','rt')


for line in f:
    data=line[:-1].split(' ')

    resolution.append(float(data[0]))
    InFlow_o2.append(float(data[1]))
    InFlow_o1.append(float(data[2]))
    InFlow_exact.append(float(data[3]))

plt.plot(resolution, InFlow_exact, lw=0.7, label = "Exact")
plt.plot(resolution, InFlow_o1, lw=0.7, label = "$O_{1}$")
plt.plot(resolution, InFlow_o2, lw=0.7, label = "$O_{2}$")

#plt.rcParams['font.family'] = 'Times New Roman'

plt.legend(loc='upper right')
#plt.title('8x8',fontsize=18)
plt.ylim(0.5, 1)

plt.xticks([0, 1, 2],['8x16', '4x8', '2x4'])
plt.tick_params(labelsize=8)

'''横軸と縦軸のラベル付け'''
plt.xlabel('Resolution[-]',fontsize=8)
plt.ylabel('Inflow rate[-]',fontsize=8)

#plt.legend(loc='lower right',prop={"size": 32})
plt.legend(loc='lower right')

'''グリッド線を引く'''
plt.grid(True)

'''表示'''
plt.show()