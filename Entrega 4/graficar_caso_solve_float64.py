import matplotlib.pylab as plt
from psutil import virtual_memory
import numpy as np


Ns_1  = []

dts_1 = []

dts_2 = []

dts_3 = []

dts_4 = []

dts_5 = []

dts_6 = []

dts_7 = []


fid = open(f"rendimiento_P04_solve64_caso_I.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_1.append(dt)

fid.close()

fid = open(f"rendimiento_P04_solve64_caso_II.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_2.append(dt)

fid.close()

fid = open(f"rendimiento_P04_solve64_caso_III.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_3.append(dt)

fid.close()

fid = open(f"rendimiento_P04_solve64_caso_IV.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_4.append(dt)

fid.close()

fid = open(f"rendimiento_P04_solve64_caso_V.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_5.append(dt)

fid.close()

fid = open(f"rendimiento_P04_solve64_caso_VI.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_6.append(dt)

fid.close()


fid = open(f"rendimiento_P04_solve64_caso_VII.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_7.append(dt)

fid.close()


i=3
T=36
NS1 = Ns_1[0:36]
DTS1=[]
DTS2=[]
DTS3=[]
DTS4=[]
DTS5=[]
DTS6=[]
DTS7=[]

for i in range(int(len(dts_1)/10)):
	V1 = np.mean([dts_1[i+T*0],dts_1[i+T*1],dts_1[i+T*2],dts_1[i+T*3],dts_1[i+T*4],dts_1[i+T*5],dts_1[i+T*6],dts_1[i+T*7],dts_1[i+T*8],dts_1[i+T*9]])
	DTS1.append(V1)

for i in range(int(len(dts_2)/10)):
	V2 = np.mean([dts_2[i+T*0],dts_2[i+T*1],dts_2[i+T*2],dts_2[i+T*3],dts_2[i+T*4],dts_2[i+T*5],dts_2[i+T*6],dts_2[i+T*7],dts_2[i+T*8],dts_2[i+T*9]])
	DTS2.append(V2)

for i in range(int(len(dts_3)/10)):
	V3 = np.mean([dts_3[i+T*0],dts_3[i+T*1],dts_3[i+T*2],dts_3[i+T*3],dts_3[i+T*4],dts_3[i+T*5],dts_3[i+T*6],dts_3[i+T*7],dts_3[i+T*8],dts_3[i+T*9]])
	DTS3.append(V3)

for i in range(int(len(dts_4)/10)):
	V4 = np.mean([dts_4[i+T*0],dts_4[i+T*1],dts_4[i+T*2],dts_4[i+T*3],dts_4[i+T*4],dts_4[i+T*5],dts_4[i+T*6],dts_4[i+T*7],dts_4[i+T*8],dts_4[i+T*9]])
	DTS4.append(V4)

for i in range(int(len(dts_5)/10)):
	V5 = np.mean([dts_5[i+T*0],dts_5[i+T*1],dts_5[i+T*2],dts_5[i+T*3],dts_5[i+T*4],dts_5[i+T*5],dts_5[i+T*6],dts_5[i+T*7],dts_5[i+T*8],dts_5[i+T*9]])
	DTS5.append(V5)

for i in range(int(len(dts_6)/10)):
	V6 = np.mean([dts_6[i+T*0],dts_6[i+T*1],dts_6[i+T*2],dts_6[i+T*3],dts_6[i+T*4],dts_6[i+T*5],dts_6[i+T*6],dts_6[i+T*7],dts_6[i+T*8],dts_6[i+T*9]])
	DTS6.append(V6)

for i in range(int(len(dts_7)/10)):
	V7 = np.mean([dts_7[i+T*0],dts_7[i+T*1],dts_7[i+T*2],dts_7[i+T*3],dts_7[i+T*4],dts_7[i+T*5],dts_7[i+T*6],dts_7[i+T*7],dts_7[i+T*8],dts_7[i+T*9]])
	DTS7.append(V7)


## xticks ##
labels_x = ["10","20","50","100","200","500", "1000","2000","5000","10000","20000"]
Ns1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

## yticks tiempo transcurrido ##
labels_y1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dts1 = [10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**(0), 10, 60, 600]

plt.figure(1)


plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento Solve dtype = float64")
plt.xticks(Ns1, labels_x, rotation = 45)

plt.loglog(NS1,DTS1,marker=".", color="r", alpha=0.8, label="Caso 1: x = inv(A)*b")
plt.loglog(NS1,DTS2,marker=".", color="g", alpha=0.8, label="Caso 2: solve (default)")
plt.loglog(NS1,DTS3,marker=".", color="m", alpha=0.8, label="Caso 3: solve (assume_a=pos)")
plt.loglog(NS1,DTS4,marker=".", color="k", alpha=0.8, label="Caso 4: solve (assume_a=sym)")
plt.loglog(NS1,DTS5,marker=".", color="c", alpha=0.8, label="Caso 5: solve (overwrite_a=True)")
plt.loglog(NS1,DTS6,marker=".", color="b", alpha=0.8, label="Caso 6: solve (overwrite_b=True)")
plt.loglog(NS1,DTS7,marker=".", color="y", alpha=0.8, label="Caso 7: solve (overwrite_a=True, overwrite_b=True)")



plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)
plt.xticks(visible=True)


plt.tight_layout()
plt.legend()
plt.savefig("plot_caso_Solve_64.png")

plt.show()