from numpy import zeros, float64
import scipy.sparse as sparse

def laplaciana (N):
	d = sparse.eye(N,N,1, dtype=float64)
	return 2*sparse.eye(N,dtype=float64) - d - d.T

