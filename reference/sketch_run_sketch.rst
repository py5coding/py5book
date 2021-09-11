run_sketch()
============

Run the Sketch.

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

    py5.run_sketch(block=True)
    print("this message will not be printed until after the sketch exits")

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    py5.run_sketch(block=False)
    print("this message will be printed immediately, while the sketch is running")

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # run the sketch with the window at position 400, 300 on display #1
    py5.run_sketch(block=False, py5_options=['--location=400,300', '--display=1'], sketch_args=['py5 is awesome'])
    # this will print 'py5 is awesome'
    print(py5.pargs[0])

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Run the Sketch. Code in the ``settings()``, ``setup()``, and ``draw()`` functions will be used to actualize your Sketch.

Use the ``block`` parameter to specify if the call to ``run_sketch()`` should return immediately (asynchronous Sketch execution) or block until the Sketch exits. If the ``block`` parameter is not specified, py5 will first attempt to determine if the Sketch is running in a Jupyter Notebook or an IPython shell. If it is, ``block`` will default to ``False``, and ``True`` otherwise.

Blocking is not supported on OSX. This is because of the (current) limitations of py5 on OSX. If the ``block`` parameter is set to ``True``, a warning message will appear and it will be changed to ``False``.

A list of strings passed to ``py5_options`` will be passed to the Processing PApplet class as arguments to specify characteristics such as the window's location on the screen. A list of strings passed to ``sketch_args`` will be available to a running Sketch using :doc:`sketch_pargs`. See the third example for an example of how this can be used.

When calling ``run_sketch()`` in module mode, py5 will by default search for functions such as ``setup()``,  ``draw()``, etc. in the caller's stack frame and use those in the Sketch. If for some reason that is not what you want or does not work because you are hacking py5 to do something unusual, you can use the ``sketch_functions`` parameter to pass a dictionary of the desired callable functions. The ``sketch_functions`` parameter is not available when coding py5 in class mode. Don't forget you can always replace the ``draw()`` function in a running Sketch using :doc:`sketch_hot_reload_draw`.

When programming in module mode and imported mode, py5 will inspect the ``setup()`` function and will attempt to split it into synthetic ``settings()`` and ``setup()`` functions if both were not created by the user and the real ``setup()`` function contains calls to :doc:`sketch_size`, :doc:`sketch_full_screen`, :doc:`sketch_smooth`, :doc:`sketch_no_smooth`, or :doc:`sketch_pixel_density`. Calls to those functions must be at the very beginning of ``setup()``, before any other Python code (except for comments). This feature allows the user to omit the ``settings()`` function, much like what can be done while programming in the Processing IDE. This feature is not available when programming in class mode.

When running a Sketch asynchronously through Jupyter Notebook, any ``print`` statements using Python's builtin function will always appear in the output of the currently active cell. This will rarely be desirable, as the active cell will keep changing as the user executes code elsewhere in the notebook. As an alternative, use py5's :doc:`sketch_println` method, which will place all text in the output of the cell that made the ``run_sketch()`` call. This will continue to be true if the user moves on to execute code in other Notebook cells. Use :doc:`sketch_set_println_stream` to customize this behavior. All py5 error messages and stack traces are routed through the :doc:`sketch_println` method. Be aware that some error messages and warnings generated inside the Processing Jars cannot be controlled in the same way, and may appear in the output of the active cell or mixed in with the Jupyter Kernel logs.

Syntax
------

.. code:: python

    run_sketch(block: bool = None, *, py5_options: List[str] = None, sketch_args: List[str] = None, sketch_functions: Dict[str, Callable] = None) -> None

Parameters
----------

* **block**: `bool = None` - method returns immediately (False) or blocks until Sketch exits (True)
* **py5_options**: `List[str] = None` - command line arguments to pass to Processing as arguments
* **sketch_args**: `List[str] = None` - command line arguments that become Sketch arguments
* **sketch_functions**: `Dict[str, Callable] = None` - sketch methods when using module mode


Updated on September 11, 2021 16:51:34pm UTC

