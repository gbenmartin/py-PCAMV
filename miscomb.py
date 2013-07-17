#  Computes the combinations of missing values in each column 
#  of a data matrix. This is needed for faster implementation.

import numpy as np

def miscomb(M,verbose):
    n1,n2 = M.shape
    if verbose:
        print 'Calculating Isv ...'

    tmp, I, Isv = np.unique(M.view([('',M.dtype)]*M.shape[1]),return_index=True,return_inverse=True)
    #tmp = tmp.view(M.dtype).reshape(-1,M.shape[1])
    nobscomb = tmp.shape[0]

    if nobscomb < n2:
        obscombj = [np.array([]) for i in xrange(nobscomb)]
        for i in xrange(n2):
            if obscombj[Isv[i]].size==0:
                obscombj[Isv[i]] = np.array([i])
            else:
                obscombj[Isv[i]]=np.append(x[Isv[i]],i)

    else:
        obscombj=[]
        Isv = []
    
    if verbose:
        print 'done'
        print 'Missing values combinations: found %d in %d columns'%(nobscomb, n2)

    return nobscomb, obscombj, Isv
