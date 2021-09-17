Py5Image
========

Datatype for storing images.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Image_0.png
    :alt: example picture for Py5Image

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global photo
        photo = py5.load_image("laDefense.jpg")


    def draw():
        py5.image(photo, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Datatype for storing images. Py5 can load ``.gif``, ``.jpg``, ``.tga``, and ``.png`` images using the :doc:`sketch_load_image` function. Py5 can also convert common Python image objects using the :doc:`sketch_convert_image` function. Images may be displayed in 2D and 3D space. The ``Py5Image`` class contains fields for the :doc:`py5image_width` and :doc:`py5image_height` of the image, as well as arrays called :doc:`py5image_pixels` and :doc:`py5image_np_pixels` that contain the values for every pixel in the image. The methods described below allow easy access to the image's pixels and alpha channel and simplify the process of compositing.

Before using the :doc:`py5image_pixels` array, be sure to use the :doc:`py5image_load_pixels` method on the image to make sure that the pixel data is properly loaded. Similarly, be sure to use the :doc:`py5image_load_np_pixels` method on the image before using the :doc:`py5image_np_pixels` array.

To create a new image, use the :doc:`sketch_create_image` function. Do not use the syntax ``Py5Image()``.

Underlying Java class: `PImage <https://processing.org/reference/PImage.html>`_

The following methods and fields are provided:

.. include:: include_py5image.rst

Updated on September 16, 2021 14:31:43pm UTC

