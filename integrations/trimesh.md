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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# 3D Shapes and Trimesh

[Trimesh](https://trimesh.org/) is a well-known and well-maintained library for working with 3D geometry.

The goal of Trimesh is to "provide a full featured and well tested Trimesh object which allows for easy manipulation and analysis, in the style of the Polygon object in the Shapely library."

Trimesh and [](/reference/sketch_convert_shape) can greatly extend py5's ability to load 3D objects, far exceeding what can be achieved with [](/reference/sketch_load_shape).

Finally, know that Trimesh is a large and complex library. It is possible (likely) that there are Trimesh features that don't work well with py5's [](/reference/sketch_convert_shape) method. If you find something that doesn't work but should or have ideas for how py5's Trimesh integrations can be improved, please let us know by [opening an issue](https://github.com/py5coding/py5generator/issues) or starting a thread in [GitHub Discussions](https://github.com/py5coding/py5generator/discussions).

## Setup

Installing Trimesh by itself is acceptable but Trimesh is much more useful if you install its dependent libraries. At a minimum, you should install the easy to install dependencies with this command:

```bash
pip install trimesh[easy]
```

Refer to the [Trimesh Installation page](https://trimesh.org/install.html) for more information about Trimesh's dependencies and installation options.

Development of py5's integration code was done with Trimesh version 3.23. Version 4.0 was released shortly after but seems to work just as well as 3.23.

Installing [OpenSCAD](https://openscad.org/) or [Blender](https://www.blender.org/) on your computer may also be useful. Trimesh can use these to perform boolean operations on 3D objects.

If Trimesh is missing a dependent library needed for the functionality you want to use, it will provide you with an error message informing you of what you should install.

## Convert `trimesh.Scene` objects to Py5Shapely objects

Let's start by importing the Trimesh library and some classes we will use later.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import py5_tools
import py5

import trimesh
from trimesh.path import Path2D, Path3D
from trimesh.primitives import Box, Capsule, Cylinder, Sphere
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

For our first example, we will use a 3D model file downloaded from [TurboSquid](https://www.turbosquid.com/). Our example is a
[strawberry](https://www.turbosquid.com/3d-models/3d-strawberry-1962030) created by the artist [minimoku](https://www.turbosquid.com/Search/Artists/minimoku).

Loading a complex 3D model in Trimesh may be slow. Don't load a model from within a Sketch unless absolutely necessary.  If you need to do this, load it once in `setup()`.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
strawberry_model = trimesh.load('models/Strawberry_gltf.gltf')

print(type(strawberry_model))
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

A [trimesh.Scene](https://trimesh.org/trimesh.html#trimesh.Scene) object can contain one or more [trimesh.Trimesh](https://trimesh.org/trimesh.html#trimesh.Trimesh) objects. Both work equally well here.

We can use the [](/reference/sketch_convert_shape) method to effortlessly convert this model into a `Py5Shape` object.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    global strawberry
    py5.size(300, 500, py5.P3D)
    strawberry = py5.convert_shape(strawberry_model)
    assert isinstance(strawberry, py5.Py5Shape)

    # increase the model's scale and change its orientation
    strawberry.scale(50)
    strawberry.rotate_z(-py5.radians(90))
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

After converting the model into a `Py5Shape` object, we need to increase the scale and rotate it to change its orientation. Consider py5's coordinate system: the positive Y axis points towards the bottom of the drawing surface. It is likely that the 3D modeling program used to create this strawberry had a different coordinate system, perhaps with the positive Z axis pointing towards the top of the screen. Therefore, when using this model in py5 you may need to do some rotations to get the result you want. Similarly, the scale may need to be some adjustments.

When loading a model, you will often want to apply some transformations so it can be drawn as you intend for it to be drawn. These adjustments can be done after converting the model into a `Py5Shape` object, as we did here in our `setup()` function. Alternatively, we can do the adjustments in the `draw()` function before the drawing the `Py5Shape` object to the screen with [](/reference/sketch_shape).

You can also adjust the Trimesh mesh object using Trimesh's transformation tools, before the call to [](/reference/sketch_convert_shape). You will use Trimesh's [apply_transform()](https://trimesh.org/trimesh.html#trimesh.Trimesh.apply_transform) method to apply a transformation matrix to a mesh.

Now let's create a `draw()` method to draw the `Py5Shape` object with the [](/reference/sketch_shape) method.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
y_rot = 0


def draw():
    global y_rot
    y_rot += 1

    py5.background(255)
    py5.ambient_light(64, 64, 64)
    py5.directional_light(220, 220, 220, 0, -1, -1)

    py5.translate(225, 400, 0)

    py5.rotate_z(py5.radians(-25))
    py5.rotate_x(py5.radians(-25))
    py5.rotate_y(py5.radians(y_rot))

    py5.shape(strawberry)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

We need to invert the model's y axis because the top of the strawberry is oriented towards the positive y axis but Processing and therefore py5 has the positive y axis pointing towards the bottom of the drawing surface. You will frequently need to employ rotations and scale adjustments when working with models created outside of py5.

When we run this, the strawberry will slowly rotate along its main axis.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.run_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The result looks like this:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
import time

time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Neat, huh? 

The [](/reference/sketch_convert_shape) method did all the heavy lifting to create the object and add apply the base color texture using the UV coordinates.

Note that Trimesh objects can have additional texture maps for things such as surface normals or metallic roughness. Since the
default py5 polygon shader cannot make use of these texture maps, py5's [](/reference/sketch_convert_shape) method will not add them to the created `Py5Shape` object. One could write additional code to make use of them, however.

+++

## Using Trimesh Primitives

Trimesh has a set of [primitive objects](https://trimesh.org/trimesh.primitives.html) such as [Box](https://trimesh.org/trimesh.primitives.html#trimesh.primitives.Box), [Capsule](https://trimesh.org/trimesh.primitives.html#trimesh.primitives.Capsule), [Cylinder](https://trimesh.org/trimesh.primitives.html#trimesh.primitives.Cylinder), and [Sphere](https://trimesh.org/trimesh.primitives.html#trimesh.primitives.Sphere).

The arrangement of triangles in a Trimesh Sphere is different from the arrangement created by py5's [](/reference/sketch_sphere) method.

Let's create a simple example showcasing these objects.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
rot_z = 0

def setup():
    global primitives
    py5.size(500, 500, py5.P3D)

    py5.stroke_weight(1.5)

    primitives = py5.create_shape(py5.GROUP)

    box = py5.convert_shape(Box((80, 120, 70)))
    box.translate(150, 0, 0)
    primitives.add_child(box)

    # NOTE: Trimesh's sections parameter might have a bug
    capsule = py5.convert_shape(Capsule(70, 40, sections=12))
    capsule.translate(0, 150, 0)
    primitives.add_child(capsule)
    
    cylinder = py5.convert_shape(Cylinder(50, 80, sections=12))
    cylinder.translate(-150, 0, 0)
    primitives.add_child(cylinder)

    sphere = py5.convert_shape(Sphere(75, subdivisions=2))
    sphere.translate(0, -150, 0)
    primitives.add_child(sphere)
    

def draw():
    global rot_z
    rot_z += 1

    py5.background(204)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.radians(60))
    py5.rotate_z(py5.radians(rot_z))
    py5.shape(primitives)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(4)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)

py5.exit_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Include note about colors, may need to disable style. Sometimes trimesh adds a style to something. If the object has a style, py5 (should) pick up on that and use it.

Scene, Trimesh, Path2D, Path3D

## Options

textures

```{code-cell} ipython3

```
