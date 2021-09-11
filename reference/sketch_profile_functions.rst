profile_functions()
===================

Profile the execution times of the Sketch's functions with a line profiler.

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
        # to load images from the web, use `request_image` instead
        img = py5.load_image('http://py5.ixora.io/images/examples/apples.jpg')
        py5.image_mode(py5.CORNERS)
        py5.image(img, 10, 10, py5.width - 10, py5.height - 10)


    py5.profile_functions(['setup'])
    py5.run_sketch()

    time.sleep(5)
    py5.print_line_profiler_stats()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Profile the execution times of the Sketch's functions with a line profiler. This uses the Python library lineprofiler to provide line by line performance data. The collected stats will include the number of times each line of code was executed (Hits) and the total amount of time spent on each line (Time). This information can be used to target the performance tuning efforts for a slow Sketch.

This method can be called before or after :doc:`sketch_run_sketch`. You are welcome to profile multiple functions, but don't initiate profiling on the same function multiple times. To profile functions that do not belong to the Sketch, including any functions called from :doc:`sketch_launch_thread` and the like, use lineprofiler directly and not through py5's performance tools.

To profile just the draw function, you can also use :doc:`sketch_profile_draw`. To see the results, use :doc:`sketch_print_line_profiler_stats`.

Syntax
------

.. code:: python

    profile_functions(function_names: List[str]) -> None

Parameters
----------

* **function_names**: `List[str]` - names of py5 functions to be profiled


Updated on September 11, 2021 16:51:34pm UTC

