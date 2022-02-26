Py5Image.set_np_pixels()
========================

Set the entire contents of :doc:`py5image_np_pixels` to the contents of another properly sized and typed numpy array.

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

    import numpy as np

    def make_array(value):
        return np.full((50, 50, 1), value, dtype=np.uint8)

    def setup():
        py5.image_mode(py5.CENTER)
        global img
        img = py5.create_image(50, 50, py5.RGB)

    def draw():
        py5.background(128)
        array = make_array(py5.frame_count % 256)
        img.set_np_pixels(array, bands='L')
        py5.image(img, py5.mouse_x, py5.mouse_y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set the entire contents of :doc:`py5image_np_pixels` to the contents of another properly sized and typed numpy array. The size of ``array``'s first and second dimensions must match the height and width of the image, respectively. The array's ``dtype`` must be ``np.uint8``.

The ``bands`` parameter is used to interpret the ``array``'s color channel dimension (the array's third dimension). It can be one of ``'L'`` (single-channel grayscale), ``'ARGB'``, ``'RGB'``, or ``'RGBA'``. If there is no alpha channel, ``array`` is assumed to have no transparency. If the ``bands`` parameter is ``'L'``, ``array``'s third dimension is optional.

This method makes its own calls to :doc:`py5image_load_np_pixels` and :doc:`py5image_update_np_pixels` so there is no need to call either explicitly.

This method exists because setting the array contents with the code ``img.np_pixels = array`` will cause an error, while the correct syntax, ``img.np_pixels[:] = array``, might also be unintuitive for beginners.

Note that the :doc:`sketch_convert_image` method can also be used to convert a numpy array into a new Py5Image object.

Syntax
------

.. code:: python

    set_np_pixels(array: npt.NDArray[np.uint8], bands: str = 'ARGB') -> None

Parameters
----------

* **array**: `npt.NDArray[np.uint8]` - properly sized numpy array to be copied to np_pixels[]
* **bands**: `str = 'ARGB'` - color channels in the array's third dimension


Updated on February 26, 2022 13:22:44pm UTC

