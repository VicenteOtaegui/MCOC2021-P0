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

dts_8 = []

dts_9 = []



fid = open(f"rendimiento_P04_eigh32_caso_I.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_1.append(dt)

fid.close()

fid = open(f"rendimiento_P04_eigh32_caso_II_overwrite_False.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_2.append(dt)

fid.close()

fid = open(f"rendimiento_P04_eigh32_caso_II_overwrite_True.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_3.append(dt)

fid.close()

fid = open(f"rendimiento_P04_eigh32_caso_III_overwrite_False.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_4.append(dt)

fid.close()

fid = open(f"rendimiento_P04_eigh32_caso_III_overwrite_True.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_5.append(dt)

fid.close()

fid = open(f"rendimiento_P04_eigh32_caso_IV_overwrite_False.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_6.append(dt)

fid.close()


fid = open(f"rendimiento_P04_eigh32_caso_IV_overwrite_True.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_7.append(dt)

fid.close()


fid = open(f"rendimiento_P04_eigh32_caso_V_overwrite_False.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_8.append(dt)

fid.close()


fid = open(f"rendimiento_P04_eigh32_caso_V_overwrite_True.txt","r")

for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])

	Ns_1.append(N)
	dts_9.append(dt)

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
DTS8=[]
DTS9=[]

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

for i in range(int(len(dts_8)/10)):
	V8 = np.mean([dts_8[i+T*0],dts_8[i+T*1],dts_8[i+T*2],dts_8[i+T*3],dts_8[i+T*4],dts_8[i+T*5],dts_8[i+T*6],dts_8[i+T*7],dts_8[i+T*8],dts_8[i+T*9]])
	DTS8.append(V8)

for i in range(int(len(dts_9)/10)):
	V9 = np.mean([dts_9[i+T*0],dts_9[i+T*1],dts_9[i+T*2],dts_9[i+T*3],dts_9[i+T*4],dts_9[i+T*5],dts_9[i+T*6],dts_9[i+T*7],dts_9[i+T*8],dts_9[i+T*9]])
	DTS9.append(V9)

## xticks ##
labels_x = ["10","20","50","100","200","500", "1000","2000","4000","10000","20000"]
Ns1 = [10,20,50,100,200,500,1000,2000,4000,10000,20000]

## yticks tiempo transcurrido ##
labels_y1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dts1 = [10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**(0), 10, 60, 600]

plt.figure(1)


plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento Eigh dtype = float32")
plt.xticks(Ns1, labels_x, rotation = 45)
alfa = 0.8
plt.loglog(NS1,DTS1,marker=".", color="r", alpha=alfa, label="Caso I: eigh (default)")
plt.loglog(NS1,DTS2,marker="*", color="g", alpha=alfa, label="Caso II: eigh (driver='ev', overwrite_a=False)")
plt.loglog(NS1,DTS3,marker="_", color="m", alpha=alfa, label="Caso II: eigh (driver='ev', overwrite_a=True)")
plt.loglog(NS1,DTS4,marker="2", color="k", alpha=alfa, label="Caso III: eigh (driver='evd', overwrite_a=False)")
plt.loglog(NS1,DTS5,marker=",", color="c", alpha=alfa, label="Caso III: eigh (driver='evd', overwrite_a=True)")
plt.loglog(NS1,DTS6,marker="p", color="pink", alpha=alfa, label="Caso IV: eigh (driver='evr', overwrite_a=False)")
plt.loglog(NS1,DTS7,marker="4", color="brown", alpha=alfa, label="Caso IV: eigh (driver='evr', overwrite_a=True)")
plt.loglog(NS1,DTS8,marker="*", color="b", alpha=alfa, label="Caso V: eigh (driver='evx', overwrite_a=False)")
plt.loglog(NS1,DTS9,marker=".", color="y", alpha=alfa, label="Caso V: eigh (driver='evx', overwrite_a=True)")


plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)
plt.xticks(visible=True)

plt.tight_layout()
plt.legend()
plt.savefig("plot_caso_Eigh_32.png")

plt.show()