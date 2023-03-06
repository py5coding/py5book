# Py5Shape.get_child_count()

Returns the number of children within the `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    us_map = py5.load_shape("us_map.svg")
    count = us_map.get_child_count()
    py5.println(count)
```

</div></div>

</div>

## Description

Returns the number of children within the `Py5Shape` object.

Underlying Processing method: [PShape.getChildCount](https://processing.org/reference/PShape_getChildCount_.html)

## Signatures

```python
get_child_count() -> int
```

Updated on March 06, 2023 02:49:26am UTC
