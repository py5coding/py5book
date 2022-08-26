Py5Image.load_pixels()
======================

Loads the pixel data for the image into its :doc:`py5image_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_load_pixels_0.png
    :alt: example picture for load_pixels()

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

Loads the pixel data for the image into its :doc:`py5image_pixels` array. This function must always be called before reading from or writing to :doc:`py5image_pixels`.

Underlying Processing method: `PImage.loadPixels <https://processing.org/reference/PImage_loadPixels_.html>`_

Signatures
------

.. code:: python

    load_pixels() -> None
Updated on August 25, 2022 20:01:47pm UTC

