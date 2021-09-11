noise_mode()
============

Sets the kind of noise that the :doc:`sketch_noise` function will generate.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_noise_mode_0.png
    :alt: example picture for noise_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # Simplex Noise demo
    import numpy as np


    def setup():
        py5.noise_seed(42)
        py5.noise_mode(py5.SIMPLEX_NOISE)
        # these are the default values
        py5.noise_detail(octaves=4, persistence=0.5, lacunarity=2.0)
        global x, y
        x, y = np.meshgrid(np.linspace(0, 5, py5.width), np.linspace(0, 5, py5.height))


    def draw():
        new_pixels = py5.remap(py5.noise(x, y), -1, 1, 0, 255).astype(np.uint8)
        py5.set_np_pixels(new_pixels, bands='L')

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_noise_mode_1.png
    :alt: example picture for noise_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # Perlin Noise demo
    import numpy as np


    def setup():
        py5.noise_seed(42)
        py5.noise_mode(py5.PERLIN_NOISE)
        # these are the default values
        py5.noise_detail(octaves=4, persistence=0.5, lacunarity=2.0)
        global x, y
        x, y = np.meshgrid(np.linspace(0, 5, py5.width), np.linspace(0, 5, py5.height))


    def draw():
        new_pixels = py5.remap(py5.noise(x, y), -1, 1, 0, 255).astype(np.uint8)
        py5.set_np_pixels(new_pixels, bands='L')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the kind of noise that the :doc:`sketch_noise` function will generate. This can be either Perlin Noise or Simplex Noise. By default, py5 will generate noise using the Simplex Noise algorithm.

Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be generated in only 1 dimension, but as a convenience, py5 will add a second dimension for you (with a value of 0) if only one dimension is used.

The specific Perlin Noise implementation provided by py5 is the "Improved Perlin Noise" algorithm as described in Ken Perlin's 2002 SIGGRAPH paper. This uses the fifth degree polynomial ``f(t)=6t^5-15t^4+10t^3`` as the blending function. This is different from the "Classic Perlin Noise" algorithm, described in Ken Perlin's 1985 SIGGRAPH paper, which uses the third degree polynomial ``f(t)=3t^2-2t^3`` instead. The Simplex Noise algorithm, also developed by Ken Perlin, is different from Perlin Noise, and uses a completely different approach for generating noise values. Processing's noise algorithm is a valid and useful noise algorithm but is not identical to any of the algorithms mentioned here, so py5's noise values will not match Processing's no matter what inputs or settings are used.

Py5's noise functionality is provided by the Python noise library. The noise library provides more advanced features than what is documented here. To use the more advanced features, import that library directly.

Syntax
------

.. code:: python

    noise_mode(mode: int) -> None

Parameters
----------

* **mode**: `int` - kind of noise to generate, either PERLIN_NOISE or SIMPLEX_NOISE


Updated on September 11, 2021 16:51:34pm UTC

