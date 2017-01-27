from urllib2 import urlopen
import numpy as np
import pandas
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
# src: 
try:
     salary_table = pandas.read_csv('./salary.table')
except:
     print "fetching from website"
     url = 'http://stats191.stanford.edu/data/salary.table'
     #the next line is not necessary with recent version of pandas
     url = urlopen(url)
     salary_table = pandas.read_table(url)
     salary_table.to_csv('salary.table', index=False)

E = salary_table.E
M = salary_table.M
X = salary_table.X
S = salary_table.S

plt.figure(figsize=(6, 6));
symbols = ['D', '^']
colors = ['r', 'g', 'blue']
factor_groups = salary_table.groupby(['E', 'M'])
print factor_groups.groups.keys()

for values, group in factor_groups:
    print group
    break
    i, j = values
    plt.scatter(group['X'], group['S'], marker=symbols[j], color=colors[i - 1],
                 s=144)
exit()
plt.xlabel('Experience');
plt.ylabel('Salary');
plt.show()


