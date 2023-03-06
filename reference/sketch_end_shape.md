# end_shape()

The `end_shape()` function is the companion to [](sketch_begin_shape) and may only be called after [](sketch_begin_shape).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for end_shape()](/images/reference/Sketch_end_shape_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.no_fill()
    
    py5.begin_shape()
    py5.vertex(20, 20)
    py5.vertex(45, 20)
    py5.vertex(45, 80)
    py5.end_shape(py5.CLOSE)
    
    py5.begin_shape()
    py5.vertex(50, 20)
    py5.vertex(75, 20)
    py5.vertex(75, 80)
    py5.end_shape()
```

</div></div>

</div>

## Description

The `end_shape()` function is the companion to [](sketch_begin_shape) and may only be called after [](sketch_begin_shape). When `end_shape()` is called, all of image data defined since the previous call to [](sketch_begin_shape) is written into the image buffer. The constant `CLOSE` as the value for the `MODE` parameter to close the shape (to connect the beginning and the end).

Underlying Processing method: [endShape](https://processing.org/reference/endShape_.html)

## Signatures

```python
end_shape() -> None

end_shape(
    mode: int,  # use CLOSE to close the shape
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
