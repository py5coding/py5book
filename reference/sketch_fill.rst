fill()
======

Sets the color used to fill shapes.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_fill_0.png
    :alt: example picture for fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.fill(153)
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_fill_1.png
    :alt: example picture for fill()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.fill(204, 102, 0)
        py5.rect(30, 20, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the color used to fill shapes. For example, if you run ``fill(204, 102, 0)``, all subsequent shapes will be filled with orange. This color is either specified in terms of the ``RGB`` or ``HSB`` color depending on the current :doc:`sketch_color_mode`. The default color space is ``RGB``, with each value in the range from 0 to 255.

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the "gray" parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

To change the color of an image or a texture, use :doc:`sketch_tint`.

Underlying Processing method: `fill <https://processing.org/reference/fill_.html>`_

Syntax
------

.. code:: python

    fill(gray: float, /) -> None
    fill(gray: float, alpha: float, /) -> None
    fill(rgb: int, /) -> None
    fill(rgb: int, alpha: float, /) -> None
    fill(v1: float, v2: float, v3: float, /) -> None
    fill(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the fill
* **gray**: `float` - number specifying value between white and black
* **rgb**: `int` - color variable or hex value
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 12, 2021 11:30:58am UTC

