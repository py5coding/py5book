py5_tools.capture_frames()
==========================

Capture frames from a running Sketch.

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

    import py5_tools

    py5.run_sketch()
    # capture 10 frames from the currently running sketch
    frames = py5_tools.capture_frames(10, period=1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Capture frames from a running Sketch.

By default this function will return right away and will capture frames in the background while the Sketch is running. The returned list of PIL Image objects (``list[PIL.Image]``) will initially be empty, and will be populated all at once when the complete set of frames has been captured. Set the ``block`` parameter to ``True`` to instruct the method to capture the frames in the foreground and to not return until the complete list of frames is ready to be returned. To get access to the captured frames as they become available, use the :doc:`py5tools_offline_frame_processing` function instead. If the Sketch is terminated prematurely, the returned list will be empty.

By default the Sketch will be the currently running Sketch, as returned by :doc:`py5functions_get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

Syntax
------

.. code:: python

    capture_frames(count: float, *, period: float = 0.0, sketch: Sketch = None, hook_post_draw: bool = False, block: bool = False) -> list[PIL.Image]

Parameters
----------

* **block**: `bool = False` - method returns immediately (False) or blocks until function returns (True)
* **count**: `float` - number of Sketch snapshots to capture
* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **period**: `float = 0.0` - time in seconds between Sketch snapshots (default 0 means no delay)
* **sketch**: `Sketch = None` - running Sketch


Updated on March 01, 2022 12:15:01pm UTC

