print_camera()
==============

Prints the current camera matrix to standard output.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(100, 100, py5.P3D)
        py5.print_camera()

        # the program above prints this data:
        # 01.0000  00.0000  00.0000 -50.0000
        # 00.0000  01.0000  00.0000 -50.0000
        # 00.0000  00.0000  01.0000 -86.6025
        # 00.0000  00.0000  00.0000  01.0000

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Prints the current camera matrix to standard output.

Underlying Processing method: `printCamera <https://processing.org/reference/printCamera_.html>`_

Signatures
----------

.. code:: python

    print_camera() -> None

Updated on September 01, 2022 16:36:02pm UTC

