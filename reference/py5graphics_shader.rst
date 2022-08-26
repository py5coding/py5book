Py5Graphics.shader()
====================

Applies the shader specified by the parameters.

Description
-----------

Applies the shader specified by the parameters. It's compatible with the ``P2D`` and ``P3D`` renderers, but not with the default renderer.

This method is the same as :doc:`sketch_shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_shader`.

Underlying Processing method: PGraphics.shader

Signatures
------

.. code:: python

    shader(
        shader: Py5Shader,  # name of shader file
        /,
    ) -> None

    shader(
        shader: Py5Shader,  # name of shader file
        kind: int,  # type of shader, either POINTS, LINES, or TRIANGLES
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

