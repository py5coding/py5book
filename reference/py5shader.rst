Py5Shader
=========

This class encapsulates a GLSL shader program, including a vertex and a fragment shader.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(640, 360, py5.P2D)
        global blur
        # shaders files must be in the "data" folder to load correctly
        blur = py5.load_shader("blur.glsl")
        py5.stroke(0, 102, 153)
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.apply_filter(blur)
        py5.rect(py5.mouse_x-75, py5.mouse_y, 150, 150)
        py5.ellipse(py5.mouse_x+75, py5.mouse_y, 150, 150)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

This class encapsulates a GLSL shader program, including a vertex and a fragment shader. It's compatible with the ``P2D`` and ``P3D`` renderers, but not with the default renderer. Use the :doc:`sketch_load_shader` function to load your shader code and create ``Py5Shader`` objects.

Underlying Java class: `PShader <https://processing.org/reference/PShader.html>`_

This class provides the following methods and fields:

.. include:: include_py5shader.rst

Updated on September 11, 2021 16:51:34pm UTC

