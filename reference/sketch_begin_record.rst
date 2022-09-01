begin_record()
==============

Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window.

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
        py5.size(400, 400)
        py5.begin_record(py5.PDF, "everything.pdf")


    def draw():
        py5.ellipse(py5.mouse_x, py5.mouse_y, 10, 10)


    def mouse_pressed():
        py5.end_record()
        py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(200, 200)

        with py5.begin_record(py5.SVG, "/tmp/test.svg") as r:
            py5.rect_mode(py5.CENTER)
            r.fill("#F00")  # affects the recorded output only

            for _ in range(10):
                py5.square(py5.random(py5.width), py5.random(py5.height), 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window. The ``begin_record()`` function requires two parameters, the first is the renderer and the second is the file name. This function is always used with :doc:`sketch_end_record` to stop the recording process and close the file.

Note that ``begin_record()`` will only pick up any settings that happen after it has been called. For instance, if you call :doc:`sketch_text_font` before ``begin_record()``, then that font will not be set for the file that you're recording to.

``begin_record()`` works only with the ``PDF`` and ``SVG`` renderers.

This method can be used as a context manager to ensure that :doc:`sketch_end_record` always gets called, as shown in the last example.

Underlying Processing method: `beginRecord <https://processing.org/reference/beginRecord_.html>`_

Signatures
----------

.. code:: python

    begin_record(
        recorder: Py5Graphics,  # Py5Graphics object to record drawing commands to
        /,
    ) -> None

    begin_record(
        renderer: str,  # PDF or SVG
        filename: str,  # filename for output
        /,
    ) -> Py5Graphics
Updated on September 01, 2022 12:53:02pm UTC

