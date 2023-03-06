# get_frame_rate()

Get the running Sketch's current frame rate.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
    py5.println(py5.get_frame_rate())
```

</div></div>

</div>

## Description

Get the running Sketch's current frame rate. This is measured in frames per second (fps) and uses an exponential moving average. The returned value will not be accurate until after the Sketch has run for a few seconds. You can set the target frame rate with [](sketch_frame_rate).

This method provides the same information as Processing's `frameRate` variable. Python can't have a variable and a method with the same name, so a new method was created to provide access to that variable.

Underlying Processing method: getFrameRate

## Signatures

```python
get_frame_rate() -> float
```

Updated on March 06, 2023 02:49:26am UTC
