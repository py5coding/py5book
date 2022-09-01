text_align()
============

Sets the current alignment for drawing text.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_align_0.png
    :alt: example picture for text_align()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.background(0)
        py5.text_size(16)
        py5.text_align(py5.RIGHT)
        py5.text("ABCD", 50, 30)
        py5.text_align(py5.CENTER)
        py5.text("EFGH", 50, 50)
        py5.text_align(py5.LEFT)
        py5.text("IJKL", 50, 70)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_align_1.png
    :alt: example picture for text_align()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.background(0)
        py5.stroke(153)
        py5.text_size(11)
        py5.text_align(py5.CENTER, py5.BOTTOM)
        py5.line(0, 30, py5.width, 30)
        py5.text("CENTER,BOTTOM", 50, 30)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.line(0, 50, py5.width, 50)
        py5.text("CENTER,CENTER", 50, 50)
        py5.text_align(py5.CENTER, py5.TOP)
        py5.line(0, 70, py5.width, 70)
        py5.text("CENTER,TOP", 50, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the current alignment for drawing text. The parameters ``LEFT``, ``CENTER``, and ``RIGHT`` set the display characteristics of the letters in relation to the values for the ``x`` and ``y`` parameters of the :doc:`sketch_text` function.
 
An optional second parameter can be used to vertically align the text. ``BASELINE`` is the default, and the vertical alignment will be reset to ``BASELINE`` if the second parameter is not used. The ``TOP`` and ``CENTER`` parameters are straightforward. The ``BOTTOM`` parameter offsets the line based on the current :doc:`sketch_text_descent`. For multiple lines, the final line will be aligned to the bottom, with the previous lines appearing above it.
 
When using :doc:`sketch_text` with width and height parameters, ``BASELINE`` is ignored, and treated as ``TOP``. (Otherwise, text would by default draw outside the box, since ``BASELINE`` is the default setting. ``BASELINE`` is not a useful drawing mode for text drawn in a rectangle.)
 
The vertical alignment is based on the value of :doc:`sketch_text_ascent`, which many fonts do not specify correctly. It may be necessary to use a hack and offset by a few pixels by hand so that the offset looks correct. To do this as less of a hack, use some percentage of :doc:`sketch_text_ascent` or :doc:`sketch_text_descent` so that the hack works even if you change the size of the font.

Underlying Processing method: `textAlign <https://processing.org/reference/textAlign_.html>`_

Signatures
----------

.. code:: python

    text_align(
        align_x: int,  # horizontal alignment, either LEFT, CENTER, or RIGHT
        /,
    ) -> None

    text_align(
        align_x: int,  # horizontal alignment, either LEFT, CENTER, or RIGHT
        align_y: int,  # vertical alignment, either TOP, BOTTOM, CENTER, or BASELINE
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

