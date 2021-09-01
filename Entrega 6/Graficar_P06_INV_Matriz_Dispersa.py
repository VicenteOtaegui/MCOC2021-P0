import matplotlib.pylab as plt
import numpy as np


fid = open(f"Entrega_P06_INV_Matriz_Dispersa.txt","r")

Ns_1  = []
L=0
dts_ensamblaje = []
dts_solucion   = []

for line in fid:
	L=L+1
	sl = line.split()
	# print (sl)
	N = int(sl[2])
	dt_ensamblaje = float(sl[5])
	dt_solucion = float(sl[9])
	Ns_1.append(N)
	dts_ensamblaje.append(dt_ensamblaje)
	dts_solucion.append(dt_solucion)
fid.close()

T=43
NS1 = Ns_1[0:T]

DTSE1 = dts_ensamblaje[0:T]
DTSS1 = dts_solucion[0:T]

DTSE2 = dts_ensamblaje[T:2*T]
DTSS2 = dts_solucion[T:2*T]

DTSE3 = dts_ensamblaje[2*T:3*T]
DTSS3 = dts_solucion[2*T:3*T]

DTSE4= dts_ensamblaje[3*T:4*T]
DTSS4 = dts_solucion[3*T:4*T]

DTSE5 = dts_ensamblaje[4*T:5*T]
DTSS5 = dts_solucion[4*T:5*T]

DTSE6 = dts_ensamblaje[5*T:6*T]
DTSS6 = dts_solucion[5*T:6*T]

DTSE7 = dts_ensamblaje[6*T:7*T]
DTSS7= dts_solucion[6*T:7*T]

DTSE8 = dts_ensamblaje[7*T:8*T]
DTSS8 = dts_solucion[7*T:8*T]

DTSE9 = dts_ensamblaje[8*T:9*T]
DTSS9 = dts_solucion[8*T:9*T]

DTSE10 = dts_ensamblaje[9*T:10*T]
DTSS10 = dts_solucion[9*T:10*T]

labels_x = ["10","20","50","100","200","500", "1000","2000","5000","10000","20000"]
Ns1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

## yticks tiempo transcurrido ##
labels_y1 = ["0.01 ms","0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dts1 = [10**(-5),10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**(0), 10, 60, 600]

# Rectas O(N) para tiempos de ensamblado

yi= DTSE1[0] 
yf= DTSE1[T-1]
Nmax = 20000
O_N0_x = [1,Nmax]
O_N0_y = [yf,yf]

O_N1_x = [1,Nmax]
O_N1_y = [yi,yf]

g=Nmax*((0.000001/yf)**(1/2))
O_N2_x = [g,Nmax]
O_N2_y = [0.00001,yf]


g=Nmax*((0.000001/yf)**(1/3))
O_N3_x = [g,Nmax]
O_N3_y = [0.00001,yf]

g=Nmax*((0.000001/yf)**(1/4))
O_N4_x = [g,Nmax]
O_N4_y = [0.00001,yf]

g=Nmax*((0.000001/yf)**(1/5))
O_N5_x = [g,Nmax]
O_N5_y = [0.00001,yf]


# Rectas O(N) para tiempos de solucion


yi= DTSS1[0] 
yf= DTSS1[T-1]

O_N0_x_s = [1,Nmax]
O_N0_y_s = [yf,yf]

O_N1_x_s = [1,Nmax]
O_N1_y_s = [yi,yf]

g=Nmax*((0.000001/yf)**(1/2))
O_N2_x_s = [g,Nmax]
O_N2_y_s = [0.000001,yf]


g=Nmax*((0.000001/yf)**(1/3))
O_N3_x_s = [g,Nmax]
O_N3_y_s = [0.000001,yf]

g=Nmax*((0.000001/yf)**(1/4))
O_N4_x_s = [g,Nmax]
O_N4_y_s = [0.000001,yf]


## graficar ## 

plt.figure(1)

plt.subplot(2,1,1)

plt.ylabel("Tiempo de ensamblaje")
plt.title("Rendimiento INV para Matriz DISPERSA")

alfa=0.4

plt.plot(O_N0_x, O_N0_y, color='b', linestyle='--', label="Constante")
plt.plot(O_N1_x, O_N1_y, color='y', linestyle='--', label="O(N)")
plt.plot(O_N2_x, O_N2_y, color='g', linestyle='--', label="$\mathregular{O(N^2)}$")
plt.plot(O_N3_x, O_N3_y, color='r', linestyle='--', label="$\mathregular{O(N^3)}$")
plt.plot(O_N4_x, O_N4_y, color='m', linestyle='--', label="$\mathregular{O(N^4)}$")

plt.loglog(NS1,DTSE1,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE2,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE3,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE4,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE5,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE6,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE7,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE8,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE9,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSE10,marker=".", color="k", alpha=alfa)
plt.ylim(0.00001,600)

plt.legend()






plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)
plt.xticks(visible=False)

plt.subplot(2,1,2)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo de solucion")
plt.plot(O_N0_x_s, O_N0_y_s, color='b', linestyle='--', label="Constante")
plt.plot(O_N1_x_s, O_N1_y_s, color='y', linestyle='--', label="O(N)")
plt.plot(O_N2_x_s, O_N2_y_s, color='g', linestyle='--', label="O(N2)")
plt.plot(O_N3_x_s, O_N3_y_s, color='r', linestyle='--', label="O(N3)")
plt.plot(O_N4_x_s, O_N4_y_s, color='m', linestyle='--', label="O(N4)")

plt.loglog(NS1,DTSS1,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS2,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS3,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS4,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS5,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS6,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS7,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS8,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS9,marker=".", color="k", alpha=alfa)
plt.loglog(NS1,DTSS10,marker=".", color="k", alpha=alfa)
plt.ylim(0.00001,600)
plt.xticks(Ns1, labels_x, rotation = 45)
plt.yticks(dts1, labels_y1)
plt.grid(True)

plt.tight_layout()
plt.savefig("plot_P06_INV_Matriz_Dispersa.png")

plt.show()