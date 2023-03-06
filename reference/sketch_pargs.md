# pargs

List of strings passed to the Sketch through the call to [](sketch_run_sketch).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.background(py5.pargs[0])

py5.run_sketch(sketch_args=["#FF0000"])
```

</div></div>

</div>

## Description

List of strings passed to the Sketch through the call to [](sketch_run_sketch). Only passing strings is allowed, but you can convert string types to something else to make this more useful.

Underlying Processing field: args

Updated on March 06, 2023 02:49:26am UTC
