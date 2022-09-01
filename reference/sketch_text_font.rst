text_font()
===========

Sets the current font that will be drawn with the :doc:`sketch_text` function.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_font_0.png
    :alt: example picture for text_font()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        # the font "andalemo.ttf" must be located in the
        # current sketch's "data" directory to load successfully
        mono = py5.create_font("andalemo.ttf", 32)
        py5.background(0)
        py5.text_font(mono)
        py5.text("word", 12, 60)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Sets the current font that will be drawn with the :doc:`sketch_text` function. Fonts must be created for py5 with :doc:`sketch_create_font` or loaded with :doc:`sketch_load_font` before they can be used. The font set through ``text_font()`` will be used in all subsequent calls to the :doc:`sketch_text` function. If no ``size`` parameter is specified, the font size defaults to the original size (the size in which it was created with :doc:`py5functions_create_font_file`) overriding any previous calls to ``text_font()`` or :doc:`sketch_text_size`.

When fonts are rendered as an image texture (as is the case with the ``P2D`` and ``P3D`` renderers as well as with :doc:`sketch_load_font` and vlw files), you should create fonts at the sizes that will be used most commonly. Using ``text_font()`` without the size parameter will result in the cleanest type.

Underlying Processing method: `textFont <https://processing.org/reference/textFont_.html>`_

Signatures
----------

.. code:: python

    text_font(
        which: Py5Font,  # any variable of the type Py5Font
        /,
    ) -> None

    text_font(
        which: Py5Font,  # any variable of the type Py5Font
        size: float,  # the size of the letters in units of pixels
        /,
    ) -> None

Updated on September 01, 2022 16:36:02pm UTC

