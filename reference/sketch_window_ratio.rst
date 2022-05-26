window_ratio()
==============

Set a window ratio to enable scale invariant drawing.

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

    def setup():
      py5.window_resizable(True)
      py5.window_ratio(1280, 720)

      py5.cursor(py5.CROSS)
      py5.stroke_weight(10)


    def draw():
      py5.background(255, 0, 0)
      py5.fill(255)
      py5.rect(0, 0, py5.rwidth, py5.rheight)

      py5.fill(0)
      py5.text_align(py5.CENTER, py5.CENTER)
      x, y = py5.rwidth / 2, py5.rheight / 2
      py5.text_size(200)
      py5.text(f'{py5.rmouse_x}, {py5.rmouse_y}', x, y - 100)
      py5.text_size(100)
      py5.text(f'top={int(py5.ratio_top)} left={int(py5.ratio_left)}', x, y + 100)
      py5.text(f'scale={round(py5.ratio_scale, 3)}', x, y + 200)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Set a window ratio to enable scale invariant drawing. If the Sketch window is resizable, drawing in a consistent way can be challenging as the window changes size. This method activates some transformations to let the user draw to the window in a way that will be consistent for all window sizes.

The usefulness of this feature is demonstrated in the example code. The size of the text will change as the window changes size. Observe the example makes two calls to :doc:`sketch_text_size` with fixed values of ``200`` and ``100``. Without this feature, calculating the appropriate text size for all window sizes would be difficult. Similarly, positioning the text in the same relative location would also involve several calculations. Using ``window_ratio()`` makes resizable Sketches that resize well easier to create.

When using this feature, use :doc:`sketch_rmouse_x` and :doc:`sketch_rmouse_y` to get the cursor coordinates. The transformations involve calls to :doc:`sketch_translate` and :doc:`sketch_scale`, and the parameters to those methods can be accessed with :doc:`sketch_ratio_top`, :doc:`sketch_ratio_left`, and :doc:`sketch_ratio_scale`. The transformed coordinates enabled with this feature can be negative for the top and left areas of the window that do not fit the desired aspect ratio. Experimenting with the example and seeing how the numbers change will provide more understanding than what can be explained with words.

When calling this method, it is better to do so with values like ``window_ratio(1280, 720)`` and not ``window_ratio(16, 9)``. The aspect ratio is the same for both but the latter might result in floating point accuracy issues.

Underlying Processing method: windowRatio

Syntax
------

.. code:: python

    window_ratio(wide: int, high: int, /) -> None

Parameters
----------

* **high**: `int` - height of scale invariant display window
* **wide**: `int` - width of scale invariant display window


Updated on May 02, 2022 12:07:22pm UTC

