from numpy import float64, eye
import numpy as np

def laplaciana (N):
	d = np.eye(N,N,1, dtype=float64)
	return 2*np.eye(N,dtype=float64) - d - d.T

