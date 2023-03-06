# Py5Shape.get_child_index()

Get a child `Py5Shape` object's index from a parent `Py5Shape` object that is defined as a `GROUP`.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for get_child_index()](/images/reference/Py5Shape_get_child_index_0.png)

</div><div class="example-cell-code">

```python
def setup():
    us_map = py5.load_shape("us_map.svg")
    for child in us_map.get_children():
        idx = us_map.get_child_index(child)
        py5.println(child.get_name(), idx)

    py5.background(192)
    py5.scale(0.1)
    py5.translate(25, 225)
    py5.shape(us_map, 0, 0)
```

</div></div>

</div>

## Description

Get a child `Py5Shape` object's index from a parent `Py5Shape` object that is defined as a `GROUP`. Inside Processing, a group `Py5Shape` object is an ordered list of child shapes. This method will retrieve the index for a particular child in that ordered list. That index value is useful when using other methods such as [](py5shape_get_child) or [](py5shape_remove_child).

Underlying Processing method: PShape.getChildIndex

## Signatures

```python
get_child_index(
    who: Py5Shape,  # Py5Shape object
    /,
) -> int
```

Updated on March 06, 2023 02:49:26am UTC
