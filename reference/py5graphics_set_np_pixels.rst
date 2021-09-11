Py5Graphics.set_np_pixels()
===========================

Set the entire contents of :doc:`py5graphics_np_pixels` to the contents of another properly sized and typed numpy array.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_set_np_pixels_0.png
    :alt: example picture for set_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        py5.background(255, 0, 0)
        array = np.full((50, 50, 1), 240, dtype=np.uint8)
        g = py5.create_graphics(50, 50)
        g.begin_draw()
        g.set_np_pixels(array, bands='L')
        g.end_draw()
        py5.image(g, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the entire contents of :doc:`py5graphics_np_pixels` to the contents of another properly sized and typed numpy array. The size of ``array``'s first and second dimensions must match the height and width of the Py5Graphics drawing surface, respectively. The array's ``dtype`` must be ``np.uint8``. This must be used after :doc:`py5graphics_begin_draw` but can be used after :doc:`py5graphics_end_draw`.

The ``bands`` parameter is used to interpret the ``array``'s color channel dimension (the array's third dimension). It can be one of ``'L'`` (single-channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha channel, ``array`` is assumed to have no transparency. Unlike the main drawing window, a Py5Graphics drawing surface's pixels can be transparent so using the alpha channel will work properly. If the ``bands`` parameter is ``'L'``, ``array``'s third dimension is optional.

This method makes its own calls to :doc:`py5graphics_load_np_pixels` and :doc:`py5graphics_update_np_pixels` so there is no need to call either explicitly.

This method exists because setting the array contents with the code ``g.np_pixels = array`` will cause an error, while the correct syntax, ``g.np_pixels[:] = array``, might also be unintuitive for beginners.

This method is the same as :doc:`sketch_set_np_pixels` but linked to a ``Py5Graphics`` object.

Syntax
------

.. code:: python

    set_np_pixels(array: np.ndarray, bands: str = 'ARGB') -> None

Parameters
----------

* **array**: `np.ndarray` - properly sized numpy array to be copied to np_pixels[]
* **bands**: `str = 'ARGB'` - color channels in the array's third dimension


Updated on September 11, 2021 16:51:34pm UTC

