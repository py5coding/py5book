tint()
======

Sets the fill value for displaying images.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_0.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        img = py5.load_image("laDefense.jpg")
        py5.image(img, 0, 0)
        py5.tint(0, 153, 204)  # tint blue
        py5.image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_1.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        img = py5.load_image("laDefense.jpg")
        py5.image(img, 0, 0)
        py5.tint(0, 153, 204, 126)  # tint blue and set transparency
        py5.image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tint_2.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        img = py5.load_image("laDefense.jpg")
        py5.image(img, 0, 0)
        py5.tint(255, 126)  # apply transparency without changing color
        py5.image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the fill value for displaying images. Images can be tinted to specified colors or made transparent by including an alpha value.

To apply transparency to an image without affecting its color, use white as the tint color and specify an alpha value. For instance, ``tint(255, 128)`` will make an image 50% transparent (assuming the default alpha range of 0-255, which can be changed with :doc:`sketch_color_mode`).

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a four or seven character string beginning with the "``#``" character (e.g., ``"#FC3"`` or ``"#FFCC33"``). After the "``#``" character, the remainder of the string is similar to hexadecimal notation, but without an alpha component.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

Underlying Processing method: `tint <https://processing.org/reference/tint_.html>`_

Syntax
------

.. code:: python

    tint(gray: float, /) -> None
    tint(gray: float, alpha: float, /) -> None
    tint(rgb: int, /) -> None
    tint(rgb: int, alpha: float, /) -> None
    tint(v1: float, v2: float, v3: float, /) -> None
    tint(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the image
* **gray**: `float` - specifies a value between white and black
* **rgb**: `int` - color value in hexadecimal notation
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)


Updated on November 12, 2021 11:30:58am UTC

