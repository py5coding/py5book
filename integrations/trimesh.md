---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 3D Shapes and Trimesh

[Trimesh](https://trimesh.org/) is a well-known and well-maintained library for
working with 3D geometry.

The goal of Trimesh is to "provide a full featured and well tested Trimesh
object which allows for easy manipulation and analysis, in the style of the
Polygon object in the Shapely library."

Trimesh can greatly extend py5's ability to load 3D objects, far exceeding what
can be achieved with [](/reference/sketch_load_shape.md).

## Setup

Installing Trimesh by itself is acceptable but Trimesh is much more useful if
you install its dependent libraries. At a minimum, you should install the easy
to install dependencies with this command:

```bash
pip install trimesh[easy]
```

Refer to the [Trimesh Installation page](https://trimesh.org/install.html) for
more information about Trimesh's dependencies and installation options.

Development of py5's integration code was done with Trimesh version 3.23.
Version 4.0 was released shortly after but seems to work just as well as 3.23.

Installing [OpenSCAD](https://openscad.org/) or
[Blender](https://www.blender.org/) on your computer may also be useful. Trimesh
can use these to perform boolean operations on 3D objects.

If Trimesh is missing a dependent library needed for the functionality you want
to use, it will provide you with an error message informing you of what you
should install.

## Basic Example

Example showing how to load a glb or gltf file with the texture

Simple geometry examples, show boolean operations

Include note about colors, may need to disable style. Sometimes trimesh adds a
style to something. If the object has a style, py5 (should) pick up on that and
use it.

Scene, Trimesh, Path2D, Path3D

## Options

textures
