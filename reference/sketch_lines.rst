lines()
=======

Draw a collection of lines to the screen.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lines_0.png
    :alt: example picture for lines()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_lines = 100 * np.random.rand(50, 4)
        py5.lines(random_lines)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Draw a collection of lines to the screen. The purpose of this method is to provide an alternative to repeatedly calling :doc:`sketch_line` in a loop. For a large number of lines, the performance of ``lines()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each line. The first few columns are for the first point of each line and the next few columns are for the second point of each line. There will be four or six columns for 2D or 3D points, respectively.

Underlying Java method: lines

Syntax
------

.. code:: python

    lines(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
----------

* **coordinates**: `NDArray[(Any, Any), Float]` - array of line coordinates


Updated on September 11, 2021 16:51:34pm UTC

