text_ascent()
=============

Returns ascent of the current font at its current size.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_ascent_0.png
    :alt: example picture for text_ascent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        base = py5.height * 0.75
        scalar = 0.8  # different for each font
    
        py5.text_size(32)  # set initial text size
        a = py5.text_ascent() * scalar  # calc ascent
        py5.line(0, base-a, py5.width, base-a)
        py5.text("dp", 0, base)  # draw text on baseline
    
        py5.text_size(64)  # increase text size
        a = py5.text_ascent() * scalar  # recalc ascent
        py5.line(40, base-a, py5.width, base-a)
        py5.text("dp", 40, base)  # draw text on baseline

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Returns ascent of the current font at its current size. This information is useful for determining the height of the font above the baseline.

Underlying Processing method: `textAscent <https://processing.org/reference/textAscent_.html>`_

Signatures
------

.. code:: python

    text_ascent() -> float
Updated on August 25, 2022 20:01:47pm UTC

