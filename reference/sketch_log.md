# log()

Calculates the natural logarithm (the base-e logarithm) of a number.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
  i = 12
  py5.println(py5.log(i))
  py5.println(log10(i))

  j = -5
  py5.println(py5.log(j))

# Calculates the base-10 logarithm of a number
# use this if you don't want to use numpy's log10 function
def log10(x):
    return (py5.log(x) / py5.log(10))
```

</div></div>

</div>

## Description

Calculates the natural logarithm (the base-e logarithm) of a number. This function expects the `n` parameter to be a value greater than 0.0. This function is the compliment to [](sketch_exp).

This function makes a call to the numpy `log()` function. If the `n` parameter is less than or equal to 0.0, you will see a `RuntimeWarning` and the returned result will be numpy's Not-a-Number value, `np.nan`.

## Signatures

```python
log(
    value: Union[float, npt.ArrayLike],  # number greater than 0.0
) -> Union[float, npt.NDArray]
```

Updated on August 23, 2025 19:59:53pm UTC
