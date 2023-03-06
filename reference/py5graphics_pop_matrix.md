# Py5Graphics.pop_matrix()

Pops the current transformation matrix off the matrix stack.

## Description

Pops the current transformation matrix off the matrix stack. Understanding pushing and popping requires understanding the concept of a matrix stack. The [](py5graphics_push_matrix) function saves the current coordinate system to the stack and `pop_matrix()` restores the prior coordinate system. [](py5graphics_push_matrix) and `pop_matrix()` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

This method is the same as [](sketch_pop_matrix) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_pop_matrix).

Underlying Processing method: PGraphics.popMatrix

## Signatures

```python
pop_matrix() -> None
```

Updated on March 06, 2023 02:49:26am UTC
