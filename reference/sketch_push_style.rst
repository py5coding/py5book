push_style()
============

The ``push_style()`` function saves the current style settings and :doc:`sketch_pop_style` restores the prior settings.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_style_0.png
    :alt: example picture for push_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push_style()  # start a new style
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(50, 50, 33, 33)  # middle circle
        py5.pop_style()  # restore original style
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_style_1.png
    :alt: example picture for push_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        with py5.push_style():  # start a new style
            py5.stroke_weight(10)
            py5.fill(204, 153, 0)
            py5.ellipse(33, 50, 33, 33)  # left-middle circle
        
            with py5.push_style():  # start another new style
                py5.stroke(0, 102, 153)
                py5.ellipse(66, 50, 33, 33)  # right-middle circle
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``push_style()`` function saves the current style settings and :doc:`sketch_pop_style` restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with ``push_style()``, it builds on the current style information. The ``push_style()`` and :doc:`sketch_pop_style` method pairs can be nested to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: :doc:`sketch_fill`, :doc:`sketch_stroke`, :doc:`sketch_tint`, :doc:`sketch_stroke_weight`, :doc:`sketch_stroke_cap`, :doc:`sketch_stroke_join`, :doc:`sketch_image_mode`, :doc:`sketch_rect_mode`, :doc:`sketch_ellipse_mode`, :doc:`sketch_shape_mode`, :doc:`sketch_color_mode`, :doc:`sketch_text_align`, :doc:`sketch_text_font`, :doc:`sketch_text_mode`, :doc:`sketch_text_size`, :doc:`sketch_text_leading`, :doc:`sketch_emissive`, :doc:`sketch_specular`, :doc:`sketch_shininess`, and :doc:`sketch_ambient`.

This method can be used as a context manager to ensure that :doc:`sketch_pop_style` always gets called, as shown in the last example.

Underlying Processing method: `pushStyle <https://processing.org/reference/pushStyle_.html>`_

Signatures
----------

.. code:: python

    push_style() -> None

Updated on September 01, 2022 16:36:02pm UTC

