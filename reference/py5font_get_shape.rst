Py5Font.get_shape()
===================

Get a single character as a :doc:`py5shape` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Font_get_shape_0.png
    :alt: example picture for get_shape()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        font = py5.create_font('DejaVu Sans', 32)
        chr_p = font.get_shape('p')
        chr_y = font.get_shape('y')
        chr_5 = font.get_shape('5')

        chr_p.disable_style()
        chr_y.disable_style()
        chr_5.disable_style()

        py5.fill(0)
        py5.no_stroke()

        x = 25
        py5.shape(chr_p, x, 40)
        x += chr_p.get_width()
        py5.shape(chr_y, x, 60)
        x += chr_y.get_width()
        py5.shape(chr_5, x, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get a single character as a :doc:`py5shape` object. Use the ``detail`` parameter to draw the shape with only straight line segments.

Calling :doc:`py5shape_disable_style` on the returned :doc:`py5shape` object seems to be necessary for these to be drawable.

This method only works on fonts loaded with :doc:`sketch_create_font`.

Underlying Java method: PFont.getShape

Syntax
------

.. code:: python

    get_shape(ch: chr, /) -> Py5Shape
    get_shape(ch: chr, detail: float, /) -> Py5Shape

Parameters
----------

* **ch**: `chr` - single character
* **detail**: `float` - level of shape detail


Updated on September 11, 2021 16:51:34pm UTC

