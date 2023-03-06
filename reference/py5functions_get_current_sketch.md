# get_current_sketch()

Get the py5 module's current `Sketch` instance.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
sketch = py5.get_current_sketch()
assert sketch.is_ready
py5.run_sketch(block=False)
assert sketch.is_running
py5.exit_sketch()
assert sketch.is_dead
```

</div></div>

</div>

## Description

Get the py5 module's current `Sketch` instance.

When coding py5 in module mode, a Sketch instance is created on your behalf that is referenced within the py5 module itself. That Sketch is called the "current sketch." Use this method to access that Sketch instance directly.

## Signatures

```python
get_current_sketch() -> Sketch
```

Updated on March 06, 2023 02:49:26am UTC
