Py5Image.pixel_density
======================

Pixel density of the Py5Image object.

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
        py5.pixel_density(2)
        img = py5.create_image(100, 100, py5.RGB)
        py5.println(img.pixel_density, img.pixel_width, img.pixel_height)  # prints 1, 100, 100

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Pixel density of the Py5Image object. This will always be equal to 1, even if the Sketch used :doc:`sketch_pixel_density` to set the pixel density to a value greater than 1.

Underlying Processing field: PImage.pixelDensity

Updated on August 25, 2022 20:01:47pm UTC

