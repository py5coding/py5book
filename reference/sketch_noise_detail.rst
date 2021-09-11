noise_detail()
==============

Adjusts the character and level of detail produced by the :doc:`sketch_noise` function.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_noise_detail_0.png
    :alt: example picture for noise_detail()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.noise_mode(py5.PERLIN_NOISE)
        py5.noise_seed(42)
        draw_noise_line(1, 0.25 * py5.height)
        draw_noise_line(2, 0.50 * py5.height)
        draw_noise_line(4, 0.75 * py5.height)


    def draw_noise_line(octaves, y):
        py5.noise_detail(octaves=octaves)
        for i in range(py5.width):
            py5.point(i, y + 25 * py5.noise(i / 50))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_noise_detail_1.png
    :alt: example picture for noise_detail()

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

.. image:: /images/reference/Sketch_noise_detail_2.png
    :alt: example picture for noise_detail()

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

Adjusts the character and level of detail produced by the :doc:`sketch_noise` function. Similar to harmonics in physics, noise is computed over several octaves. Lower octaves contribute more to the output signal and as such define the overall intensity of the noise, whereas higher octaves create finer-grained details in the noise sequence.

By default, noise is computed over 4 octaves. Each octave has half the amplitude and twice the frequency of its predecessor. The decrease in amplitude can be adjusted with the ``persistence`` parameter. The increase in frequency can be adjusted with the ``lacunarity`` parameter.

For example, a ``persistence`` parameter of 0.75 means each octave will now have 75% impact (25% less) of the previous lower octave. A ``lacunarity`` parameter of 4 means that each octave will have 4 times the frequency of the previous lower octave, providing noise at a finer-grained scale than what the default value of 2 would provide.

By changing these parameters, the signal created by the :doc:`sketch_noise` function can be adapted to fit very specific needs and characteristics.

Py5's noise functionality is provided by the Python noise library. The noise library provides more advanced features than what is documented here. To use the more advanced features, import that library directly.

Syntax
------

.. code:: python

    noise_detail(octaves: float = None, persistence: float = None, lacunarity: float = None) -> None

Parameters
----------

* **lacunarity**: `float = None` - change in noise frequency from one octave to the next
* **octaves**: `float = None` - number of noise octaves
* **persistence**: `float = None` - change in noise amplitude from one octave to the next


Updated on September 11, 2021 16:51:34pm UTC

