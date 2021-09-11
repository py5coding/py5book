Py5Image.copy()
===============

Copies a region of pixels from one image into another.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_copy_0.png
    :alt: example picture for copy()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global apples
        apples = py5.load_image("apples.jpg")
        x = py5.width//2
        apples.copy(x, 0, x, py5.height, 0, 0, x, py5.height)


    def draw():
        py5.image(apples, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Copies a region of pixels from one image into another. If the source and destination regions aren't the same size, it will automatically resize source pixels to fit the specified target region. No alpha information is used in the process, however if the source image has an alpha channel set, it will be copied as well.

This function ignores :doc:`sketch_image_mode`.

Underlying Java method: `PImage.copy <https://processing.org/reference/PImage_copy_.html>`_

Syntax
------

.. code:: python

    copy() -> Py5Image
    copy(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None
    copy(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, /) -> None

Parameters
----------

* **dh**: `int` - destination image height
* **dw**: `int` - destination image width
* **dx**: `int` - x-coordinate of the destination's upper left corner
* **dy**: `int` - y-coordinate of the destination's upper left corner
* **sh**: `int` - source image height
* **src**: `Py5Image` - an image variable referring to the source image.
* **sw**: `int` - source image width
* **sx**: `int` - x-coordinate of the source's upper left corner
* **sy**: `int` - y-coordinate of the source's upper left corner


Updated on September 11, 2021 16:51:34pm UTC

