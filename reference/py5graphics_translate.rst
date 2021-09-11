Py5Graphics.translate()
=======================

Specifies an amount to displace objects within the Py5Graphics drawing surface.

Description
-----------

Specifies an amount to displace objects within the Py5Graphics drawing surface. The ``x`` parameter specifies left/right translation, the ``y`` parameter specifies up/down translation, and the ``z`` parameter specifies translations toward/away from the screen. Using this function with the ``z`` parameter requires using the ``P3D`` renderer.

Transformations are cumulative and apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as ``translate(70, 0)``. This function can be further controlled by using :doc:`py5graphics_push_matrix` and :doc:`py5graphics_pop_matrix`.

This method is the same as :doc:`sketch_translate` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_translate`.

Underlying Java method: PGraphics.translate

Syntax
------

.. code:: python

    translate(x: float, y: float, /) -> None
    translate(x: float, y: float, z: float, /) -> None

Parameters
----------

* **x**: `float` - left/right translation
* **y**: `float` - up/down translation
* **z**: `float` - forward/backward translation


Updated on September 11, 2021 16:51:34pm UTC

