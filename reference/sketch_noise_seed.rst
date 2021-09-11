noise_seed()
============

Sets the seed value for :doc:`sketch_noise`.

Examples
--------

.. raw:: html

    <div class="example-table">

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

Sets the seed value for :doc:`sketch_noise`. By default, :doc:`sketch_noise` produces different results each time the program is run. Set the seed parameter to a constant to return the same pseudo-random numbers each time the Sketch is run.

Py5's noise functionality is provided by the Python noise library. The noise library provides more advanced features than what is documented here. To use the more advanced features, import that library directly.

Syntax
------

.. code:: python

    noise_seed(seed: int) -> None

Parameters
----------

* **seed**: `int` - seed value


Updated on September 11, 2021 16:51:34pm UTC

