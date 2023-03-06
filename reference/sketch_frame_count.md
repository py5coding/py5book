# frame_count

The system variable `frame_count` contains the number of frames that have been displayed since the program started.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.frame_rate(30)


def draw():
    py5.line(0, 0, py5.width, py5.height)
    py5.println(py5.frame_count)
```

</div></div>

</div>

## Description

The system variable `frame_count` contains the number of frames that have been displayed since the program started. Inside `setup()` the value is 0. Inside the first execution of `draw()` it is 1, and it will increase by 1 for every execution of `draw()` after that.

Underlying Processing field: [frameCount](https://processing.org/reference/frameCount.html)

Updated on March 06, 2023 02:49:26am UTC
