profile_draw()
==============

Profile the execution times of the draw function with a line profiler.

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
        # this draw function should use `points` instead
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

Profile the execution times of the draw function with a line profiler. This uses the Python library lineprofiler to provide line by line performance data. The collected stats will include the number of times each line of code was executed (Hits) and the total amount of time spent on each line (Time). This information can be used to target the performance tuning efforts for a slow Sketch.

This method can be called before or after :doc:`sketch_run_sketch`. You are welcome to profile multiple functions, but don't initiate profiling on the same function multiple times. To profile functions that do not belong to the Sketch, including any functions called from :doc:`sketch_launch_thread` and the like, use lineprofiler directly and not through py5's performance tools.

To profile a other functions besides draw, use :doc:`sketch_profile_functions`. To see the results, use :doc:`sketch_print_line_profiler_stats`.

Signatures
----------

.. code:: python

    profile_draw() -> None

Updated on September 01, 2022 14:08:27pm UTC

