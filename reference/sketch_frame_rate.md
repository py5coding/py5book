# frame_rate()

Specifies the number of frames to be displayed every second.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
pos = 0


def setup():
    py5.frame_rate(4)


def draw():
    global pos
    py5.background(204)
    pos += 1
    py5.line(pos, 20, pos, 80)
    if pos > py5.width:
        pos = 0
```

</div></div>

</div>

## Description

Specifies the number of frames to be displayed every second. For example, the function call `frame_rate(30)` will attempt to refresh 30 times a second. If the processor is not fast enough to maintain the specified rate, the frame rate will not be achieved. Setting the frame rate within `setup()` is recommended. The default rate is 60 frames per second.

Underlying Processing method: [frameRate](https://processing.org/reference/frameRate_.html)

## Signatures

```python
frame_rate(
    fps: float,  # number of desired frames per second
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
