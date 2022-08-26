Py5Surface.resume_thread()
==========================

Resume a paused Sketch.

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

    def draw():
        py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)
        py5.println(py5.frame_count)

    py5.run_sketch(block=False)
    surface = py5.get_surface()

    # pause the sketch.
    surface.pause_thread()
    # the sketch is no longer running and there is no output

    # after waiting a bit, resume the sketch
    surface.resume_thread()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Resume a paused Sketch. The Sketch window will resume operating as it did before :doc:`py5surface_pause_thread` was called.

The :doc:`sketch_frame_count` will continue incrementing after the Sketch is resumed.

Underlying Processing method: PSurface.resumeThread

Signatures
------

.. code:: python

    resume_thread() -> None
Updated on August 25, 2022 20:01:47pm UTC

