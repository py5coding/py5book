# end_record()

Stops the recording process started by [](sketch_begin_record) and closes the file.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.size(400, 400)
    py5.begin_record(py5.PDF, "everything.pdf")


def draw():
    py5.ellipse(py5.mouse_x, py5.mouse_y, 10, 10)


def mouse_pressed():
    py5.end_record()
    py5.exit_sketch()
```

</div></div>

</div>

## Description

Stops the recording process started by [](sketch_begin_record) and closes the file.

Underlying Processing method: [endRecord](https://processing.org/reference/endRecord_.html)

## Signatures

```python
end_record() -> None
```

Updated on March 06, 2023 02:49:26am UTC
