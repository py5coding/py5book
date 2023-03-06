# Py5Shape.get_parent()

Locate a child `Py5Shape` object's parent `GROUP` `Py5Shape` object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_parent()](/images/reference/Py5Shape_get_parent_0.png)

</div><div class="example-cell-code">

```python
def setup():
    p = py5.create_shape(py5.GROUP)
    s1 = py5.create_shape(py5.RECT, 10, 10, 35, 35)
    p.add_child(s1)
    s2 = py5.create_shape(py5.RECT, 55, 10, 35, 35)
    p.add_child(s2)
    py5.shape(s2.get_parent())
```

</div></div>

</div>

## Description

Locate a child `Py5Shape` object's parent `GROUP` `Py5Shape` object. This will return `None` if the shape has no parent, such as when the shape is the parent object or the shape is not a part of a group.

Underlying Processing method: PShape.getParent

## Signatures

```python
get_parent() -> Py5Shape
```

Updated on March 06, 2023 02:49:26am UTC
