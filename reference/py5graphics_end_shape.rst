Py5Graphics.end_shape()
=======================

The ``end_shape()`` function is the companion to :doc:`py5graphics_begin_shape` and may only be called after :doc:`py5graphics_begin_shape`.

Description
-----------

The ``end_shape()`` function is the companion to :doc:`py5graphics_begin_shape` and may only be called after :doc:`py5graphics_begin_shape`. When ``end_shape()`` is called, all of image data defined since the previous call to :doc:`py5graphics_begin_shape` is written into the image buffer. The constant ``CLOSE`` as the value for the ``MODE`` parameter to close the shape (to connect the beginning and the end).

This method is the same as :doc:`sketch_end_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_end_shape`.

Underlying Processing method: PGraphics.endShape

Syntax
------

.. code:: python

    end_shape() -> None
    end_shape(mode: int, /) -> None

Parameters
----------

* **mode**: `int` - use CLOSE to close the shape


Updated on November 12, 2021 11:30:58am UTC

