Py5Image.pixels[]
=================

The pixels[] array contains the values for all the pixels in the image.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_pixels_0.png
    :alt: example picture for pixels[]

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global tower
        tower = py5.load_image("tower.jpg")
        dimension = tower.width * tower.height
        tower.load_pixels()
        for i in range(0, dimension, 2):
            tower.pixels[i] = "#000"

        tower.update_pixels()


    def draw():
        py5.image(tower, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The pixels[] array contains the values for all the pixels in the image. These values are of the color datatype. This array is the size of the image, meaning if the image is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. 

Before accessing this array, the data must loaded with the :doc:`py5image_load_pixels` method. Failure to do so may result in a Java ``NullPointerException``. After the array data has been modified, the :doc:`py5image_update_pixels` method must be run to update the content of the display window.

Underlying Processing field: `PImage.pixels <https://processing.org/reference/PImage_pixels.html>`_


Updated on November 12, 2021 11:30:58am UTC

