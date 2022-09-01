Py5Graphics.hint()
==================

This function is used to enable or disable special features that control how graphics are drawn.

Description
-----------

This function is used to enable or disable special features that control how graphics are drawn. In the course of developing Processing, the developers had to make hard decisions about tradeoffs between performance and visual quality. They put significant effort into determining what makes most sense for the largest number of users, and then use functions like ``hint()`` to allow people to tune the settings for their particular Sketch. Implementing a ``hint()`` is a last resort that's used when a more elegant solution cannot be found. Some options might graduate to standard features instead of hints over time, or be added and removed between (major) releases.

Like other :doc:`py5graphics` methods, ``hint()`` can only be used between calls to :doc:`py5graphics_begin_draw` and :doc:`py5graphics_end_draw`.

Hints used by the Default Renderer
----------------------------------

* ``ENABLE_STROKE_PURE``: Fixes a problem with shapes that have a stroke and are rendered using small steps (for instance, using :doc:`py5graphics_vertex` with points that are close to one another), or are drawn at small sizes.

Hints for use with ``P2D`` and ``P3D``
--------------------------------------

* ``DISABLE_OPENGL_ERRORS``: Speeds up the ``P3D`` renderer setting by not checking for errors while running.
* ``DISABLE_TEXTURE_MIPMAPS``: Disable generation of texture mipmaps in ``P2D`` or ``P3D``. This results in lower quality - but faster - rendering of texture images when they appear smaller than their native resolutions (the mipmaps are scaled-down versions of a texture that make it look better when drawing it at a small size). However, the difference in performance is fairly minor on recent desktop video cards.


Hints for use with ``P3D`` only
-------------------------------

* ``DISABLE_DEPTH_MASK``: Disables writing into the depth buffer. This means that a shape drawn with this hint can be hidden by another shape drawn later, irrespective of their distances to the camera. Note that this is different from disabling the depth test. The depth test is still applied, as long as the ``DISABLE_DEPTH_TEST`` hint is not called, but the depth values of the objects are not recorded. This is useful when drawing a semi-transparent 3D object without depth sorting, in order to avoid visual glitches due the faces of the object being at different distances from the camera, but still having the object properly occluded by the rest of the objects in the scene.
* ``ENABLE_DEPTH_SORT``: Enable primitive z-sorting of triangles and lines in ``P3D``. This can slow performance considerably, and the algorithm is not yet perfect.
* ``DISABLE_DEPTH_TEST``: Disable the zbuffer, allowing you to draw on top of everything at will. When depth testing is disabled, items will be drawn to the screen sequentially, like a painting. This hint is most often used to draw in 3D, then draw in 2D on top of it (for instance, to draw GUI controls in 2D on top of a 3D interface). When called, this will also clear the depth buffer. Restore the default with ``hint(ENABLE_DEPTH_TEST)``, but note that with the depth buffer cleared, any 3D drawing that happens later in will ignore existing shapes on the screen.
* ``DISABLE_OPTIMIZED_STROKE``: Forces the ``P3D`` renderer to draw each shape (including its strokes) separately, instead of batching them into larger groups for better performance. One consequence of this is that 2D items drawn with ``P3D`` are correctly stacked on the screen, depending on the order in which they were drawn. Otherwise, glitches such as the stroke lines being drawn on top of the interior of all the shapes will occur. However, this hint can make rendering substantially slower, so it is recommended to use it only when drawing a small amount of shapes. For drawing two-dimensional scenes, use the ``P2D`` renderer instead, which doesn't need the hint to properly stack shapes and their strokes.
* ``ENABLE_STROKE_PERSPECTIVE``: Enables stroke geometry (lines and points) to be affected by the perspective, meaning that they will look smaller as they move away from the camera.

This method is the same as :doc:`sketch_hint` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_hint`.

Underlying Processing method: PGraphics.hint

Signatures
----------

.. code:: python

    hint(
        which: int,  # hint to use when rendering Sketch
        /,
    ) -> None
Updated on September 01, 2022 12:53:02pm UTC

