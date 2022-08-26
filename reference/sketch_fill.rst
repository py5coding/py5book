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

When using web color notation to specify a color, create a string beginning with the "``#``" character followed by three, four, six, or eight characters. The example colors ``"#D93"`` and ``"#DD9933"`` specify red, green, and blue values (in that order) for the color and assume the color has no transparency. The example colors ``"#D93F"`` and ``"#DD9933FF"`` specify red, green, blue, and alpha values (in that order) for the color. Notice that in web color notation the alpha channel is last, which is consistent with CSS colors, and in hexadecimal notation the alpha channel is first, which is consistent with Processing color values.

The value for the "gray" parameter must be less than or equal to the current maximum value as specified by :doc:`sketch_color_mode`. The default maximum value is 255.

To change the color of an image or a texture, use :doc:`sketch_tint`.

Underlying Processing method: `fill <https://processing.org/reference/fill_.html>`_

Signatures
------

.. code:: python

    fill(
        gray: float,  # number specifying value between white and black
        /,
    ) -> None

    fill(
        gray: float,  # number specifying value between white and black
        alpha: float,  # opacity of the fill
        /,
    ) -> None

    fill(
        rgb: int,  # color variable or hex value
        /,
    ) -> None

    fill(
        rgb: int,  # color variable or hex value
        alpha: float,  # opacity of the fill
        /,
    ) -> None

    fill(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        /,
    ) -> None

    fill(
        v1: float,  # red or hue value (depending on current color mode)
        v2: float,  # green or saturation value (depending on current color mode)
        v3: float,  # blue or brightness value (depending on current color mode)
        alpha: float,  # opacity of the fill
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

