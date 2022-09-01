Py5Graphics.begin_camera()
==========================

The ``begin_camera()`` and :doc:`py5graphics_end_camera` functions enable advanced customization of the camera space.

Examples
--------

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_begin_camera_0.png
    :alt: example picture for begin_camera()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.size(100, 100, py5.P2D)

        g = py5.create_graphics(60, 60, py5.P3D)

        with g.begin_draw():
            g.no_fill()
            with g.begin_camera():
                g.camera()
                g.rotate_x(-py5.PI/6)
            g.translate(30, 30, 0)
            g.rotate_y(py5.PI/3)
            g.box(30)

        py5.image(g, 0, 0)
        py5.image(g, 40, 40)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

The ``begin_camera()`` and :doc:`py5graphics_end_camera` functions enable advanced customization of the camera space. The functions are useful if you want to more control over camera movement, however for most users, the :doc:`py5graphics_camera` function will be sufficient. The camera functions will replace any transformations (such as :doc:`py5graphics_rotate` or :doc:`py5graphics_translate`) that occur before them, but they will not automatically replace the camera transform itself. For this reason, camera functions should be placed right after the call to :doc:`py5graphics_begin_draw` (so that transformations happen afterwards), and the :doc:`py5graphics_camera` function can be used after ``begin_camera()`` if you want to reset the camera before applying transformations.

This function sets the matrix mode to the camera matrix so calls such as :doc:`py5graphics_translate`, :doc:`py5graphics_rotate`, :doc:`py5graphics_apply_matrix` and :doc:`py5graphics_reset_matrix` affect the camera. ``begin_camera()`` should always be used with a following :doc:`py5graphics_end_camera` and pairs of ``begin_camera()`` and :doc:`py5graphics_end_camera` cannot be nested.

This method can be used as a context manager to ensure that :doc:`py5graphics_end_camera` always gets called, as shown in the example.

This method is the same as :doc:`sketch_begin_camera` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_begin_camera`.

Underlying Processing method: PGraphics.beginCamera

Signatures
----------

.. code:: python

    begin_camera() -> None

Updated on September 01, 2022 14:08:27pm UTC

