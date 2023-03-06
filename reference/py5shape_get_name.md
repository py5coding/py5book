# Py5Shape.get_name()

Get the name assigned to a Py5Shape object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_name()](/images/reference/Py5Shape_get_name_0.png)

</div><div class="example-cell-code">

```python
def setup():
    us_map = py5.load_shape("us_map.svg")
    for child in us_map.get_children():
        py5.println(child.get_name())

    py5.background(192)
    py5.scale(0.1)
    py5.translate(25, 225)
    py5.shape(us_map, 0, 0)
```

</div></div>

</div>

## Description

Get the name assigned to a Py5Shape object. Will return `None` if the object has no name.

Underlying Processing method: PShape.getName

## Signatures

```python
get_name() -> str
```

Updated on March 06, 2023 02:49:26am UTC
