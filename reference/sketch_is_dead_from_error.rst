is_dead_from_error
==================

Boolean value reflecting if the Sketch has been run and has now stopped because of an error.

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

Boolean value reflecting if the Sketch has been run and has now stopped because of an error. This will be ``True`` only when :doc:`sketch_is_dead` is ``True`` and the Sketch stopped because an exception was thrown.

Updated on September 01, 2022 16:36:02pm UTC

