text_descent()
==============

Returns descent of the current font at its current size.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_descent_0.png
    :alt: example picture for text_descent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        base = py5.height * 0.75
        scalar = 0.8  # different for each font
    
        py5.text_size(32)  # set initial text size
        a = py5.text_descent() * scalar  # calc ascent
        py5.line(0, base+a, py5.width, base+a)
        py5.text("dp", 0, base)  # draw text on baseline
    
        py5.text_size(64)  # increase text size
        a = py5.text_descent() * scalar  # recalc ascent
        py5.line(40, base+a, py5.width, base+a)
        py5.text("dp", 40, base)  # draw text on baseline

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns descent of the current font at its current size. This information is useful for determining the height of the font below the baseline.

Underlying Processing method: `textDescent <https://processing.org/reference/textDescent_.html>`_

Signatures
----------

.. code:: python

    text_descent() -> float
Updated on September 01, 2022 12:53:02pm UTC

