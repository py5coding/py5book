Py5Image.pixel_width
====================

Width of the Py5Image object in pixels.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.pixel_density(2)
        img = py5.create_image(100, 100, py5.RGB)
        py5.println(img.pixel_density, img.pixel_width, img.pixel_height)  # prints 1, 100, 100

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Width of the Py5Image object in pixels. This will be the same as :doc:`py5image_width`, even if the Sketch used :doc:`sketch_pixel_density` to set the pixel density to a value greater than 1.

Underlying Processing field: PImage.pixelWidth

Updated on September 01, 2022 16:36:02pm UTC

