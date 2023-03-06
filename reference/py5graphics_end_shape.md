# Py5Graphics.end_shape()

The `end_shape()` function is the companion to [](py5graphics_begin_shape) and may only be called after [](py5graphics_begin_shape).

## Description

The `end_shape()` function is the companion to [](py5graphics_begin_shape) and may only be called after [](py5graphics_begin_shape). When `end_shape()` is called, all of image data defined since the previous call to [](py5graphics_begin_shape) is written into the image buffer. The constant `CLOSE` as the value for the `MODE` parameter to close the shape (to connect the beginning and the end).

This method is the same as [](sketch_end_shape) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_end_shape).

Underlying Processing method: PGraphics.endShape

## Signatures

```python
end_shape() -> None

end_shape(
    mode: int,  # use CLOSE to close the shape
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
