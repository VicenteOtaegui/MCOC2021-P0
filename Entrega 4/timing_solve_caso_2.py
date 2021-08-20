from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import solve, inv
from numpy import eye, float32, ones, float64, double, zeros
import numpy as np


def laplaciana(N, tipo=float32):
	e=eye(N)-eye(N,N,1)
	return tipo(e+e.T)

dts = []
mems = []

Ns = 	[1,5,10,20,40,60,80,100,120,140,160,180,200,220,
		240,260,280,300,320,340,360,380,400,420,440,460,
		480,500,600,700,800,900,1000,2500,5000,10000]

Nschico = 	[1,5,10,20,40,60,80,100,120,140,160,180,200,220,
			240,260,280,300,320,340,360,380,400,420,440,460,
			480,500,750,1000]

fid = open(f"rendimiento_P04_solve32_caso_II.txt", "w")

for i in range(10):

	for N in Ns:

		A=laplaciana(N)
		b=ones(N)

		t1 = perf_counter()
		x  = solve(A,b)
		t2 = perf_counter()

		dt = t2-t1

		# print (f"Tiempo transcurrido: {dt} s")

		dts.append(dt)

		fid.write(f"N = {N} dt = {dt} s\n" )

	print (f"Corrida single {i+1} lista")

fid.close()


def laplaciana(N, dtype):
	A = zeros(((N,N)) ,dtype = dtype)
	for i in range (N):
		A[i,i] = 2
		for j in range (max((0,i-2)),i):
			if abs(i-j) == 1:
				A[i,j] = -1
				A[j,i] = -1
	return (A)

fid = open(f"rendimiento_P04_solve64_caso_II.txt", "w")

for i in range(10):

	for N in Ns:

		A=laplaciana(N, dtype=double)
		b=ones(N)

		t1 = perf_counter()
		x  = solve(A,b)
		t2 = perf_counter()

		dt = t2-t1

		# print (f"Tiempo transcurrido: {dt} s")

		dts.append(dt)

		fid.write(f"N = {N} dt = {dt} s\n" )
		
	print (f"Corrida double {i+1} lista")

fid.close()

