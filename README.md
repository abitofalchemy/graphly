# Xplograph

A sandbox for exploring graphs and machine learning.

Graphs are also referred to as networks and formaly defined by:

G = (V,E) 

##  Machine Learning

Machine learning and optimization methos.
  
  - Supervised Methods
  - Unsupervised (or semi supervised) Methods
  - Decision tree problems and methods
  - Clustering
  - Dimensionality reduction


##  Graph Mining

Data mining and graph mining analytic methods
igraph

### Modularity

Sites Used:

The following was requrired by igraph to work in script (CLI):
- [Installing pkgconfig on macosx, src code](https://lists.freedesktop.org/archives/pkg-config/2016-March/001043.html)
	but using brew install pkg-config also worked just note that we need the dependencies, and to finally compile pycairo
	I had to call configure using `LIBTOOLIZE=glibtoolize ./autogen.sh --prefix=/Users/saguinag/anaconda2` see the 
	file `macosx_commands.txt`
- [pycairo](https://www.cairographics.org/pycairo/)
- [easy-flexible-framework-for-community-detection](http://www.traag.net/2013/10/25/easy-flexible-framework-for-community-detection/#zp-ID-163-1383957-EPZH5I7G)

Next to tackle:
- https://blog.dominodatalab.com/social-network-analysis-with-networkx/




## Directories

`./Modularity` Modularity | Clustering | Community Detection 

`./Theano` Jupyter notebooks on Theano setup and examples.

## StarLog
- 20Dec16: Get this working https://blog.dominodatalab.com/social-network-analysis-with-networkx/ 
