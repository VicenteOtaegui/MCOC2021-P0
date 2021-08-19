import matplotlib.pylab as plt
from psutil import virtual_memory

# CASOS NUMPY
# 	rendimiento_P03_1.txt
# 	rendimiento_P03_2.txt
# 	rendimiento_P03_3.txt
# 	rendimiento_P03_4.txt
# CASOS SCIPY OVERWRITE = FALSE
# 	rendimiento_P03_5.txt
# 	rendimiento_P03_6.txt
# 	rendimiento_P03_7.txt
# 	rendimiento_P03_8.txt
# CASOS SCIPY OVERWRITE = TRUE
# 	rendimiento_P03_9.txt
# 	rendimiento_P03_10.txt
# 	rendimiento_P03_11.txt
# 	rendimiento_P03_12.txt

# print (virtual_memory().total/(10**9))

Ns_1 = []
dts_1 = []
mems_1 = []

Ns_2 = []
dts_2 = []
mems_2 = []

Ns_3 = []
dts_3 = []
mems_3 = []

i=2
ii=6
iii=10

fid = open(f"rendimiento_P03_{i}.txt","r")
L=0
for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])
	mem = int(sl[9])
	L += 1

	Ns_1.append(N)
	dts_1.append(dt)
	mems_1.append(mem)

	#print (sl)

fid.close()


fid = open(f"rendimiento_P03_{ii}.txt","r")
LL=0
for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])
	mem = int(sl[9])
	LL+=1
	Ns_2.append(N)
	dts_2.append(dt)
	mems_2.append(mem)

	#print (sl)

fid.close()

fid = open(f"rendimiento_P03_{iii}.txt","r")
LLL=0
for line in fid:
	sl = line.split()
	N = int(sl[2])
	dt = float(sl[5])
	mem = int(sl[9])
	LLL+=1
	Ns_3.append(N)
	dts_3.append(dt)
	mems_3.append(mem)

	#print (sl)

fid.close()

# print (Ns)
# print (dts)
# print (mems)

L=int(L/10)
LL=int(LL/10)
LLL=int(LLL/10)


## xticks ##
labels_x = ["10","20","50","100","200","500", "1000","2000","5000","10000","20000"]
Ns1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

## yticks tiempo transcurrido ##
labels_y1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dts1 = [10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**(0), 10, 60, 600]

## yticks uso memoria ##
labels_y2 = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
mems1 = [1e3, 10**(4), 10**(5), 10**(6), 10**(7), 10**(8), 10**(9), 10**(10)]


plt.figure(1)

plt.subplot(2,1,1)

plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento Inversa dtype=single")

for i in range(L):
	plt.loglog(Ns_1[i*L:(i+1)*L],dts_1[i*L:(i+1)*L],marker=".",linestyle='-.', color="r", alpha=0.4, label="Numpy")

for i in range(LL):
	plt.loglog(Ns_2[i*LL:(i+1)*LL],dts_2[i*LL:(i+1)*LL],marker=".",linestyle='-.', color="y", alpha=0.4, label="Scipy overwrite False")

for i in range(LLL):
	plt.loglog(Ns_3[i*LLL:(i+1)*LLL],dts_3[i*LLL:(i+1)*LLL],marker=".",linestyle='-.', color="c", alpha=0.4, label="Scipy overwrite True")

plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)
plt.xticks(visible=False)


plt.subplot(2,1,2)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.loglog(Ns_1,mems_1,marker=".", color="r", label="Numpy", alpha=0.3)
plt.loglog(Ns_2,mems_2,marker=".", color="y", label="Scipy overwrite False", alpha=0.3)
plt.loglog(Ns_3,mems_3,marker=".", color="c", label="Scipy overwrite True", alpha=0.3)
plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(mems1, labels_y2)
plt.grid(True)
plt.axhline(y=16e9, color='k', linestyle='--')

plt.tight_layout()
plt.legend()
plt.savefig("plot_single.png")

plt.show()