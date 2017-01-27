import numpy as np
import pandas as pd
import networkx as nx
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

# http://stackoverflow.com/questions/35233664/pass-pandas-dataframe-to-scipy-optimize-curve-fit

# X = np.random.randn(100, 4)     # independent variables
# m = np.random.randn(4)          # known coefficients
# y = X.dot(m)                    # dependent variable
#
# df = pd.DataFrame(np.hstack((X, y[:, None])),
#                   columns=['A', 'B', 'C', 'D', 'Z_real'])
#
# print df.head()
#
# def func(X, *params):
#     return np.hstack(params).dot(X)
#
# popt, pcov = curve_fit(func, df[['A', 'B', 'C', 'D']].T, df['Z_real'],
#                        p0=np.random.randn(4))
#
# print(np.allclose(popt, m))

# power law
x = range(1,1000)
y = [i**(-2.5) for i in x]

## use a proper power law random number generator (or code your own)
from networkx.utils import powerlaw_sequence
import powerlaw

#pl_sequence = powerlaw_sequence(1000,exponent=2.5)
def powerlaw_sequence(n,exponent=2.0):
  """
  Return sample sequence of length n from a power law distribution.
  """
  import random
  return [random.paretovariate(exponent-1) for i in range(n)]

pl_sequence = powerlaw_sequence(20)
pl_sequence = sorted(pl_sequence,reverse=True)

fitted_pl = powerlaw.Fit(y)

print 'alpha (exponent)' , fitted_pl.alpha
#print help(fitted_pl)print
# y = [i**(-fitted_pl.alpha) for i in pl_sequence]

fig, ax = plt.subplots()

'''
ax.set_xscale('log')
ax.set_yscale('log')
ax.plot(y)
ax.plot(range(0,len(pl_sequence)), pl_sequence, '+')

#ax.plot(pl_sequence)
# plplot
# http://tuvalu.santafe.edu/~aaronc/powerlaws/plplot.py

import plplot as plp

xmin = 1
alpha=2.71
x = pl_sequence #[500,150,90,81,75,75,70,65,60,58,49,47,40]
x = [500,150,90,81,75,75,70,65,60,58,49,47,40]
df= pd.DataFrame.from_dict(nx.karate_club_graph().degree().items())
gb = df.groupby([1]).count()
x = list(gb[0])
print x
h = plp.plplot(x,xmin,alpha);

print np.shape(pl_sequence)

'''

from scipy import linspace, randn, log10, optimize, sqrt

powerlaw = lambda x, amp, index: amp * (x**index)

##########
# Generate data points with noise
##########
num_points = 20

# Note: all positive, non-zero data
xdata = linspace(1.1, 10.1, num_points)
ydata = powerlaw(xdata, 10.0, -2.0)     # simulated perfect data
yerr = 0.2 * ydata                      # simulated errors (10%)

ydata += randn(num_points) * yerr       # simulated noisy data
ydata = pl_sequence
##########
# Fitting the data -- Least Squares Method
##########

# Power-law fitting is best done by first converting
# to a linear equation and then fitting to a straight line.
#
#  y = a * x^b
#  log(y) = log(a) + b*log(x)
#

logx = log10(xdata)
logy = log10(ydata)
logyerr = yerr / ydata

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

pinit = [1.0, -1.0]
out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy, logyerr), full_output=1)

pfinal = out[0]
covar = out[1]
print pfinal
print covar

index = pfinal[1]
amp = 10.0**pfinal[0]

indexErr = sqrt( covar[0][0] )
ampErr = sqrt( covar[1][1] ) * amp

print index

# ########
# plotting
# ########
ax.plot(ydata)
ax.plot(pl_sequence)

fig.clf()
fig, axs = plt.subplots(2,1)

axs[0].plot(xdata, powerlaw(xdata, amp, index))     # Fit
axs[0].errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
axs[0].text(5, 6.5, 'Ampli = %5.2f +/- %5.2f' % (amp, ampErr))
axs[0].text(5, 5.5, 'Index = %5.2f +/- %5.2f' % (index, indexErr))
axs[0].set_title('Best Fit Power Law')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
# xlim(1, 11)
#
# subplot(2, 1, 2)
axs[1].loglog(xdata, powerlaw(xdata, amp, index))
axs[1].errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
axs[1].set_xlabel('X (log scale)')
axs[1].set_ylabel('Y (log scale)')
# xlim(1.0, 11)


plt.savefig('tmpfig', bbox_inches='tight')
