# noise_seed()

Sets the seed value for [](sketch_noise).

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.noise_seed(42)
    py5.stroke(0, 10)


def draw():
    n = py5.remap(py5.noise(py5.frame_count / 100), 0, 1, 0, py5.width)
    py5.line(n, 0, n, py5.height)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    global xpos, ypos
    py5.rect_mode(py5.CENTER)
    py5.noise_seed(42)
    xpos = py5.width / 2
    ypos = py5.height / 2


def draw():
    global xpos, ypos
    py5.background(128)
    xpos = (xpos + py5.noise(py5.frame_count / 250) - 0.5) % py5.width
    ypos = (ypos + py5.noise(500 + py5.frame_count / 250) - 0.5) % py5.height
    py5.square(xpos, ypos, 25)
```

</div></div>

</div>

## Description

Sets the seed value for [](sketch_noise). By default, [](sketch_noise) produces different results each time the program is run. Set the seed parameter to a constant to return the same pseudo-random numbers each time the Sketch is run.

Underlying Processing method: [noiseSeed](https://processing.org/reference/noiseSeed_.html)

## Signatures

```python
noise_seed(
    seed: int,  # seed value
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
