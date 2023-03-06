# push_matrix()

Pushes the current transformation matrix onto the matrix stack.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for push_matrix()](/images/reference/Sketch_push_matrix_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.fill(255)
    py5.rect(0, 0, 50, 50)  # white rectangle
    
    py5.push_matrix()
    py5.translate(30, 20)
    py5.fill(0)
    py5.rect(0, 0, 50, 50)  # black rectangle
    py5.pop_matrix()
    
    py5.fill(100)
    py5.rect(15, 10, 50, 50)  # gray rectangle
```

</div></div>

<div class="example-row"><div class="example-cell-image">

![example picture for push_matrix()](/images/reference/Sketch_push_matrix_1.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.ellipse(0, 50, 33, 33)  # left circle
    
    py5.stroke_weight(10)
    py5.fill(204, 153, 0)
    
    with py5.push():
        py5.translate(50, 0)
        py5.ellipse(0, 50, 33, 33)  # middle circle
    
    py5.stroke_weight(1)
    py5.fill(255)
    py5.ellipse(100, 50, 33, 33)  # right circle
```

</div></div>

</div>

## Description

Pushes the current transformation matrix onto the matrix stack. Understanding `push_matrix()` and [](sketch_pop_matrix) requires understanding the concept of a matrix stack. The `push_matrix()` function saves the current coordinate system to the stack and [](sketch_pop_matrix) restores the prior coordinate system. `push_matrix()` and [](sketch_pop_matrix) are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

This method can be used as a context manager to ensure that [](sketch_pop_matrix) always gets called, as shown in the last example.

Underlying Processing method: [pushMatrix](https://processing.org/reference/pushMatrix_.html)

## Signatures

```python
push_matrix() -> None
```

Updated on March 06, 2023 02:49:26am UTC
