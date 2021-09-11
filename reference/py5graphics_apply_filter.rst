Py5Graphics.apply_filter()
==========================

Filters the Py5Graphics drawing surface using a preset filter or with a custom shader.

Description
-----------

Filters the Py5Graphics drawing surface using a preset filter or with a custom shader. Using a shader with ``apply_filter()`` is much faster than without. Shaders require the ``P2D`` or ``P3D`` renderer in :doc:`sketch_size`.

The presets options are:

* THRESHOLD: Converts the image to black and white pixels depending if they are above or below the threshold defined by the level parameter. The parameter must be between 0.0 (black) and 1.0 (white). If no level is specified, 0.5 is used.
* GRAY: Converts any colors in the image to grayscale equivalents. No parameter is used.
* OPAQUE: Sets the alpha channel to entirely opaque. No parameter is used.
* INVERT: Sets each pixel to its inverse value. No parameter is used.
* POSTERIZE: Limits each channel of the image to the number of colors specified as the parameter. The parameter can be set to values between 2 and 255, but results are most noticeable in the lower ranges.
* BLUR: Executes a Guassian blur with the level parameter specifying the extent of the blurring. If no parameter is used, the blur is equivalent to Guassian blur of radius 1. Larger values increase the blur.
* ERODE: Reduces the light areas. No parameter is used.
* DILATE: Increases the light areas. No parameter is used.

This method is the same as :doc:`sketch_apply_filter` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_apply_filter`.

Underlying Java method: PGraphics.filter

Syntax
------

.. code:: python

    apply_filter(kind: int, /) -> None
    apply_filter(kind: int, param: float, /) -> None
    apply_filter(shader: Py5Shader, /) -> None

Parameters
----------

* **kind**: `int` - Either THRESHOLD, GRAY, OPAQUE, INVERT, POSTERIZE, BLUR, ERODE, or DILATE
* **param**: `float` - unique for each, see above
* **shader**: `Py5Shader` - the fragment shader to apply


Updated on September 11, 2021 16:51:34pm UTC

