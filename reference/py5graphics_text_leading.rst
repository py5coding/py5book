Py5Graphics.text_leading()
==========================

Sets the spacing between lines of text in units of pixels.

Description
-----------

Sets the spacing between lines of text in units of pixels. This setting will be used in all subsequent calls to the :doc:`py5graphics_text` function.  Note, however, that the leading is reset by :doc:`py5graphics_text_size`. For example, if the leading is set to 20 with ``text_leading(20)``, then if ``text_size(48)`` is run at a later point, the leading will be reset to the default for the text size of 48.

This method is the same as :doc:`sketch_text_leading` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_text_leading`.

Underlying Processing method: PGraphics.textLeading

Signatures
------

.. code:: python

    text_leading(
        leading: float,  # the size in pixels for spacing between lines
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

