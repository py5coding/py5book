finished
========

Boolean variable reflecting if the Sketch has stopped permanently.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    import time

    def draw():
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)


    py5.run_sketch()
    py5.println('sketch has stopped:', py5.finished)
    time.sleep(10)

    py5.exit_sketch()
    py5.println('sketch has stopped:', py5.finished)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Boolean variable reflecting if the Sketch has stopped permanently.

Underlying Processing field: finished

Updated on September 01, 2022 16:36:02pm UTC

