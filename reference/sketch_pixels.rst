pixels[]
========

The ``pixels[]`` array contains the values for all the pixels in the display window.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pixels_0.png
    :alt: example picture for pixels[]

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        pink = "#F6C"
        py5.load_pixels()
        for i in range(0, (py5.width*py5.height//2) - py5.width//2):
            py5.pixels[i] = pink
    
        py5.update_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``pixels[]`` array contains the values for all the pixels in the display window. These values are of the color datatype. This array is defined by the size of the display window. For example, if the window is 100 x 100 pixels, there will be 10,000 values and if the window is 200 x 300 pixels, there will be 60,000 values. When the pixel density is set to higher than 1 with the :doc:`sketch_pixel_density` function, these values will change. See the reference for :doc:`sketch_pixel_width` or :doc:`sketch_pixel_height` for more information. 

Before accessing this array, the data must loaded with the :doc:`sketch_load_pixels` function. Failure to do so may result in a Java ``NullPointerException``. Subsequent changes to the display window will not be reflected in ``pixels`` until :doc:`sketch_load_pixels` is called again. After ``pixels`` has been modified, the :doc:`sketch_update_pixels` function must be run to update the content of the display window.

Underlying Processing field: `pixels <https://processing.org/reference/pixels.html>`_

Updated on August 25, 2022 20:01:47pm UTC

