is_ready
========

Boolean value reflecting if the Sketch is in the ready state.

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

    import time

    def setup():
        py5.background(255, 0, 0)


    py5.println("the sketch is ready:", py5.is_ready)

    py5.run_sketch()

    py5.println("the sketch is running:", py5.is_running)

    py5.exit_sketch()

    # wait for exit_sketch to complete
    time.sleep(1)

    py5.println("the sketch is dead:", py5.is_dead)
    py5.println("did the sketch exit from an error?", py5.is_dead_from_error)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Boolean value reflecting if the Sketch is in the ready state. This will be ``True`` before :doc:`sketch_run_sketch` is called. It will be ``False`` while the Sketch is running and after it has exited.


Updated on September 11, 2021 16:51:34pm UTC

