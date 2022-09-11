frame_count
===========

The system variable ``frame_count`` contains the number of frames that have been displayed since the program started.

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
        py5.frame_rate(30)


    def draw():
        py5.line(0, 0, py5.width, py5.height)
        py5.println(py5.frame_count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The system variable ``frame_count`` contains the number of frames that have been displayed since the program started. Inside ``setup()`` the value is 0. Inside the first execution of ``draw()`` it is 1, and it will increase by 1 for every execution of ``draw()`` after that.

Underlying Processing field: `frameCount <https://processing.org/reference/frameCount.html>`_

Updated on September 01, 2022 16:36:02pm UTC

