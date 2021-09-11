py5_tools.animated_gif()
========================

Create an animated GIF using a running Sketch.

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
    # create a 10 frame animated GIF saved to '/tmp/animated.gif'
    py5_tools.animated_gif('/tmp/animated.gif', 10, 1, 0.5)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Create an animated GIF using a running Sketch.

By default the Sketch will be the currently running Sketch, as returned by :doc:`py5functions_get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

Syntax
------

.. code:: python

    animated_gif(filename: str, count: int, period: float, duration: float, *, loop: int = 0, optimize: bool = True, sketch: Sketch = None, hook_post_draw: bool = False) -> str

Parameters
----------

* **count**: `int` - number of Sketch snapshots to create
* **duration**: `float` - time in seconds between frames in the GIF
* **filename**: `str` - filename of GIF to create
* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **loop**: `int = 0` - number of times for the GIF to loop (default of 0 loops indefinitely)
* **optimize**: `bool = True` - optimize GIF palette
* **period**: `float` - time in seconds between Sketch snapshots
* **sketch**: `Sketch = None` - running Sketch


Updated on September 11, 2021 16:51:34pm UTC

