import numpy as np
import json

def InitParams(init, n1, n2, ncomp, nobscomb, Isv):
    if type(init) == str:
        if init.lower() == 'random':
            init = {}
        else:
            # load file
            with open(init,'r') as initFile:
                init = json.load(initFile)

    if 'A' in init:
        A = init['A']
    else:
        q, r = np.linalg.qr(np.random.randn(n1,ncomp))
        A = q

    if 'S' in init:
        S = init['S']
    else:
        q, r =np.linalg.qr(np.random.randn(ncomp,n2))
        S = q

    if 'Mu' in init and init['Mu']:
        Mu = init['Mu']
    else:
        Mu = []

    # double check this Av part
    if 'Av' in init and init['Av']:
        Av = init['Av']
        if len(Av.shape) == 2:
            newAv = []
            for i = in xrange(n1): 
                newAv.append(np.diag(Av[i,:]))
            Av = np.array(newAv)                    
    else:
        Av = []
        for i in xrange(n1):
            Av.append(np.identity(ncomp))
            Av = np.array(Av)
            
    if 'Muv' in init and init['Muv']:
        Muv = init['Muv']
    else:
        Muv = np.ones(n1)

    if 'V' in init:
        V = init['V']
    else:
        V = 1
    #incomplete
    if 'Sv' in init and init['Sv']:
        Sv = init['Sv']
    else:
        Sv = []

    return A, S, Mu, V, Av, Sv, Muv     


