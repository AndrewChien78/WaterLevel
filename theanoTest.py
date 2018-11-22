# This code is from Fabian Tence's post on Ankivil.com
# This code can be used to test if the installation of Theano has been carried out correctly.
# The post can be found at: 
# https://ankivil.com/installing-keras-theano-and-dependencies-on-windows-10/
#
# The expected result should be:
# [Elemwise{exp,no_inplace}(<TensorType(float64, vector)>)]
# Looping 1000 times took 13.727821 seconds
# Result is [1.23178032 1.61879341 1.52278065 ... 2.20771815 2.29967753 1.62323285]
# Used the cpu

from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()
t1 = time.time()
print("Looping %d times took %f seconds" % (iters, t1 - t0))
print("Result is %s" % (r,))
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')