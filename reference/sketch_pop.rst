pop()
=====

The ``pop()`` function restores the previous drawing style settings and transformations after :doc:`sketch_push` has changed them.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_0.png
    :alt: example picture for pop()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.fill(255)
        py5.rect(0, 0, 50, 50)  # white rectangle
    
        py5.push()
        py5.translate(30, 20)
        py5.fill(0)
        py5.rect(0, 0, 50, 50)  # black rectangle
        py5.pop()  # restore original settings
    
        py5.fill(100)
        py5.rect(15, 10, 50, 50)  # gray rectangle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_1.png
    :alt: example picture for pop()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push()
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(50, 50, 33, 33)  # middle circle
        py5.pop()  # restore original settings
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``pop()`` function restores the previous drawing style settings and transformations after :doc:`sketch_push` has changed them. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with :doc:`sketch_push`, it builds on the current style and transform information.

:doc:`sketch_push` stores information related to the current transformation state and style settings controlled by the following functions: :doc:`sketch_rotate`, :doc:`sketch_translate`, :doc:`sketch_scale`, :doc:`sketch_fill`, :doc:`sketch_stroke`, :doc:`sketch_tint`, :doc:`sketch_stroke_weight`, :doc:`sketch_stroke_cap`, :doc:`sketch_stroke_join`, :doc:`sketch_image_mode`, :doc:`sketch_rect_mode`, :doc:`sketch_ellipse_mode`, :doc:`sketch_color_mode`, :doc:`sketch_text_align`, :doc:`sketch_text_font`, :doc:`sketch_text_mode`, :doc:`sketch_text_size`, and :doc:`sketch_text_leading`.

The :doc:`sketch_push` and ``pop()`` functions can be used in place of :doc:`sketch_push_matrix`, :doc:`sketch_pop_matrix`, ``push_styles()``, and ``pop_styles()``. The difference is that :doc:`sketch_push` and ``pop()`` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

Underlying Java method: `pop <https://processing.org/reference/pop_.html>`_

Syntax
------

.. code:: python

    pop() -> None

Updated on September 11, 2021 16:51:34pm UTC

