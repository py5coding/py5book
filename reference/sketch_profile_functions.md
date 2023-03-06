# profile_functions()

Profile the execution times of the Sketch's functions with a line profiler.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time


def setup():
    # to load images from the web, use `request_image` instead
    img = py5.load_image('http://py5coding.org/files/apples.jpg')
    py5.image_mode(py5.CORNERS)
    py5.image(img, 10, 10, py5.width - 10, py5.height - 10)


py5.profile_functions(['setup'])
py5.run_sketch()

time.sleep(5)
py5.print_line_profiler_stats()
```

</div></div>

</div>

## Description

Profile the execution times of the Sketch's functions with a line profiler. This uses the Python library lineprofiler to provide line by line performance data. The collected stats will include the number of times each line of code was executed (Hits) and the total amount of time spent on each line (Time). This information can be used to target the performance tuning efforts for a slow Sketch.

This method can be called before or after [](sketch_run_sketch). You are welcome to profile multiple functions, but don't initiate profiling on the same function multiple times. To profile functions that do not belong to the Sketch, including any functions called from [](sketch_launch_thread) and the like, use lineprofiler directly and not through py5's performance tools.

To profile just the draw function, you can also use [](sketch_profile_draw). To see the results, use [](sketch_print_line_profiler_stats).

## Signatures

```python
profile_functions(
    function_names: list[str],  # names of py5 functions to be profiled
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
