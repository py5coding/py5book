Py5Image.load_np_pixels()
=========================

Loads the pixel data of the image into the :doc:`py5image_np_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_load_np_pixels_0.png
    :alt: example picture for load_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        my_image = py5.load_image("apples.jpg")
        my_image.load_np_pixels()
        my_image.np_pixels[:50, :, :] = my_image.np_pixels[50:100, :, :]
        my_image.update_np_pixels()
        py5.image(my_image, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Loads the pixel data of the image into the :doc:`py5image_np_pixels` array. This method must always be called before reading from or writing to :doc:`py5image_np_pixels`. Subsequent changes to the image will not be reflected in :doc:`py5image_np_pixels` until ``py5image_load_np_pixels()`` is called again.

The ``load_np_pixels()`` method is similar to :doc:`py5image_load_pixels` in that ``load_np_pixels()`` must be called before reading from or writing to :doc:`py5image_np_pixels` just as :doc:`py5image_load_pixels` must be called before reading from or writing to :doc:`py5image_pixels`.

Note that ``load_np_pixels()`` will as a side effect call :doc:`py5image_load_pixels`, so if your code needs to read :doc:`py5image_np_pixels` and :doc:`py5image_pixels` simultaneously, there is no need for a separate call to :doc:`py5image_load_pixels`. However, be aware that modifying both :doc:`py5image_np_pixels` and :doc:`py5image_pixels` simultaneously will likely result in the updates to :doc:`py5image_pixels` being discarded.

Signatures
----------

.. code:: python

    load_np_pixels() -> None

Updated on September 01, 2022 14:08:27pm UTC

