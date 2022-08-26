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

When using web color notation to specify a color, create a string beginning with the "``#``" character followed by three, four, six, or eight characters. The example colors ``"#D93"`` and ``"#DD9933"`` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors ``"#D93F"`` and ``"#DD9933FF"`` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

Underlying Processing method: `tint <https://processing.org/reference/tint_.html>`_

Signatures
------

.. code:: python

    tint(
        gray: float,  # specifies a value between white and black
        /,
    ) -> None

    tint(
        gray: float,  # specifies a value between white and black
        alpha: float,  # opacity of the image
        /,
    ) -> None

    tint(
        rgb: int,  # color value in hexadecimal notation
        /,
    ) -> None

    tint(
        rgb: int,  # color value in hexadecimal notation
        alpha: float,  # opacity of the image
        /,
    ) -> None

    tint(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    tint(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        alpha: float,  # opacity of the image
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

