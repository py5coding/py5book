blue()
======

Extracts the blue value from a color, scaled to match current :doc:`sketch_color_mode`.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_blue_0.png
    :alt: example picture for blue()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        c = "#AF64DC"  # define color 'c'
        py5.fill(c)  # use color variable 'c' as fill color
        py5.rect(15, 20, 35, 60)  # draw left rectangle
    
        blue_value = py5.blue(c)  # get blue in 'c'
        py5.println(blue_value)  # prints "220.0"
        py5.fill(0, 0, blue_value)  # use 'blue_value' in new fill
        py5.rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Extracts the blue value from a color, scaled to match current :doc:`sketch_color_mode`.

The ``blue()`` function is easy to use and understand, but it is slower than a technique called bit masking. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``blue()`` but with greater speed by using a bit mask to remove the other color components. For example, ``blue(c)`` and ``c & 0xFF`` both extract the blue value from a color variable ``c`` but the later is faster.

Underlying Processing method: `blue <https://processing.org/reference/blue_.html>`_

Signatures
----------

.. code:: python

    blue(
        rgb: int,  # any value of the color datatype
        /,
    ) -> float
Updated on September 01, 2022 12:53:02pm UTC

