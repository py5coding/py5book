pixel_height
============

Height of the display window in pixels.

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

    def setup():
        py5.size(600, 400)
        py5.pixel_density(2)
        py5.println(py5.width, py5.height)
        py5.println(py5.pixel_width, py5.pixel_height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(600, 400)
        py5.pixel_density(2)  # double the pixel density
        py5.println(py5.width, py5.height)
        py5.println(py5.pixel_width, py5.pixel_height)


    def draw():
        py5.load_pixels()
        # fill all the pixels to blue with using
        # pixel_width and pixel_height
        for i in range(0, py5.pixel_width*py5.pixel_height):
            py5.pixels[i] = "#00F"

        # fill one quarter of the pixels to yellow
        # because the pixel density is set to 2 in setup()
        # and 'width' and 'height' don't reflect the pixel
        # dimensions of the sketch
        for i in range(0, py5.width*py5.height):
            py5.pixels[i] = "#FF0"

        py5.update_pixels()
        py5.no_loop()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Height of the display window in pixels. When ``pixel_density(2)`` is used to make use of a high resolution display (called a Retina display on OSX or high-dpi on Windows and Linux), the width and height of the Sketch do not change, but the number of pixels is doubled. As a result, all operations that use pixels (like :doc:`sketch_load_pixels`, :doc:`sketch_get`, etc.) happen in this doubled space. As a convenience, the variables :doc:`sketch_pixel_width` and ``pixel_height`` hold the actual width and height of the Sketch in pixels. This is useful for any Sketch that use the :doc:`sketch_pixels` or :doc:`sketch_np_pixels` arrays, for instance, because the number of elements in each array will be ``pixel_width*pixel_height``, not ``width*height``.

Underlying Processing field: `pixelHeight <https://processing.org/reference/pixelHeight.html>`_


Updated on November 12, 2021 11:30:58am UTC

