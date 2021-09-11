Py5Graphics.image()
===================

The ``image()`` function draws an image to the Py5Graphics drawing surface.

Description
-----------

The ``image()`` function draws an image to the Py5Graphics drawing surface. Images must be in the Sketch's "data" directory to load correctly. Py5 currently works with GIF, JPEG, and PNG images. 

The ``img`` parameter specifies the image to display and by default the ``a`` and ``b`` parameters define the location of its upper-left corner. The image is displayed at its original size unless the ``c`` and ``d`` parameters specify a different size. The :doc:`py5graphics_image_mode` function can be used to change the way these parameters draw the image.

Use the ``u1``, ``u2``, ``v1``, and ``v2`` parameters to use only a subset of the image. These values are always specified in image space location, regardless of the current :doc:`py5graphics_texture_mode` setting.

The color of an image may be modified with the :doc:`py5graphics_tint` function. This function will maintain transparency for GIF and PNG images.

This method is the same as :doc:`sketch_image` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_image`.

Underlying Java method: PGraphics.image

Syntax
------

.. code:: python

    image(img: Py5Image, a: float, b: float, /) -> None
    image(img: Py5Image, a: float, b: float, c: float, d: float, /) -> None
    image(img: Py5Image, a: float, b: float, c: float, d: float, u1: int, v1: int, u2: int, v2: int, /) -> None

Parameters
----------

* **a**: `float` - x-coordinate of the image by default
* **b**: `float` - y-coordinate of the image by default
* **c**: `float` - width to display the image by default
* **d**: `float` - height to display the image by default
* **img**: `Py5Image` - the image to display
* **u1**: `int` - x-coordinate of the upper left corner of image subset
* **u2**: `int` - y-coordinate of the upper left corner of image subset
* **v1**: `int` - x-coordinate of the lower right corner of image subset
* **v2**: `int` - y-coordinate of the lower right corner of image subset


Updated on September 11, 2021 16:51:34pm UTC

