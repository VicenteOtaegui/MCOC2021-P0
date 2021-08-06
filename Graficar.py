import matplotlib.pylab as plt
from psutil import virtual_memory

## print (virtual_memory().total/(10**9))

Ns = []
dts = []
mems = []

for i in range (10):
	fid = open(f"rendimiento{i}.txt","r")
	L=0
	for line in fid:
		sl = line.split()
		N = int(sl[2])
		dt = float(sl[5])
		mem = int(sl[9])
		L+=1
		Ns.append(N)
		dts.append(dt)
		mems.append(mem)

		#print (sl)

	fid.close()

# print (Ns)
# print (dts)
# print (mems)

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
plt.title("Rendimiento A@B")

for i in range(L):
	plt.loglog(Ns[i*L:(i+1)*L],dts[i*L:(i+1)*L],marker=".",linestyle='-.')

plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)
plt.xticks(visible=False)

plt.subplot(2,1,2)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria")
plt.loglog(Ns,mems,marker=".")
plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(mems1, labels_y2)
plt.grid(True)
plt.axhline(y=12e9, color='k', linestyle='--')

plt.tight_layout()
plt.savefig("plot.png")

plt.show()