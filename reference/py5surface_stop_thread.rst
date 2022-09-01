Py5Surface.stop_thread()
========================

Stop the animation thread.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def draw():
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

    py5.run_sketch(block=False)
    surface = py5.get_surface()
    # this will print False
    py5.println(surface.is_stopped())

    surface.stop_thread()
    # now it will print True
    py5.println(surface.is_stopped())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Stop the animation thread. The Sketch window will remain open but will be static and unresponsive. Use :doc:`py5surface_is_stopped` to determine if a Sketch has been stopped or not.

This method is different from :doc:`py5surface_pause_thread` in that it will irreversably stop the animation. Use :doc:`py5surface_pause_thread` and :doc:`py5surface_resume_thread` if you want to pause and resume a running Sketch.

Underlying Processing method: PSurface.stopThread

Signatures
----------

.. code:: python

    stop_thread() -> bool

Updated on September 01, 2022 16:36:02pm UTC

