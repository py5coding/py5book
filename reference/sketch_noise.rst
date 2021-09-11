noise()
=======

Generate pseudo-random noise values for specific coodinates.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_noise_0.png
    :alt: example picture for noise()

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

.. image:: /images/reference/Sketch_noise_1.png
    :alt: example picture for noise()

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

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # Animated Noise demo
    import numpy as np


    def setup():
        py5.size(200, 200)
        py5.noise_seed(42)
        py5.noise_mode(py5.PERLIN_NOISE)
        py5.noise_detail(octaves=4, persistence=0.5, lacunarity=2.0)
        global x, y
        x, y = np.meshgrid(
            np.linspace(
                0, 5, py5.width), np.linspace(
                0, 5, py5.height))


    def draw():
        new_pixels = py5.remap(
            py5.noise(x, y, py5.frame_count / 100), -1, 1, 0, 255).astype(np.uint8)
        py5.set_np_pixels(new_pixels, bands='L')

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.noise_seed(42)
        py5.stroke(0, 10)


    def draw():
        n = py5.remap(py5.noise(py5.frame_count / 100), -1, 1, 0, 1) * py5.width
        py5.line(n, 0, n, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect_mode(py5.CENTER)
        py5.noise_seed(42)
        global xpos, ypos
        xpos = py5.width / 2
        ypos = py5.height / 2


    def draw():
        py5.background(128)
        global xpos, ypos
        xpos = (xpos + py5.noise(py5.frame_count / 200)) % py5.width
        ypos = (ypos + py5.noise(500 + py5.frame_count / 200)) % py5.height
        py5.square(xpos, ypos, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Generate pseudo-random noise values for specific coodinates. Noise functions are random sequence generators that produce a more natural, harmonic succession of numbers compared to the :doc:`sketch_random` function. Several well-known noise algorithms were developed by Ken Perlin and have been used in graphical applications to generate procedural textures, shapes, terrains, and other seemingly organic forms.

In contrast to the :doc:`sketch_random` function, noise is defined in an n-dimensional space, in which each coordinate corresponds to a fixed pseudo-random value (fixed only for the lifespan of the program). Py5 can generate Perlin Noise and Simplex Noise. By default, py5 will generate noise using the Simplex Noise algorithm. The noise value can be animated by moving through the noise space, as demonstrated in the examples. Any dimension can also be interpreted as time. An easy way to animate the noise value is to pass the ``noise()`` function the :doc:`sketch_frame_count` divided by a scaling factor, as is done in a few of the examples.

The generated noise values for both Perlin Noise and Simplex Noise will be between -1 and 1. This contrasts with Processing's noise function, which typically returns values between 0 and 1.

Perlin Noise can be generated in 1, 2, or 3 dimensions and Simplex Noise can be generated in 1, 2, 3, or 4 dimensions. Technically Simplex Noise cannot be generated in only 1 dimension, but as a convenience, py5 will add a second dimension for you (with a value of 0) if only one dimension is used.

The actual noise structure is similar to that of an audio signal, in respect to the function's use of frequencies. Similar to the concept of harmonics in physics, both noise algorithms are computed over several octaves which are added together for the final result.

The nature of the noise values returned can be adjusted with :doc:`sketch_noise_mode`, :doc:`sketch_noise_seed`, and :doc:`sketch_noise_detail`.

Another way to adjust the character of the resulting sequence is the scale of the input coordinates. As the function works within an infinite space, the value of the coordinates doesn't matter as such; only the distance between successive coordinates is important (such as when using ``noise()`` within a loop). As a general rule, the smaller the difference between coordinates, the smoother the resulting noise sequence. Steps of 0.005-0.03 work best for most applications, but this will differ depending on the use case and the noise settings.

Py5's noise functionality is provided by the Python noise library. The noise library provides more advanced features than what is documented here. To use the more advanced features, import that library directly.

Py5's ``noise()`` function can also accept numpy arrays as parameters. It will automatically vectorize the operations and use broadcasting when needed.

Syntax
------

.. code:: python

    noise(x: float, **kwargs) -> float
    noise(x: float, y: float, **kwargs) -> float
    noise(x: float, y: float, z: float, **kwargs) -> float
    noise(x: float, y: float, z: float, w: float, **kwargs) -> float

Parameters
----------

* **kwargs**: - keyword arguments to override existing noise detail or noise seed settings
* **w**: `float` - w-coordinate in noise space
* **x**: `float` - x-coordinate in noise space
* **y**: `float` - y-coordinate in noise space
* **z**: `float` - z-coordinate in noise space


Updated on September 11, 2021 16:51:34pm UTC

