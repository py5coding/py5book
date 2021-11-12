Py5Graphics.reset_shader()
==========================

Restores the default shaders.

Description
-----------

Restores the default shaders. Code that runs after ``reset_shader()`` will not be affected by previously defined shaders.

This method is the same as :doc:`sketch_reset_shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_reset_shader`.

Underlying Processing method: PGraphics.resetShader

Syntax
------

.. code:: python

    reset_shader() -> None
    reset_shader(kind: int, /) -> None

Parameters
----------

* **kind**: `int` - type of shader, either POINTS, LINES, or TRIANGLES


Updated on November 12, 2021 11:30:58am UTC

