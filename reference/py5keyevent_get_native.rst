Py5KeyEvent.get_native()
========================

Retrieve native key event object.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python

    def setup():
        py5.size(200, 200, py5.P2D)
        py5.rect_mode(py5.CENTER)


    def draw():
        py5.square(py5.random(py5.width), py5.random(py5.height), 10)


    def key_pressed(e):
        native_event = e.get_native()
        if native_event != None:
            py5.println(native_event.getKeyChar())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Retrieve native key event object. The returned object will be a Java object and its type can vary based on the renderer used by the Sketch and the operating system the Sketch is run on. Sometimes the native object can be used to access functionality not otherwise available through Processing or py5.

Be aware that it is possible for the native event object to be ``None``, such as when interacting with a Sketch through :doc:`py5tools_sketch_portal`.

Underlying Processing method: getNative

Signatures
----------

.. code:: python

    get_native() -> Any

Updated on September 01, 2022 16:36:02pm UTC

