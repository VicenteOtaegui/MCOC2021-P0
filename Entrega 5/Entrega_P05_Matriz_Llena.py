import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as lin
from time import perf_counter
from numpy import zeros, eye, double, float64

def matriz_laplaciana_dispersa (N, t=double):
	return sparse.eye(N,dtype=t)-sparse.eye(N,N,1, dtype=t)

def matriz_laplaciana_llena (N, dtype):
	A = zeros(((N,N)) ,dtype = dtype)
	for i in range (N):
		A[i,i] = 2
		for j in range (max((0,i-2)),i):
			if abs(i-j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return (A)

Ns = 	[1,5,10,20,40,60,80,100,120,140,160,180,200,220,
		240,260,280,300,320,340,360,380,400,420,440,460,
		480,500,600,700,800,900,1000,2000,3000,4000,5000,
		6000,7000,8000,9000,10000,12000,14000,16000,18000]
# print (len(Ns)) = 46

fid = open(f"Entrega_P05_Matriz_Llena.txt", "w")

for i in range (10):
	for N in Ns:

		t1 = perf_counter()

		A = matriz_laplaciana_llena(N,double)
		B = matriz_laplaciana_llena(N,double)

		#A = matriz_laplaciana_dispersa(N)
		#B = matriz_laplaciana_dispersa(N)

		t2 = perf_counter()

		C = A @ B

		t3 = perf_counter()

		dt_ensamblaje = t2 - t1
		dt_solucion = t3 - t2

		fid.write(f"N = {N} dt_ensamblaje = {dt_ensamblaje} s dt_solucion = {dt_solucion}\n" )


		# print (f"C: {C}")
	
	print (f"Corrida {i+1} lista")

fid.close()