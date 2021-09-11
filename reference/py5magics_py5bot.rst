%%py5bot
========

Create a PNG image using py5bot and embed the result in the notebook.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Magics_py5bot_0.png
    :alt: example picture for %%py5bot

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    %%py5bot
    size(100, 100)
    background(128)
    fill(255, 0, 0)
    rect(40, 50, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create a PNG image using py5bot and embed the result in the notebook.

This cell magic uses the same rendering mechanism as the py5bot kernel. For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed as a static Sketch with no ``draw()`` function and your code in the ``setup()`` function. The first line in the cell should be a call to :doc:`sketch_size`.

This magic is similar to :doc:`py5magics_py5draw` in that both can be used to create a static Sketch. One key difference is that ``%%py5bot`` requires the user to begin the code with a call to :doc:`sketch_size`, while :doc:`py5magics_py5draw` calls :doc:`sketch_size` for you based on the magic's arguments. 

This magic supports the default renderer and the ``P2D`` and ``P3D`` renderers. Note that both of the OpenGL renderers will briefly open a window on your screen. This magic is only available when using the py5 kernel and coding in imported mode. The ``P2D`` and ``P3D`` renderers are not available when the py5 kernel is hosted on an OSX computer.

Code used in this cell can reference functions and variables defined in other cells. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. If you understand the risks, you can use the ``global`` keyword to add a single function or variable to the notebook namespace.

Usage
-----

.. code::

    %%py5bot [-f FILENAME] [-v VARIABLE]

Arguments
---------

.. code::

    optional arguments:
      -f FILENAME, --filename FILENAME
                            save image to file
      -v VARIABLE, --var VARIABLE
                            assign image to variable

Updated on September 11, 2021 16:51:34pm UTC

