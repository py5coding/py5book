Py5Graphics.sphere_detail()
===========================

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh.

Description
-----------

Controls the detail used to render a sphere by adjusting the number of vertices of the sphere mesh. The default resolution is 30, which creates a fairly detailed sphere definition with vertices every ``360/30 = 12`` degrees. If you're going to render a great number of spheres per frame, it is advised to reduce the level of detail using this function. The setting stays active until ``sphere_detail()`` is called again with a new parameter and so should *not* be called prior to every :doc:`py5graphics_sphere` statement, unless you wish to render spheres with different settings, e.g. using less detail for smaller spheres or ones further away from the camera. To control the detail of the horizontal and vertical resolution independently, use the version of the functions with two parameters.

This method is the same as :doc:`sketch_sphere_detail` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`sketch_sphere_detail`.

Underlying Processing method: PGraphics.sphereDetail

Signatures
------

.. code:: python

    sphere_detail(
        res: int,  # number of segments (minimum 3) used per full circle revolution
        /,
    ) -> None

    sphere_detail(
        ures: int,  # number of segments used longitudinally per full circle revolutoin
        vres: int,  # number of segments used latitudinally from top to bottom
        /,
    ) -> None
Updated on August 25, 2022 20:01:47pm UTC

