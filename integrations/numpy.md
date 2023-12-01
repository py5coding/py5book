---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Numpy, Arrays, and Images

[Numpy](https://numpy.org/) is used extensively in Python. It is the
foundation of virtually all numerical computing projects in Python.
It has a long history within the Python community, and like
[](/integrations/matplotlib), numpy's contributions to the scientific
community cannot be understated. Py5 is well positioned to be used
for numerical computing because of its close ties with numpy.

Numpy is one of py5's dependencies, so it will always installed
alongside py5.

+++

## Comparing `pixels` & `np_pixels`

In Processing and p5, direct pixel manipulation is done
with `pixels`, a one dimensional array of colors (integers).
Using this array can be a bit tedious. For example, to
change a pixel at a specific location in the Sketch window,
one must do a few calculations to find that pixel's location
in the one dimensional array.

This approach will get the job done. However, this approach
is also very different from how direct pixel manipulation is
typically done by virtually every Python program that has
access to numpy.

In the Python world, direct pixel manipulation is typically
done with a 3 dimensional array. The 3 dimensions represent
the vertical and horizontal positioning of the pixel and the
pixels's color, split into several color channels.

To provide analogous functionality, py5 offers the 3
dimensional array `np_pixels`. This is actualized in 
[](/reference/sketch_np_pixels), [](/reference/py5graphics_np_pixels),
and [](/reference/py5image_np_pixels).

Let's explore these two pixel data structures with a
simple example.

TODO: link to vectorized noise page somewhere

```{code-cell} ipython3
import numpy as np
import cv2
from PIL import Image

import py5_tools
import py5
```

```{code-cell} ipython3
# example that does something with pixels
```

```{code-cell} ipython3
# example that does the same thing with np_pixels
```

```{code-cell} ipython3

```

```{code-cell} ipython3
import time

time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

## Color Channel Ordering

The `np_pixels` array's third dimension can sometimes be tricky
to work with because you must be cognizant of where each color
channel is located. This is called color channel ordering.
Sometimes the term
"[bands](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#bands)"
will be used.

It is best to illustrate what this means for you, the py5 coder,
with a simple example.

```{code-cell} ipython3
# load an image two different ways, convert to numpy
# use create_image_from_numpy to create image, use defaults
```

TODO: Talk about why the results are wrong, bands

```{code-cell} ipython3
# new example that gets the cnannel ordering right
```

```{code-cell} ipython3
time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

## Bulk Coordinate Methods

If you are using py5 and need to create a shape with a
thousand vertices, one approach for implementing this
would involve a `for` loop that created each vertex,
one at a time.

Unfortunately, that py5 code would execute slowly.

It would execute slowly because the method call for
each individual vertex would involve a separate call
to py5's underlying Processing code.

A better approach would involve skipping the `for`
loop and creating all of the vertices with a single
command. This approach lets py5 create the vertices
in the most efficient way possible. The performance
difference between the two approaches can be significant.

```{code-cell} ipython3
# slow for loop example
```

```{code-cell} ipython3
# fast vertices example
```

```{code-cell} ipython3

```

```{code-cell} ipython3
time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

TODO: list all of the bulk commands

```{code-cell} ipython3

```
