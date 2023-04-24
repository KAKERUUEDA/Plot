import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','ieee'])
input_csv = pd.read_csv('/Users/ueda/code/NSFluid/example/optimalControl/results_Re=200_loop=1000_alpha=1e0_Alpha=2e0_Data8x8/v_at_y=0.625.csv')
pointID = input_csv[input_csv.keys()[0]]
x_coordinate = input_csv[input_csv.keys()[1]]
y_coordinate = input_csv[input_csv.keys()[2]]
z_coordinate = input_csv[input_csv.keys()[3]]
Points_Magnitude = input_csv[input_csv.keys()[4]]
arc_length = input_csv[input_csv.keys()[5]]
u = input_csv[input_csv.keys()[6]]
v = input_csv[input_csv.keys()[7]]
w = input_csv[input_csv.keys()[8]]
velocity_Magunitude = input_csv[input_csv.keys()[9]]

input_csv2 = pd.read_csv('/Users/ueda/code/OptimalControl_NS_QUAD/example/optimalControl/results_Re=200_loop=2000_alpha=1e0_Alpha=3e1_Data8x8/v_at_y=0.625.csv')
pointID2 = input_csv2[input_csv2.keys()[0]]
x_coordinate2 = input_csv2[input_csv2.keys()[1]]
y_coordinate2 = input_csv2[input_csv2.keys()[2]]
z_coordinate2 = input_csv2[input_csv2.keys()[3]]
Points_Magnitude2 = input_csv2[input_csv2.keys()[4]]
arc_length2 = input_csv2[input_csv2.keys()[5]]
u2 = input_csv2[input_csv2.keys()[6]]
v2 = input_csv2[input_csv2.keys()[7]]
w2 = input_csv2[input_csv2.keys()[8]]
velocity_Magunitude2 = input_csv2[input_csv2.keys()[9]]

input_csv3 = pd.read_csv('/Users/ueda/code/NSFluid/example/NavierStokes/results256x256_Re=200_loop=300/v_at_y=5.25.csv')

pointID3 = input_csv3[input_csv3.keys()[0]]
x_coordinate3 = input_csv3[input_csv3.keys()[1]]
y_coordinate3 = input_csv3[input_csv3.keys()[2]]
z_coordinate3 = input_csv3[input_csv3.keys()[3]]
Points_Magnitude3 = input_csv3[input_csv3.keys()[4]]
arc_length3 = input_csv3[input_csv3.keys()[5]]
u3 = input_csv3[input_csv3.keys()[8]]
v3 = input_csv3[input_csv3.keys()[9]]
w3 = input_csv3[input_csv3.keys()[10]]

input_csv4 = pd.read_csv('/Users/ueda/Result/Re=200/v_at_y=0.625_8x8_MRI.csv')

x_coordinate4 = input_csv4[input_csv4.keys()[5]]
u4 = input_csv4[input_csv4.keys()[10]]
v4 = input_csv4[input_csv4.keys()[11]]
w4 = input_csv4[input_csv4.keys()[12]]


plt.tick_params(labelsize=7)
plt.ylabel('v at(x,0.5)[-]',fontsize=7)
plt.xlabel('x[-]',fontsize=7)
#plt.title('4x4',fontsize=18)
#
#plt.plot(x_coordinate, v3, '-', color='r', lw=3, label = "Exact")
#plt.plot(x_coordinate, v, '--', color='b', lw=3, label = "$O_{1}$")
#plt.plot(x_coordinate2, v2,linestyle = "dashdot", color='g', lw=3, label = "$O_{2}$")
#plt.figure()
plt.plot(x_coordinate, v3,lw=0.7,label = "Exact")
plt.plot(x_coordinate4, v4,lw=0.7,label = "Measurement")
plt.plot(x_coordinate, v,lw=0.7,label = " Proposed method")
plt.plot(x_coordinate2, v2,lw=0.7,label = "Previous method")

plt.legend(loc='upper right', fontsize=5)

plt.show()

