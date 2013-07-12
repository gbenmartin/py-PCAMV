# RMEMPTY - Remove empty columns or rows from data matrix
# removes empty columns or rows from data matrix X and matrix Xprobe
# of probing data. Those columns and rows do not affect the found
# solution.

import numpy as np
from scipy import sparse

def rmempty(X):
#def rmempty(X, Xprobe, init, verbose=0):
    [n1x,n2x] = X.shape
    if sparse.issparse(X):
        Ic = [i[0] for i in np.argwhere(np.sum(X!=0,0)>0)]
        Ir = [i[0] for i in np.argwhere(np.sum(X!=0,1)>0)]
    else:
        Ic = [i[0] for i in np.argwhere(np.sum(np.isnan(X)==False,0)>0)]
        Ir = [i[0] for i in np.argwhere(np.sum(np.isnan(X)==False,1)>0)]

    n1 = len(Ir)
    n2 = len(Ic)

    X = np.array([X[j][i] for j in Ir for i in Ic])
    X.shape = (len(Ir),len(Ic))
    
    return X, Ir, Ic
#   return X, Xprobe, Ir, Ic, init


