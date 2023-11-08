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

## Convert Trimesh objects to Py5Shapely objects

+++

Let's start by importing the Trimesh library and some classes we will use later.

```{code-cell} ipython3
import py5_tools
import py5

import trimesh
```

For our first example, we will use a 3D model file downloaded from [TurboSquid](https://www.turbosquid.com/). Our example is a
[strawberry](https://www.turbosquid.com/3d-models/3d-strawberry-1962030) created by the artist [minimoku](https://www.turbosquid.com/Search/Artists/minimoku).

Loading a complex 3D model in Trimesh may be slow. Don't load a model from within a Sketch unless absolutely necessary.  If you need to do this, load it once in `setup()`.

```{code-cell} ipython3
strawberry_model = trimesh.load('models/Strawberry_gltf.gltf')
```

We can use the [](/reference/sketch_convert_shape) method to effortlessly
convert this model into a `Py5Shape` object.

```{code-cell} ipython3
def setup():
    global strawberry
    py5.size(300, 500, py5.P3D)
    strawberry = py5.convert_shape(strawberry_model)
    assert isinstance(strawberry, py5.Py5Shape)

    # increase the model's scale and change its orientation
    strawberry.scale(50)
    strawberry.rotate_z(-py5.radians(90))
```

After converting the model into a `Py5Shape` object, we need to increase the scale and rotate it to change its orientation. Consider py5's coordinate system: the positive Y axis points towards the bottom of the drawing surface, the positive X axis points towards the right side of the drawing surface, and the positive Z axis points away from the drawing surface, towards the viewer. The model may have been created with a different coordinate system in mind. The model may also have been created with a different scale.

When loading a model, you will often want to apply some transformations so it can be drawn as you intend for it to be drawn. These adjustments can be done after converting the model into a `Py5Shape` object, as we did here in our `setup()` function. Alternatively, we can do the adjustments in the `draw()` function before the drawing the `Py5Shape` object to the screen with [](/reference/sketch_shape).

You can also adjust the Trimesh mesh object using Trimesh's transformation tools, before the call to [](/reference/sketch_convert_shape). You will use Trimesh's [apply_transform()](https://trimesh.org/trimesh.html#trimesh.Trimesh.apply_transform) method to apply a transformation matrix to a mesh.

Now let's create a `draw()` method to draw the `Py5Shape` object with the [](/reference/sketch_shape) method. 

```{code-cell} ipython3
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

We need to invert the model's y axis because the top of the strawberry is oriented towards the positive y axis but Processing and therefore py5 has the positive y axis pointing towards the bottom of the drawing surface. You will frequently need to employ rotations and scale adjustments when working with models created outside of py5.

When we run this, the strawberry will slowly rotate along its main axis.

```{code-cell} ipython3
py5.run_sketch()
```

The result looks like this:

```{code-cell} ipython3
py5_tools.screenshot()
```

Neat, huh? 

The [](/reference/sketch_convert_shape) method did all the heavy lifting to create the object and add apply the base color texture using the UV coordinates.

Note that Trimesh objects can have additional texture maps for things such as surface normals or metallic roughness. Since the
default py5 polygon shader cannot make use of these, py5's [](/reference/sketch_convert_shape) method will not add them to the created `Py5Shape` object.

+++

Simple geometry examples, show boolean operations

Include note about colors, may need to disable style. Sometimes trimesh adds a style to something. If the object has a style, py5 (should) pick up on that and use it.

Scene, Trimesh, Path2D, Path3D

## Options

textures

```{code-cell} ipython3

```
