Py5Graphics.text()
==================

Draws text to the Py5Graphics drawing surface.

Description
-----------

Draws text to the Py5Graphics drawing surface. Displays the information specified in the first parameter on the drawing surface in the position specified by the additional parameters. A default font will be used unless a font is set with the :doc:`py5graphics_text_font` function and a default size will be used unless a font is set with :doc:`py5graphics_text_size`. Change the color of the text with the :doc:`py5graphics_fill` function. The text displays in relation to the :doc:`py5graphics_text_align` function, which gives the option to draw to the left, right, and center of the coordinates.

The ``x2`` and ``y2`` parameters define a rectangular area to display within and may only be used with string data. When these parameters are specified, they are interpreted based on the current :doc:`py5graphics_rect_mode` setting. Text that does not fit completely within the rectangle specified will not be drawn.

Note that py5 lets you call ``text()`` without first specifying a Py5Font with :doc:`py5graphics_text_font`. In that case, a generic sans-serif font will be used instead.

This method is the same as :doc:`sketch_text` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_text`.

Underlying Processing method: PGraphics.text

Signatures
------

.. code:: python

    text(
        c: chr,  # the alphanumeric character to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        /,
    ) -> None

    text(
        c: chr,  # the alphanumeric character to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        z: float,  # z-coordinate of text
        /,
    ) -> None

    text(
        chars: list[chr],  # the alphanumberic symbols to be displayed
        start: int,  # array index at which to start writing characters
        stop: int,  # array index at which to stop writing characters
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        /,
    ) -> None

    text(
        chars: list[chr],  # the alphanumberic symbols to be displayed
        start: int,  # array index at which to start writing characters
        stop: int,  # array index at which to stop writing characters
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        z: float,  # z-coordinate of text
        /,
    ) -> None

    text(
        num: float,  # the numeric value to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        /,
    ) -> None

    text(
        num: float,  # the numeric value to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        z: float,  # z-coordinate of text
        /,
    ) -> None

    text(
        num: int,  # the numeric value to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        /,
    ) -> None

    text(
        num: int,  # the numeric value to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        z: float,  # z-coordinate of text
        /,
    ) -> None

    text(
        str: str,  # string to be displayed
        x1: float,  # by default, the x-coordinate of text, see rectMode() for more info
        y1: float,  # by default, the y-coordinate of text, see rectMode() for more info
        x2: float,  # by default, the width of the text box, see rectMode() for more info
        y2: float,  # by default, the height of the text box, see rectMode() for more info
        /,
    ) -> None

    text(
        str: str,  # string to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        /,
    ) -> None

    text(
        str: str,  # string to be displayed
        x: float,  # x-coordinate of text
        y: float,  # y-coordinate of text
        z: float,  # z-coordinate of text
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

