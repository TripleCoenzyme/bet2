===================
bet2
===================
standalone Brain Extraction Tool (bet2) with python wrapper, released by http://fsl.fmrib.ox.ac.uk/

The following features are added:

 * reconfigured with CMake (I suggest using CMake version > 3.15.)
 * support windows platform
 * python wrapper based on `pybind11 <https://github.com/pybind/pybind11>`_, allow to install with pip (new)
 * use 4D numpy array as input and output for multi-echo GRE images (new)
 * enable openmp (new)

To install:

.. code-block:: bash

  git clone --recursive https://github.com/TripleCoenzyme/bet2.git
  
  pip install ./bet2
  
To use:

.. code-block:: python
  
  import bet2
  
  mask = bet2.run_bet(image_array, voxel_size, f_th, g_th)
  
where 

* **image_array** is the 4D float numpy image array in (x, y, z, echo)
* **voxel_size** is a list containing spatial resolution in (x, y, z)
* **f_th** and **g_th** is *OPTIONAL* fractional_threshold and gradient_threshold in original BET (with -f and -g). Default set to 0.4 and 0.

a test.py and a tmp.nii test data can be found in the path.

Known BUG:

1. Output array dtype will be numpy.float32 but not int as given. **Please convert output to numpy.uint8 to save space.**
2. **Only support CMake<3.19 in Ubuntu 18.04**, no matter with gcc/g++ 7, 8 or 9.

Thank twice to Liangfu Chen for his contribution.
