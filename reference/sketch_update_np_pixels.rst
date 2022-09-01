update_np_pixels()
==================

Updates the display window with the data in the :doc:`sketch_np_pixels` array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_update_np_pixels_0.png
    :alt: example picture for update_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        img = py5.load_image("rockies.jpg")
        py5.image(img, 0, 0)
        py5.load_np_pixels()
        py5.np_pixels[50:100, :, :] = py5.np_pixels[:50, :, :]
        py5.update_np_pixels()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Updates the display window with the data in the :doc:`sketch_np_pixels` array. Use in conjunction with :doc:`sketch_load_np_pixels`. If you're only reading pixels from the array, there's no need to call ``update_np_pixels()`` — updating is only necessary to apply changes.

The ``update_np_pixels()`` method is similar to :doc:`sketch_update_pixels` in that ``update_np_pixels()`` must be called after modifying :doc:`sketch_np_pixels` just as :doc:`sketch_update_pixels` must be called after modifying :doc:`sketch_pixels`.

Signatures
----------

.. code:: python

    update_np_pixels() -> None
Updated on September 01, 2022 12:53:02pm UTC

