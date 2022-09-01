red()
=====

Extracts the red value from a color, scaled to match current :doc:`sketch_color_mode`.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_red_0.png
    :alt: example picture for red()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        c = "#FFCC00"  # define color 'c'
        py5.fill(c)  # use color variable 'c' as fill color
        py5.rect(15, 20, 35, 60)  # draw left rectangle
    
        red_value = py5.red(c)  # get red in 'c'
        py5.println(red_value)  # print "255.0"
        py5.fill(red_value, 0, 0)  # use 'red_value' in new fill
        py5.rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Extracts the red value from a color, scaled to match current :doc:`sketch_color_mode`.

The ``red()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``red()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``red(c)`` and ``c >> 16 & 0xFF`` both extract the red value from a color variable ``c`` but the later is faster.

Underlying Processing method: `red <https://processing.org/reference/red_.html>`_

Signatures
----------

.. code:: python

    red(
        rgb: int,  # any value of the color datatype
        /,
    ) -> float

Updated on September 01, 2022 14:08:27pm UTC

