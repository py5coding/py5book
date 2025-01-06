# lines()

Draw a collection of lines to the screen.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for lines()](/images/reference/Sketch_lines_0.png)

</div><div class="example-cell-code">

```python
import numpy as np

def setup():
    random_lines = 100 * np.random.rand(50, 4)
    py5.lines(random_lines)
```

</div></div>

</div>

## Description

Draw a collection of lines to the screen. The purpose of this method is to provide an alternative to repeatedly calling [](sketch_line) in a loop. For a large number of lines, the performance of `lines()` will be much faster.

The `coordinates` parameter should be a numpy array with one row for each line. The first few columns are for the first point of each line and the next few columns are for the second point of each line. There will be four or six columns for 2D or 3D points, respectively.

## Signatures

```python
lines(
    coordinates: Iterator[Iterator[float]],  # 2D array of line coordinates with 4 or 6 columns for 2D or 3D points, respectively
    /,
) -> None
```

Updated on January 06, 2025 22:21:18pm UTC
