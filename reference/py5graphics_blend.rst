Py5Graphics.blend()
===================

Blends a region of pixels from one image into another (or in itself again) with full alpha channel support.

Description
-----------

Blends a region of pixels from one image into another (or in itself again) with full alpha channel support. There is a choice of the following modes to blend the source pixels (A) with the ones of pixels in the destination image (B):

* BLEND: linear interpolation of colors: ``C = A*factor + B``
* ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
* SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
* DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
* LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
* DIFFERENCE: subtract colors from underlying image.
* EXCLUSION: similar to DIFFERENCE, but less extreme.
* MULTIPLY: Multiply the colors, result will always be darker.
* SCREEN: Opposite multiply, uses inverse values of the colors.
* OVERLAY: A mix of MULTIPLY and SCREEN. Multiplies dark values, and screens light values.
* HARD_LIGHT: SCREEN when greater than 50% gray, MULTIPLY when lower.
* SOFT_LIGHT: Mix of DARKEST and LIGHTEST.  Works like OVERLAY, but not as harsh.
* DODGE: Lightens light tones and increases contrast, ignores darks. Called "Color Dodge" in Illustrator and Photoshop.
* BURN: Darker areas are applied, increasing contrast, ignores lights. Called "Color Burn" in Illustrator and Photoshop.

All modes use the alpha information (highest byte) of source image pixels as the blending factor. If the source and destination regions are different sizes, the image will be automatically resized to match the destination size. If the ``src`` parameter is not used, the Py5Graphics drawing surface is used as the source image.

This function ignores :doc:`py5graphics_image_mode`.

This method is the same as :doc:`sketch_blend` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_blend`.

Underlying Java method: PGraphics.blend

Syntax
------

.. code:: python

    blend(src: Py5Image, sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None
    blend(sx: int, sy: int, sw: int, sh: int, dx: int, dy: int, dw: int, dh: int, mode: int, /) -> None

Parameters
----------

* **dh**: `int` - destination image height
* **dw**: `int` - destination image width
* **dx**: `int` - x-coordinate of the destinations's upper left corner
* **dy**: `int` - y-coordinate of the destinations's upper left corner
* **mode**: `int` - Either BLEND, ADD, SUBTRACT, LIGHTEST, DARKEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, BURN
* **sh**: `int` - source image height
* **src**: `Py5Image` - an image variable referring to the source image
* **sw**: `int` - source image width
* **sx**: `int` - x-coordinate of the source's upper left corner
* **sy**: `int` - y-coordinate of the source's upper left corner


Updated on September 11, 2021 16:51:34pm UTC

