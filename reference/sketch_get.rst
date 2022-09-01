get()
=====

Reads the color of any pixel or grabs a section of the drawing surface.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_get_0.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        py5.image(my_image, 0, 0)
        c = py5.get()
        py5.image(c, py5.width//2, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_get_1.png
    :alt: example picture for get()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        py5.image(my_image, 0, 0)
        c = py5.get(25, 25)
        py5.fill(c)
        py5.no_stroke()
        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Reads the color of any pixel or grabs a section of the drawing surface. If no parameters are specified, the entire drawing surface is returned. Use the ``x`` and ``y`` parameters to get the value of one pixel. Get a section of the display window by specifying additional ``w`` and ``h`` parameters. When getting an image, the ``x`` and ``y`` parameters define the coordinates for the upper-left corner of the returned image, regardless of the current :doc:`sketch_image_mode`.

If the pixel requested is outside of the image window, black is returned. The numbers returned are scaled according to the current color ranges, but only ``RGB`` values are returned by this function. For example, even though you may have drawn a shape with ``color_mode(HSB)``, the numbers returned will be in ``RGB`` format.

If a width and a height are specified, ``get(x, y, w, h)`` returns a Py5Image corresponding to the part of the original Py5Image where the top left pixel is at the ``(x, y)`` position with a width of ``w`` a height of ``h``.

Getting the color of a single pixel with ``get(x, y)`` is easy, but not as fast as grabbing the data directly from :doc:`sketch_pixels` or :doc:`sketch_np_pixels`. The equivalent statement to ``get(x, y)`` using :doc:`sketch_pixels` is ``pixels[y*width+x]``. Using :doc:`sketch_np_pixels` it is ``np_pixels[y, x]``. See the reference for :doc:`sketch_pixels` and :doc:`sketch_np_pixels` for more information.

Underlying Processing method: `get <https://processing.org/reference/get_.html>`_

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

Updated on September 01, 2022 14:08:27pm UTC

