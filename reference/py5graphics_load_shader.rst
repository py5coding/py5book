Py5Graphics.load_shader()
=========================

Loads a shader into a ``Py5Shader`` object.

Description
-----------

Loads a shader into a ``Py5Shader`` object. The shader file must be located in the Sketch's "data" directory to load correctly. Shaders are compatible with the ``P2D`` and ``P3D`` renderers, but not with the default renderer.

Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the ``None`` value may cause an error if your code does not check whether the value returned is ``None``.

This method is the same as :doc:`sketch_load_shader` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_load_shader`.

Underlying Processing method: PGraphics.loadShader

Signatures
----------

.. code:: python

    load_shader(
        frag_filename: str,  # name of fragment shader file
        /,
    ) -> Py5Shader

    load_shader(
        frag_filename: str,  # name of fragment shader file
        vert_filename: str,  # name of vertex shader file
        /,
    ) -> Py5Shader
Updated on September 01, 2022 12:53:02pm UTC

