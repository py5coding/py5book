Py5Graphics.blend_mode()
========================

Blends the pixels in the Py5Graphics drawing surface according to a defined mode.

Description
-----------

Blends the pixels in the Py5Graphics drawing surface according to a defined mode. There is a choice of the following modes to blend the source pixels (A) with the ones of pixels already in the Py5Graphics drawing surface (B). Each pixel's final color is the result of applying one of the blend modes with each channel of (A) and (B) independently. The red channel is compared with red, green with green, and blue with blue.

* BLEND: linear interpolation of colors: ``C = A*factor + B``. This is the default.
* ADD: additive blending with white clip: ``C = min(A*factor + B, 255)``
* SUBTRACT: subtractive blending with black clip: ``C = max(B - A*factor, 0)``
* DARKEST: only the darkest color succeeds: ``C = min(A*factor, B)``
* LIGHTEST: only the lightest color succeeds: ``C = max(A*factor, B)``
* DIFFERENCE: subtract colors from underlying image.
* EXCLUSION: similar to DIFFERENCE, but less extreme.
* MULTIPLY: multiply the colors, result will always be darker.
* SCREEN: opposite multiply, uses inverse values of the colors.
* REPLACE: the pixels entirely replace the others and don't utilize alpha (transparency) values

We recommend using ``blend_mode()`` and not the previous :doc:`py5graphics_blend` function. However, unlike :doc:`py5graphics_blend`, the ``blend_mode()`` function does not support the following: ``HARD_LIGHT``, ``SOFT_LIGHT``, ``OVERLAY``, ``DODGE``, ``BURN``. On older hardware, the ``LIGHTEST``, ``DARKEST``, and ``DIFFERENCE`` modes might not be available as well.

This method is the same as :doc:`sketch_blend_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_blend_mode`.

Underlying Processing method: PGraphics.blendMode

Signatures
------

.. code:: python

    blend_mode(
        mode: int,  # the blending mode to use
        /,
    ) -> None
Updated on August 25, 2022 19:59:03pm UTC

