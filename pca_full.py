from scipy.sparse import issparse

[ opts, errmsg, wrnmsg ] = argschk( opts, varargin{:} );
if ~isempty(errmsg), error( errmsg ), end
if ~isempty(wrnmsg), warning( wrnmsg ), end
Xprobe = opts['xprobe'];

algo = opts['algorithm']
if algo =='ppca':
    use_prior = 0
    use_postervar = 0
elif algo == 'map'
    use_prior = 1
    use_postervar = 0
elif algo == 'vb'
    use_prior = 1
    use_postervar = 1
else
    raise NameError('Wrong value of the argument ''algorithm''')

n1x,n2x = X.shape
X, Xprobe, Ir, Ic, opts['init'] = rmempty(X, Xprobe,
                                            opts['init'], opts['verbose'])

n1,n2 = X.shape




if not use_postervar:
    # MAP estimation for Mu and A
    Muv = []
    Av = {}

if not Mu:
    if opts['bias']:
        Mu = sum(X,2) ./ Nobs_i
    else
        Mu = np.zeros(n1,1)
