# pop_matrix()

Pops the current transformation matrix off the matrix stack.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for pop_matrix()](/images/reference/Sketch_pop_matrix_0.png)

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

</div>

## Description

Pops the current transformation matrix off the matrix stack. Understanding pushing and popping requires understanding the concept of a matrix stack. The [](sketch_push_matrix) function saves the current coordinate system to the stack and `pop_matrix()` restores the prior coordinate system. [](sketch_push_matrix) and `pop_matrix()` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

Underlying Processing method: [popMatrix](https://processing.org/reference/popMatrix_.html)

## Signatures

```python
pop_matrix() -> None
```

Updated on March 06, 2023 02:49:26am UTC
