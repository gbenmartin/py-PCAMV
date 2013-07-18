from scipy.sparse import issparse

def pca_full(X,ncomp,varargin):
#[ opts, errmsg, wrnmsg ] = argschk( opts, varargin{:} );

#if ~isempty(errmsg), error( errmsg ), end
#if ~isempty(wrnmsg), warning( wrnmsg ), end
    eps = np.spacing(1)

    Xprobe = opts['xprobe'];

    algo = opts['algorithm']
    if algo =='ppca':
        use_prior = 0
        use_postervar = 0
    elif algo == 'map':
        use_prior = 1
        use_postervar = 0
    elif algo == 'vb':
        use_prior = 1
        use_postervar = 1
    else:
        raise NameError('Wrong value of the argument ''algorithm''')

    n1x,n2x = X.shape
    X, Xprobe, Ir, Ic, opts['init'] = rmempty(X, Xprobe, opts['init'], opts['verbose'])
        
    n1,n2 = X.shape
        
    if issparse(X):
        M = X.copy()
        M.data.fill(1)
        Mprobe = Xprobe.copy()
        Mprobe.data.fill(1)

    else:
        M = X
        M[~np.isnan(X)] = 1
        M[np.isnan(X)] = 0
        Mprobe = Xprobe
        Mprobe[~np.isnan(Xprobe)] = 1
        Mprobe[np.isnan(Xprobe)] = 0
        
        X[np.where(X==0)] = eps
        Xprobe[np.where(Xprobe==0)] = eps
        X[np.isnan(X)] = 0
        Xprobe[np.isnan(Xprobe)] = 0


    if not use_postervar:
        # MAP estimation for Mu and A
        Muv = []
        Av = {}


#    if not Mu:
#        if opts['bias']:
#            Mu = sum(X,2) ./ Nobs_i
#        else:
#            Mu = np.zeros(n1,1)
