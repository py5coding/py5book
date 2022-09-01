Py5Graphics.create_shape()
==========================

The ``create_shape()`` function is used to define a new shape.

Description
-----------

The ``create_shape()`` function is used to define a new shape. Once created, this shape can be drawn with the :doc:`py5graphics_shape` function. The basic way to use the function defines new primitive shapes. One of the following parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these different shapes are the same as their corresponding functions: :doc:`py5graphics_ellipse`, :doc:`py5graphics_rect`, :doc:`py5graphics_arc`, :doc:`py5graphics_triangle`, :doc:`py5graphics_sphere`, :doc:`py5graphics_box`, :doc:`py5graphics_quad`, and :doc:`py5graphics_line`.

Custom, unique shapes can be made by using ``create_shape()`` without a parameter. After the shape is started, the drawing attributes and geometry can be set directly to the shape within the :doc:`py5graphics_begin_shape` and :doc:`py5graphics_end_shape` methods. See reference for :doc:`py5graphics_begin_shape` for all of its options.

The  ``create_shape()`` function can also be used to make a complex shape made of other shapes. This is called a "group" and it's created by using the parameter ``GROUP`` as the first parameter.

After using ``create_shape()``, stroke and fill color can be set by calling methods like :doc:`py5shape_set_fill` and :doc:`py5shape_set_stroke`, as seen in the examples. The complete list of methods and fields for the :doc:`py5shape` class are in the py5 documentation.

This method is the same as :doc:`sketch_create_shape` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_create_shape`.

Underlying Processing method: PGraphics.createShape

Signatures
----------

.. code:: python

    create_shape() -> Py5Shape

    create_shape(
        kind: int,  # either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE
        /,
        *p: float,
    ) -> Py5Shape

    create_shape(
        type: int,  # either GROUP, PATH, or GEOMETRY
        /,
    ) -> Py5Shape

Updated on September 01, 2022 14:08:27pm UTC

