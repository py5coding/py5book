Py5Image.update_pixels()
========================

Updates the image with the data in its :doc:`py5image_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_update_pixels_0.png
    :alt: example picture for update_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global my_image
        global half_image
        half_image = py5.width * py5.height//2
        my_image = py5.load_image("apples.jpg")
        my_image.load_pixels()
        for i in range(0, half_image):
            my_image.pixels[i+half_image] = my_image.pixels[i]

        my_image.update_pixels()


    def draw():
        py5.image(my_image, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Updates the image with the data in its :doc:`py5image_pixels` array. Use in conjunction with :doc:`py5image_load_pixels`. If you're only reading pixels from the array, there's no need to call ``update_pixels()``.

Underlying Java method: `PImage.updatePixels <https://processing.org/reference/PImage_updatePixels_.html>`_

Syntax
------

.. code:: python

    update_pixels() -> None
    update_pixels(x: int, y: int, w: int, h: int, /) -> None

Parameters
----------

* **h**: `int` - height
* **w**: `int` - width
* **x**: `int` - x-coordinate of the upper-left corner
* **y**: `int` - y-coordinate of the upper-left corner


Updated on September 11, 2021 16:51:34pm UTC

