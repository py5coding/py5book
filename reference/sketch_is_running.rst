is_running
==========

Boolean value reflecting if the Sketch is in the running state.

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


    print("the sketch is ready:", py5.is_ready)

    py5.run_sketch()

    print("the sketch is running:", py5.is_running)

    py5.exit_sketch()

    # wait for exit_sketch to complete
    time.sleep(1)

    print("the sketch is dead:", py5.is_dead)
    print("did the sketch exit from an error?", py5.is_dead_from_error)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Boolean value reflecting if the Sketch is in the running state. This will be ``False`` before :doc:`sketch_run_sketch` is called and ``True`` after. It will be ``False`` again after the Sketch has exited.

Updated on August 25, 2022 20:01:47pm UTC

