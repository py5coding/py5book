Py5Image.get()
==============

Reads the color of any pixel or grabs a section of an image.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_get_0.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        mountains = py5.load_image("rockies.jpg")
        py5.background(mountains)
        py5.no_stroke()
        c = mountains.get(60, 90)
        py5.fill(c)
        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_get_1.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        mountains = py5.load_image("rockies.jpg")
        py5.background(mountains)
        new_mountains = mountains.get(50, 0, 50, 100)
        py5.image(new_mountains, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Reads the color of any pixel or grabs a section of an image. If no parameters are specified, the entire image is returned. Use the ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the image by specifying additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and ``y`` parameters define the coordinates for the upper-left corner of the returned image, regardless of the current :doc:`sketch_image_mode`.

If the pixel requested is outside of the image, black is returned. The numbers returned are scaled according to the current color ranges, but only ``RGB`` values are returned by this function. For example, even though you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in ``RGB`` format.

Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast as grabbing the data directly from :doc:`py5image_pixels`. The equivalent statement to ``get(x, y)`` using :doc:`py5image_pixels` is ``pixels[y*width+x]``. See the reference for :doc:`py5image_pixels` for more information.

Underlying Processing method: `PImage.get <https://processing.org/reference/PImage_get_.html>`_

Signatures
----------

.. code:: python

    get() -> Py5Image

    get(
        x: int,  # x-coordinate of the pixel
        y: int,  # y-coordinate of the pixel
        /,
    ) -> int

    get(
        x: int,  # x-coordinate of the pixel
        y: int,  # y-coordinate of the pixel
        w: int,  # width of pixel rectangle to get
        h: int,  # height of pixel rectangle to get
        /,
    ) -> Py5Image

Updated on September 01, 2022 16:36:02pm UTC

