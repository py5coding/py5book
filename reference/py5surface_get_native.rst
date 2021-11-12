Py5Surface.get_native()
=======================

Get the Sketch's Java native window object.

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

    py5.run_sketch(block=False)
    surface = py5.get_surface()
    native = surface.get_native()
    # output will depend on your operating system and the sketch's renderer
    py5.println(type(native))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Get the Sketch's Java native window object. Here there be dragons! The returned object will be a Java object you can interact with through py5's Python-Java bridge, jpype. The type of the native window will depend on your operating system and the Sketch's renderer, and is subject to change in future releases of Processing.

This method may be useful to you if you research the Java libraries Processing uses to display animations. Any errors will result in Java Exceptions.

Underlying Processing method: PSurface.getNative

Syntax
------

.. code:: python

    get_native() -> Any

Updated on November 12, 2021 11:30:58am UTC

