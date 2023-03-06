# random()

Generates random numbers.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for random()](/images/reference/Sketch_random_0.png)

</div><div class="example-cell-code">

```python
def setup():
    py5.random_seed(42)
    for i in range(100):
        s = py5.random()
        py5.stroke(255*s)
        r = py5.random(80)
        py5.line(20, i, 20+r, i)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    for i in range(100):
        r = py5.random(-50, 50)
        py5.println(r)
```

</div></div>

</div>

## Description

Generates random numbers. Each time the `random()` function is called, it returns an unexpected value within the specified range. This function's randomness can be influenced by [](sketch_random_seed).

If no parameters are passed to the function, it will return a float between zero and one.

If only one parameter is passed to the function, it will return a float between zero and the value of the `high` parameter. For example, `random(5)` returns values between 0 and 5 (starting at zero, and up to, but not including, 5).

If two parameters are specified, the function will return a float with a value between the two values. For example, `random(-5, 10.2)` returns values starting at -5 and up to (but not including) 10.2. To convert a floating-point random number to an integer, use the `int()` function, or alternatively, consider using [](sketch_random_int).

This function makes calls to numpy to generate the random values.

## Signatures

```python
random() -> float

random(
    high: float,  # upper limit
    /,
) -> float

random(
    low: float,  # lower limit
    high: float,  # upper limit
    /,
) -> float
```

Updated on March 06, 2023 02:49:26am UTC
