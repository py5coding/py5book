load_pixels()
=============

Loads the pixel data of the current display window into the :doc:`sketch_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_pixels_0.png
    :alt: example picture for load_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        half_image = py5.width*py5.height//2
        my_image = py5.load_image("apples.jpg")
        py5.image(my_image, 0, 0)
    
        py5.load_pixels()
        for i in range(0, half_image):
            py5.pixels[i+half_image] = py5.pixels[i]
    
        py5.update_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Loads the pixel data of the current display window into the :doc:`sketch_pixels` array. This function must always be called before reading from or writing to :doc:`sketch_pixels`. Subsequent changes to the display window will not be reflected in :doc:`sketch_pixels` until ``load_pixels()`` is called again.

Underlying Processing method: `loadPixels <https://processing.org/reference/loadPixels_.html>`_

Signatures
----------

.. code:: python

    load_pixels() -> None
Updated on September 01, 2022 12:53:02pm UTC

