os_noise_seed()
===============

Sets the seed value for :doc:`sketch_os_noise`.

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
        py5.os_noise_seed(42)
        py5.stroke(0, 10)


    def draw():
        n = py5.remap(py5.os_noise(0.2, py5.frame_count / 100), -1, 1, 0, py5.width)
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
        global xpos, ypos
        py5.rect_mode(py5.CENTER)
        py5.os_noise_seed(42)
        xpos = py5.width / 2
        ypos = py5.height / 2


    def draw():
        global xpos, ypos
        py5.background(128)
        xpos = (xpos + py5.os_noise(xpos, py5.frame_count / 250)) % py5.width
        ypos = (ypos + py5.os_noise(ypos, py5.frame_count / 250)) % py5.height
        py5.square(xpos, ypos, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the seed value for :doc:`sketch_os_noise`. By default, :doc:`sketch_os_noise` produces different results each time the program is run. Set the seed parameter to a constant to return the same pseudo-random numbers each time the Sketch is run.

Signatures
----------

.. code:: python

    os_noise_seed(
        seed: int,  # seed value
        /,
    ) -> None

Updated on September 01, 2022 14:08:27pm UTC

