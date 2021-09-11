Py5Graphics.background()
========================

The ``background()`` function sets the color used for the background of the ``Py5Graphics`` object.

Description
-----------

The ``background()`` function sets the color used for the background of the ``Py5Graphics`` object. The default background is 100% transparent.
 
An image can also be used as the background, although the image's width and height must match that of the ``Py5Graphics`` object. Images used with ``background()`` will ignore the current :doc:`py5graphics_tint` setting. To resize an image to the size of the ``Py5Graphics`` object, use ``image.resize(width, height)``.
 
This method is the same as :doc:`sketch_background` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_background`.

Underlying Java method: PGraphics.background

Syntax
------

.. code:: python

    background(gray: float, /) -> None
    background(gray: float, alpha: float, /) -> None
    background(image: Py5Image, /) -> None
    background(rgb: int, /) -> None
    background(rgb: int, alpha: float, /) -> None
    background(v1: float, v2: float, v3: float, /) -> None
    background(v1: float, v2: float, v3: float, alpha: float, /) -> None

Parameters
----------

* **alpha**: `float` - opacity of the background
* **gray**: `float` - specifies a value between white and black
* **image**: `Py5Image` - Py5Image to set as background (must be same size as the Sketch window)
* **rgb**: `int` - any value of the color datatype
* **v1**: `float` - red or hue value (depending on the current color mode)
* **v2**: `float` - green or saturation value (depending on the current color mode)
* **v3**: `float` - blue or brightness value (depending on the current color mode)


Updated on September 11, 2021 16:51:34pm UTC

