green()
=======

Extracts the green value from a color, scaled to match current :doc:`sketch_color_mode`.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_green_0.png
    :alt: example picture for green()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        c = "#144BC8"  # define color 'c'
        py5.fill(c)  # use color variable 'c' as fill color
        py5.rect(15, 20, 35, 60)  # draw left rectangle
    
        green_value = py5.green(c)  # get green in 'c'
        py5.println(green_value)  # print "75.0"
        py5.fill(0, green_value, 0)  # use 'green_value' in new fill
        py5.rect(50, 20, 35, 60)  # draw right rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Extracts the green value from a color, scaled to match current :doc:`sketch_color_mode`.

The ``green()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``green()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``green(c)`` and ``c >> 8 & 0xFF`` both extract the green value from a color variable ``c`` but the later is faster.

Underlying Processing method: `green <https://processing.org/reference/green_.html>`_

Signatures
----------

.. code:: python

    green(
        rgb: int,  # any value of the color datatype
        /,
    ) -> float

Updated on September 01, 2022 16:36:02pm UTC

