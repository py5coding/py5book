cursor()
========

Sets the cursor to a predefined symbol or an image, or makes it visible if already hidden.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # move the mouse left and right across the image
    # to see the cursor change from_ a cross to a hand

    def draw():
        if py5.mouse_x < 50:
            py5.cursor(py5.CROSS)
        else:
            py5.cursor(py5.HAND)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the cursor to a predefined symbol or an image, or makes it visible if already hidden. If you are trying to set an image as the cursor, the recommended size is 16x16 or 32x32 pixels. The values for parameters ``x`` and ``y`` must be less than the dimensions of the image.

Setting or hiding the cursor does not generally work with "Present" mode (when running full-screen).

With the ``P2D`` and ``P3D`` renderers, a generic set of cursors are used because the OpenGL renderer doesn't have access to the default cursor images for each platform (Processing Issue 3791).

Underlying Java method: `cursor <https://processing.org/reference/cursor_.html>`_

Syntax
------

.. code:: python

    cursor() -> None
    cursor(img: Py5Image, /) -> None
    cursor(img: Py5Image, x: int, y: int, /) -> None
    cursor(kind: int, /) -> None

Parameters
----------

* **img**: `Py5Image` - any variable of type Py5Image
* **kind**: `int` - either ARROW, CROSS, HAND, MOVE, TEXT, or WAIT
* **x**: `int` - the horizontal active spot of the cursor
* **y**: `int` - the vertical active spot of the cursor


Updated on September 11, 2021 16:51:34pm UTC

