py5_tools.save_frames()
=======================

Save a running Sketch's frames to a directory.

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
    # save the next 50 frames to the `/tmp/frames` directory
    frames = py5_tools.save_frames('/tmp/frames', limit=50, start=0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Save a running Sketch's frames to a directory.

By default the Sketch will be the currently running Sketch, as returned by :doc:`py5functions_get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If the ``limit`` parameter is used, this function will wait to return a list of the filenames. If not, it will return right away as the frames are saved in the background. It will keep doing so as long as the Sketch continues to run.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

Syntax
------

.. code:: python

    save_frames(dirname: str, *, filename: str = 'frame_####.png', period: float = 0.0, start: int = None, limit: int = 0, sketch: Sketch = None, hook_post_draw: bool = False) -> List[str]

Parameters
----------

* **dirname**: `str` - directory to save the frames
* **filename**: `str = 'frame_####.png'` - filename template to use for saved frames
* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **limit**: `int = 0` - limit the number of frames to save (default 0 means no limit)
* **period**: `float = 0.0` - time in seconds between Sketch snapshots (default 0 means no delay)
* **sketch**: `Sketch = None` - running Sketch
* **start**: `int = None` - frame starting number instead of Sketch frame_count


Updated on September 11, 2021 16:51:34pm UTC

