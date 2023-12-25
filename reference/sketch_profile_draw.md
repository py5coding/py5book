# profile_draw()

Profile the execution times of the draw function with a line profiler.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def draw():
    py5.stroke(py5.random_int(255), py5.random_int(255), py5.random_int(255))
    # this draw function should use `points` instead
    for _ in range(100):
        py5.point(py5.random_int(py5.width), py5.random_int(py5.height))


def key_pressed():
    py5.print_line_profiler_stats()


py5.profile_draw()
py5.run_sketch()
```

</div></div>

</div>

## Description

Profile the execution times of the draw function with a line profiler. This uses the Python library lineprofiler to provide line by line performance data. The collected stats will include the number of times each line of code was executed (Hits) and the total amount of time spent on each line (Time). This information can be used to target the performance tuning efforts for a slow Sketch.

This method can be called before or after [](sketch_run_sketch). You are welcome to profile multiple functions, but don't initiate profiling on the same function multiple times. To profile functions that do not belong to the Sketch, including any functions called from [](sketch_launch_thread) and the like, use lineprofiler directly and not through py5's performance tools.

To profile a other functions besides draw, use [](sketch_profile_functions). To see the results, use [](sketch_print_line_profiler_stats).

## Signatures

```python
profile_draw() -> None
```

Updated on December 25, 2023 17:40:34pm UTC
