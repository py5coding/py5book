print_line_profiler_stats()
===========================

Print the line profiler stats initiated with :doc:`sketch_profile_draw` or :doc:`sketch_profile_functions`.

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


    def draw():
        py5.stroke(py5.random_int(255), py5.random_int(255), py5.random_int(255))
        # this should use `points` instead
        for _ in range(100):
            py5.point(py5.random_int(py5.width), py5.random_int(py5.height))


    py5.profile_draw()
    py5.run_sketch()


    # let the sketch run for a bit to accumulate data
    time.sleep(10)

    py5.print_line_profiler_stats()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Print the line profiler stats initiated with :doc:`sketch_profile_draw` or :doc:`sketch_profile_functions`. The collected stats will include the number of times each line of code was executed (Hits) and the total amount of time spent on each line (Time). This information can be used to target the performance tuning efforts for a slow Sketch.

This method can be called multiple times on a running Sketch.

Signatures
------

.. code:: python

    print_line_profiler_stats() -> None
Updated on August 25, 2022 20:01:47pm UTC

