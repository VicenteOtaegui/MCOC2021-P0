from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt


Ns = [1,5,10]
for i in range (20,600,20):
	Ns.append(i)
Ns[-1]=8000
Ns[-2]=5000
Ns[-3]=2000
Ns[-4]=1000


#print (Ns)
#print (len(Ns))
# exit(0)

dts = []
mems = []


for i in range(10):
	fid = open(f"rendimiento{i}.txt", "w")

	for N in Ns:

		uso_memoria = 0

		A = zeros ((N, N), dtype=float16) + 1

		uso_memoria_teorico = 4*N*N #bytes... float32 4bytes
		uso_memoria_numpy  = A.nbytes
		#print (f"uso_memoria_teorico = {uso_memoria_teorico}")
		#print (f"uso_memoria_numpy = {uso_memoria_numpy}")

		B = zeros ((N, N))+2

		# print (f"A = {A}")
		# print (f"B = {B}")

		t1 = perf_counter()
		C = A@B
		t2 = perf_counter()

		uso_memoria_total = A.nbytes + B.nbytes + C.nbytes

		dt = t2-t1
		dts.append(dt)
		mems.append(uso_memoria_total)

		print (f"N = {N} dt = {dt} s _ uso_memoria_total= {uso_memoria_total} bytes _ flops = {N**3/dt} flops/s")

		fid.write(f"N = {N} dt = {dt} s _ uso_memoria_total= {uso_memoria_total} bytes \n" )
	
	print (f"iteración = {i}")

	fid.close()

### END ###