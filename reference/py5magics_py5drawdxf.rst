%%py5drawdxf
============

Create a DXF file with py5.

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

    %%py5drawdxf 200 200 /tmp/test.dxf
    py5.translate(py5.width//2, py5.height//2)
    py5.rotate_x(0.4)
    py5.rotate_y(0.8)
    py5.box(80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create a DXF file with py5.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a Sketch with no ``draw()`` function and your code in the ``setup()`` function. It will use the ``DXF`` renderer.

As this is creating a DXF file, your code will be limited to the capabilities of that renderer. 

This magic is not available on OSX.

Code used in this cell can reference functions and variables defined in other cells because a copy of the user namespace is provided during execution. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. Mutable objects in the user namespace, however, can be altered and those changes will persist elsewhere in the notebook.

If you understand the risks, you can use the ``--unsafe`` argument so that variables and functions created in this cell are stored in the user namespace instead of a copy, making them available in other notebook cells. This may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another Sketch can result in nasty errors and bizzare consequences.

Usage
-----

.. code::

    %%py5drawdxf [--unsafe] width height filename

Arguments
---------

.. code::

    positional arguments:
      width     width of DXF output
      height    height of DXF output
      filename  filename for DXF output

    optional arguments:
      --unsafe  allow new variables to enter the user namespace

Updated on October 29, 2021 22:01:43pm UTC

