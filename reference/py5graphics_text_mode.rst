Py5Graphics.text_mode()
=======================

Sets the way text draws to the Py5Graphics drawing surface, either as texture maps or as vector geometry.

Description
-----------

Sets the way text draws to the Py5Graphics drawing surface, either as texture maps or as vector geometry. The default ``text_mode(MODEL)``, uses textures to render the fonts. The ``text_mode(SHAPE)`` mode draws text using the glyph outlines of individual characters rather than as textures. This mode is only supported with the ``PDF`` and ``P3D`` renderer settings. With the ``PDF`` renderer, you must call ``text_mode(SHAPE)`` before any other drawing occurs. If the outlines are not available, then ``text_mode(SHAPE)`` will be ignored and ``text_mode(MODEL)`` will be used instead.

The ``text_mode(SHAPE)`` option in ``P3D`` can be combined with :doc:`py5graphics_begin_raw` to write vector-accurate text to 2D and 3D output files, for instance ``DXF`` or ``PDF``. The ``SHAPE`` mode is not currently optimized for ``P3D``, so if recording shape data, use ``text_mode(MODEL)`` until you're ready to capture the geometry with :doc:`py5graphics_begin_raw`.

This method is the same as :doc:`sketch_text_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_text_mode`.

Underlying Processing method: PGraphics.textMode

Signatures
------

.. code:: python

    text_mode(
        mode: int,  # either MODEL or SHAPE
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

