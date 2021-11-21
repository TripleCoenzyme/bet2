===================
bet2
===================
standalone Brain Extraction Tool (bet2) with python wrapper, released by http://fsl.fmrib.ox.ac.uk/

The following features are added:

 * reconfigured with CMake
 * support windows platform
 * use 4D numpy array as input and output for multi-echo GRE images (new)
 * enable openmp (new)

to compile source code (not tested yet -- Jie Feng):

.. code-block:: bash

 mkdir build
 cd build
 cmake ..
 make -j6

Need more test.

Thank twice to Liangfu Chen for his contribution.
