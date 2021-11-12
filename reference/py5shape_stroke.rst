Py5Shape.stroke()
=================

Sets the color used to draw the ``Py5Shape`` object's lines.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_stroke_0.png
    :alt: example picture for stroke()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.stroke(255, 0, 0)
        s.vertex(20, 80)
        s.vertex(50, 20)
        s.vertex(80, 80)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the color used to draw the ``Py5Shape`` object's lines. This color is either specified in terms of the RGB or HSB color depending on the current :doc:`sketch_color_mode`. The default color space is RGB, with each value in the range from 0 to 255.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

When drawing in 2D with the default renderer, you may need ``hint(ENABLE_STROKE_PURE)`` to improve drawing quality (at the expense of performance). See the :doc:`sketch_hint` documentation for more details.

Underlying Processing method: PShape.stroke

Syntax
------

.. code:: python

    stroke(gray: float, /) -> None
    stroke(gray: float, alpha: float, /) -> None
    stroke(rgb: int, /) -> None
    stroke(rgb: int, alpha: float, /) -> None
    stroke(x: float, y: float, z: float, /) -> None
    stroke(x: float, y: float, z: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the stroke
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **x**: `float` - red or hue value (depending on current color mode)
* **y**: `float` - green or saturation value (depending on current color mode)
* **z**: `float` - blue or brightness value (depending on current color mode)


Updated on November 12, 2021 11:30:58am UTC

