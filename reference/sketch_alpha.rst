alpha()
=======

Extracts the alpha value from a color, scaled to match current :doc:`sketch_color_mode`.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_alpha_0.png
    :alt: example picture for alpha()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        c = py5.color(0, 126, 255, 102)
        py5.fill(c)
        py5.rect(15, 15, 35, 70)
        value = py5.alpha(c)  # sets 'value' to 102
        py5.fill(value)
        py5.rect(50, 15, 35, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Extracts the alpha value from a color, scaled to match current :doc:`sketch_color_mode`.

The ``alpha()`` function is easy to use and understand, but it is slower than a technique called bit shifting. When working in ``color_mode(RGB, 255)``, you can achieve the same results as ``alpha()`` but with greater speed by using the right shift operator (``>>``) with a bit mask. For example, ``alpha(c)`` and ``c >> 24 & 0xFF`` both extract the alpha value from a color variable ``c`` but the later is faster.

Underlying Processing method: `alpha <https://processing.org/reference/alpha_.html>`_

Signatures
----------

.. code:: python

    alpha(
        rgb: int,  # any value of the color datatype
        /,
    ) -> float
Updated on September 01, 2022 12:53:02pm UTC

