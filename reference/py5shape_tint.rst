Py5Shape.tint()
===============

Apply a color tint to a shape's texture map.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_tint_0.png
    :alt: example picture for tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)
        img = py5.load_image("tower.jpg")
        s = py5.create_shape()
        s.begin_shape()
        s.texture(img)
        s.tint(0, 0, 255)
        s.vertex(20, 20, 0, 0)
        s.vertex(20, 80, 0, 100)
        s.no_tint()
        s.vertex(80, 80, 100, 100)
        s.vertex(80, 20, 100, 0)
        s.end_shape(py5.CLOSE)

        py5.shape(s)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Apply a color tint to a shape's texture map. The tint will be applied only to vertices after the call to ``tint()``. Use :doc:`py5shape_no_tint` to deactivate the tint.

Images can be tinted to specified colors or made transparent by including an alpha value. To apply transparency to an image without affecting its color, use white as the tint color and specify an alpha value. For instance, ``tint(255, 128)`` will make an image 50% transparent (assuming the default alpha range of 0-255, which can be changed with :doc:`sketch_color_mode`).

When using hexadecimal notation to specify a color, use "``0x``" before the values (e.g., ``0xFFCCFFAA``). The hexadecimal value must be specified with eight characters; the first two characters define the alpha component, and the remainder define the red, green, and blue components.

When using web color notation to specify a color, create a string beginning with the "``#``" character followed by three, four, six, or eight characters. The example colors ``"#D93"`` and ``"#DD9933"`` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors ``"#D93F"`` and ``"#DD9933FF"`` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the gray parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

The ``tint()`` function is also used to control the coloring of textures in 3D.

Underlying Processing method: PShape.tint

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
        x: float,  # red or hue value (depending on current color mode)
        y: float,  # green or saturation value (depending on current color mode)
        z: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    tint(
        x: float,  # red or hue value (depending on current color mode)
        y: float,  # green or saturation value (depending on current color mode)
        z: float,  # blue or brightness value (depending on current color mode)
        alpha: float,  # opacity of the image
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

