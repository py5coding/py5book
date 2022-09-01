load_np_pixels()
================

Loads the pixel data of the current display window into the :doc:`sketch_np_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_np_pixels_0.png
    :alt: example picture for load_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        py5.image(my_image, 0, 0)
    
        py5.load_np_pixels()
        py5.np_pixels[50:100, :, :] = py5.np_pixels[:50, :, :]
        py5.update_np_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Loads the pixel data of the current display window into the :doc:`sketch_np_pixels` array. This method must always be called before reading from or writing to :doc:`sketch_np_pixels`. Subsequent changes to the display window will not be reflected in :doc:`sketch_np_pixels` until ``load_np_pixels()`` is called again.

The ``load_np_pixels()`` method is similar to :doc:`sketch_load_pixels` in that ``load_np_pixels()`` must be called before reading from or writing to :doc:`sketch_np_pixels` just as :doc:`sketch_load_pixels` must be called before reading from or writing to :doc:`sketch_pixels`.

Note that ``load_np_pixels()`` will as a side effect call :doc:`sketch_load_pixels`, so if your code needs to read :doc:`sketch_np_pixels` and :doc:`sketch_pixels` simultaneously, there is no need for a separate call to :doc:`sketch_load_pixels`. However, be aware that modifying both :doc:`sketch_np_pixels` and :doc:`sketch_pixels` simultaneously will likely result in the updates to :doc:`sketch_pixels` being discarded.

Signatures
----------

.. code:: python

    load_np_pixels() -> None

Updated on September 01, 2022 14:08:27pm UTC

