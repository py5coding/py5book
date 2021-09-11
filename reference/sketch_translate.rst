translate()
===========

Specifies an amount to displace objects within the display window.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_translate_0.png
    :alt: example picture for translate()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.translate(30, 20)
        py5.rect(0, 0, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_translate_1.png
    :alt: example picture for translate()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P3D)
        # translating in 3D requires P3D
        # as the parameter to size()
        # translate 30 across, 20 down, and
        # 50 back, or "away" from_ the screen.
        py5.translate(30, 20, -50)
        py5.rect(0, 0, 55, 55)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_translate_2.png
    :alt: example picture for translate()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.rect(0, 0, 55, 55)  # draw rect at original 0,0
        py5.translate(30, 20)
        py5.rect(0, 0, 55, 55)  # draw rect at new 0,0
        py5.translate(14, 14)
        py5.rect(0, 0, 55, 55)  # draw rect at new 0,0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Specifies an amount to displace objects within the display window. The ``x`` parameter specifies left/right translation, the ``y`` parameter specifies up/down translation, and the ``z`` parameter specifies translations toward/away from the screen. Using this function with the ``z`` parameter requires using ``P3D`` as a parameter in combination with size as shown in the second example.

Transformations are cumulative and apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling ``translate(50, 0)`` and then ``translate(20, 0)`` is the same as ``translate(70, 0)``. If ``translate()`` is called within ``draw()``, the transformation is reset when the loop begins again. This function can be further controlled by using :doc:`sketch_push_matrix` and :doc:`sketch_pop_matrix`.

Underlying Java method: `translate <https://processing.org/reference/translate_.html>`_

Syntax
------

.. code:: python

    translate(x: float, y: float, /) -> None
    translate(x: float, y: float, z: float, /) -> None

Parameters
----------

* **x**: `float` - left/right translation
* **y**: `float` - up/down translation
* **z**: `float` - forward/backward translation


Updated on September 11, 2021 16:51:34pm UTC

