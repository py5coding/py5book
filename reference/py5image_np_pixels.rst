Py5Image.np_pixels[]
====================

The ``np_pixels[]`` array contains the values for all the pixels in the image.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_np_pixels_0.png
    :alt: example picture for np_pixels[]

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        tower = py5.load_image("tower.jpg")
        tower.load_np_pixels()
        tower.np_pixels[:, ::2, 1:] = [0, 0, 0]
        tower.update_np_pixels()
        py5.image(tower, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``np_pixels[]`` array contains the values for all the pixels in the image. Unlike the one dimensional array :doc:`py5image_pixels`, the ``np_pixels[]`` array organizes the color data in a 3 dimensional numpy array. The size of the array's dimensions are defined by the size of the image. The first dimension is the height, the second is the width, and the third represents the color channels. The color channels are ordered alpha, red, green, blue (ARGB). Every value in ``np_pixels[]`` is an integer between 0 and 255.

This numpy array is very similar to the image arrays used by other popular Python image libraries, but note that some of them like opencv will by default order the color channels as RGBA.

Much like the :doc:`py5image_pixels` array, there are load and update methods that must be called before and after making changes to the data in ``np_pixels[]``. Before accessing ``np_pixels[]``, the data must be loaded with the :doc:`py5image_load_np_pixels` method. If this is not done, ``np_pixels`` will be equal to ``None`` and your code will likely result in Python exceptions. After ``np_pixels[]`` has been modified, the :doc:`py5image_update_np_pixels` method must be called to update the content of the display window.

To set the entire contents of ``np_pixels[]`` to the contents of another equally sized numpy array, consider using :doc:`py5image_set_np_pixels`.

Updated on September 01, 2022 16:36:02pm UTC

