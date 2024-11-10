# Py5Graphics.vertex()

Add a new vertex to a shape.

## Description

Add a new vertex to a shape. All shapes are constructed by connecting a series of vertices. The `vertex()` method is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the [](py5graphics_begin_shape) and [](py5graphics_end_shape) functions.

Drawing a vertex in 3D using the `z` parameter requires the `P3D` renderer.

This method is also used to map a texture onto geometry. The [](py5graphics_texture) function declares the texture to apply to the geometry and the `u` and `v` coordinates define the mapping of this texture to the form. By default, the coordinates used for `u` and `v` are specified in relation to the image's size in pixels, but this relation can be changed with the [](py5graphics_texture_mode) method.

This method is the same as [](sketch_vertex) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_vertex).

Underlying Processing method: PGraphics.vertex

## Signatures

```python
vertex(
    x: float,  # x-coordinate of the vertex
    y: float,  # y-coordinate of the vertex
    /,
) -> None

vertex(
    x: float,  # x-coordinate of the vertex
    y: float,  # y-coordinate of the vertex
    u: float,  # horizontal coordinate for the texture mapping
    v: float,  # vertical coordinate for the texture mapping
    /,
) -> None

vertex(
    x: float,  # x-coordinate of the vertex
    y: float,  # y-coordinate of the vertex
    z: float,  # z-coordinate of the vertex
    /,
) -> None

vertex(
    x: float,  # x-coordinate of the vertex
    y: float,  # y-coordinate of the vertex
    z: float,  # z-coordinate of the vertex
    u: float,  # horizontal coordinate for the texture mapping
    v: float,  # vertical coordinate for the texture mapping
    /,
) -> None
```

Updated on October 28, 2024 02:52:09am UTC
