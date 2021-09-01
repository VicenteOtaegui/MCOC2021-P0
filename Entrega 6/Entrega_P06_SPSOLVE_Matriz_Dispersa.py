from numpy import double, ones
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from laplaciana_sparse import laplaciana
from time import perf_counter

Ns = 	[1,5,10,20,40,60,80,100,120,140,160,180,200,220,
		240,260,280,300,320,340,360,380,400,420,440,460,
		480,500,600,700,800,900,1000,2000,3000,4000,5000,
		6000,7000,8000,9000,10000,20000,30000,40000,50000,
		60000,70000,80000,90000,100000,200000,300000,400000,
		500000,1000000,5000000,10000000]

# print (len(Ns)) # = 58

fid = open(f"Entrega_P06_SPSOLVE_Matriz_Dispersa.txt", "w")

for i in range(10):
	for N in Ns:

		t1 = perf_counter()

		A = laplaciana(N)
		b = ones(N, dtype=double)
		Acsr = sp.csr_matrix(A)

		t2 = perf_counter()

		x = lin.spsolve(Acsr,b)

		t3 = perf_counter()

		dt_ensamblaje = t2 - t1
		dt_solucion = t3 - t2

		#print (f"Tiempo ensamblaje: {dt_ensamblaje} s")
		#print (f"Tiempo solución: {dt_solucion} s")

		fid.write(f"N = {N} dt_ensamblaje = {dt_ensamblaje} s dt_solucion = {dt_solucion}\n" )
	
	print (f"Corrida {i+1} lista")

fid.close()