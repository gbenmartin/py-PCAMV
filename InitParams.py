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

    #double check this
    if 'Sv' in init and init['Sv']:
        initSv=init['Sv']
        if nobscomb < n2:
            B,I=np.unique(Isv,return_index=True)
            if len(initSv.shape) == 2:
                Sv=[]
                for j in xrange(nobscomb):                
                    Sv.append(np.diag(initSv[:,j]))
                Sv=np.array(Sv)
            elif 'Isv' in init and init['Isv']]}:
                Sv=initSv[init['Isv'][I]]
            else:
                Sv=[]
                for j in xrange(nobscomb):
                    Sv.append(initSv[Isv][I][j])
                Sv=np.array(Sv)
        else:
            if len(initSv.shape) == 2:
                Sv=[]
                for j in xrange(n2):
                    Sv.append(np.diag(initSv[:,j]))
                Sv=np.array(Sv)
            elif 'Isv' in init and init['Isv']]}:
                Sv=initSv[init['Isv']]
            elif len(initSv)==n2:
                Sv=initSv
    else:
        Sv = []
        for i in xrange(nobscomb):
            Sv.append(np.identity(ncomp))
        Sv = np.array(Sv)

    return A, S, Mu, V, Av, Sv, Muv     


