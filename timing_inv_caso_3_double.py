from time import perf_counter
from numpy import zeros, float16, float32, float64, half, single, double, longdouble, complex128
from scipy.linalg import inv
from laplaciana import laplaciana
import matplotlib.pylab as plt
import numpy as np

N = 2500
dts = []
mems = []

Ns = [1,5,10]
for i in range (20,600,20):
	Ns.append(i)
Ns[-1]=10000
Ns[-2]=5000
Ns[-3]=2500
Ns[-4]=1000


# print (Ns)
# print (len(Ns))
# exit(0)

fid = open(f"rendimiento_P03_11.txt", "w")

for i in range(10):

	for N in Ns:

		uso_memoria = 0
		t1 = perf_counter()
		A = laplaciana(N, dtype = double)

		# print (f"{A}")
		
		# exit(0)

		t2 = perf_counter()
		Am1 = inv(A, overwrite_a = True)
		t3 = perf_counter()

		dt_ensamblaje = t2 - t1
		dt_inversion = t3 - t2

		bytes_total= A.nbytes + Am1.nbytes

		dts.append(dt_inversion)
		mems.append(bytes_total)

		#print (f"N = {N} dt = {dt_inversion} s _ uso_memoria_total= {bytes_total/10**6} bytes _ flops = {N**3/dt_inversion} flops/s")

		fid.write(f"N = {N} dt = {dt_inversion} s _ uso_memoria_total= {bytes_total} bytes \n" )

		# print (f" Uso memoria: {bytes_total} bytes")
		# print (f" Tiempo ensamblaje: {dt_ensamblaje} s")
		# print (f" Tiempo inversion: {dt_inversion} s")

# print (A)
# print (Am1)

fid.close()