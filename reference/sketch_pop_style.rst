pop_style()
===========

The :doc:`sketch_push_style` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_style_0.png
    :alt: example picture for pop_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

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

.. image:: /images/reference/Sketch_pop_style_1.png
    :alt: example picture for pop_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push_style()  # start a new style
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(33, 50, 33, 33)  # left-middle circle
    
        py5.push_style()  # start another new style
        py5.stroke(0, 102, 153)
        py5.ellipse(66, 50, 33, 33)  # right-middle circle
        py5.pop_style()  # restore the previous style
    
        py5.pop_style()  # restore original style
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The :doc:`sketch_push_style` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with :doc:`sketch_push_style`, it builds on the current style information. The :doc:`sketch_push_style` and ``pop_style()`` method pairs can be nested to provide more control (see the second example for a demonstration.)

Underlying Processing method: `popStyle <https://processing.org/reference/popStyle_.html>`_

Syntax
------

.. code:: python

    pop_style() -> None

Updated on November 12, 2021 11:30:58am UTC

