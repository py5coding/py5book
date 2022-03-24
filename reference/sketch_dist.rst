dist()
======

Calculates the distance between two points.

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

    # Sets the background gray value based on the distance 
    # of the mouse from the center of the screen
    def draw():
      py5.no_stroke()
      d = py5.dist(py5.width/2, py5.height/2, py5.mouse_x, py5.mouse_y)
      max_dist = py5.dist(0, 0, py5.width/2, py5.height/2)
      gray = py5.remap(d, 0, max_dist, 0, 255)
      py5.fill(gray)
      py5.rect(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
-----------

Calculates the distance between two points.

Syntax
------

.. code:: python

    dist(x1: Union[float, npt.NDArray], y1: Union[float, npt.NDArray], x2: Union[float, npt.NDArray], y2: Union[float, npt.NDArray], /) -> Union[float, npt.NDArray]
    dist(x1: Union[float, npt.NDArray], y1: Union[float, npt.NDArray], z1: Union[float, npt.NDArray], x2: Union[float, npt.NDArray], y2: Union[float, npt.NDArray], z2: Union[float, npt.NDArray], /) -> Union[float, npt.NDArray]

Parameters
----------

* **x1**: `Union[float, npt.NDArray]` - x-coordinate of the first point
* **x2**: `Union[float, npt.NDArray]` - x-coordinate of the second point
* **y1**: `Union[float, npt.NDArray]` - y-coordinate of the first point
* **y2**: `Union[float, npt.NDArray]` - y-coordinate of the second point
* **z1**: `Union[float, npt.NDArray]` - z-coordinate of the first point
* **z2**: `Union[float, npt.NDArray]` - z-coordinate of the second point


Updated on February 26, 2022 13:22:44pm UTC

