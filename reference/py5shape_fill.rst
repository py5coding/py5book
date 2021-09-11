Py5Shape.fill()
===============

Sets the color used to fill the ``Py5Shape`` object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_fill_0.png
    :alt: example picture for fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape()
        s.begin_shape()
        s.fill(230, 230, 25)
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

Sets the color used to fill the ``Py5Shape`` object. For example, if you run ``fill(204, 102, 0)``, the shape will be filled with orange. This color is either specified in terms of the ``RGB`` or ``HSB`` color depending on the current :doc:`sketch_color_mode`. The default color space is ``RGB``, with each value in the range from 0 to 255.

This method can only be used within a :doc:`py5shape_begin_shape` and :doc:`py5shape_end_shape` pair.

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the "gray" parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

To change the color of a ``Py5Shape`` object's image or a texture, use :doc:`py5shape_tint`.

Underlying Java method: PShape.fill

Syntax
------

.. code:: python

    fill(gray: float, /) -> None
    fill(gray: float, alpha: float, /) -> None
    fill(rgb: int, /) -> None
    fill(rgb: int, alpha: float, /) -> None
    fill(x: float, y: float, z: float, /) -> None
    fill(x: float, y: float, z: float, a: float, /) -> None

Parameters
----------

* **a**: `float` - opacity of the fill
* **alpha**: `float` - opacity of the fill
* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - color variable or hex value
* **x**: `float` - red or hue value (depending on current color mode)
* **y**: `float` - green or saturation value (depending on current color mode)
* **z**: `float` - blue or brightness value (depending on current color mode)


Updated on September 11, 2021 16:51:34pm UTC

