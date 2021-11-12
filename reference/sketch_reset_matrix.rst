reset_matrix()
==============

Replaces the current matrix with the identity matrix.

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
        py5.size(100, 100, py5.P3D)
        py5.no_fill()
        py5.box(80)
        py5.print_matrix()
        # prints:
        # 01.0000  00.0000  00.0000 -50.0000
        # 00.0000  01.0000  00.0000 -50.0000
        # 00.0000  00.0000  01.0000 -86.6025
        # 00.0000  00.0000  00.0000  01.0000

        py5.reset_matrix()
        py5.box(80)
        py5.print_matrix()
        # prints:
        # 1.0000  0.0000  0.0000  0.0000
        # 0.0000  1.0000  0.0000  0.0000
        # 0.0000  0.0000  1.0000  0.0000
        # 0.0000  0.0000  0.0000  1.0000

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Replaces the current matrix with the identity matrix. The equivalent function in OpenGL is ``gl_load_identity()``.

Underlying Processing method: `resetMatrix <https://processing.org/reference/resetMatrix_.html>`_

Syntax
------

.. code:: python

    reset_matrix() -> None

Updated on November 12, 2021 11:30:58am UTC

