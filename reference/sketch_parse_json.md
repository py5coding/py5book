# parse_json()

Parse serialized JSON data from a string.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for parse_json()](/images/reference/Sketch_parse_json_0.png)

</div><div class="example-cell-code">

```python
serialized_json = '{"red":255, "green":255, "blue":128}'

def setup():
    data = py5.parse_json(serialized_json)
    py5.fill(data['red'], data['green'], data['blue'])
    py5.rect(10, 10, 80, 80)
```

</div></div>

</div>

## Description

Parse serialized JSON data from a string. When reading JSON data from a file, [](sketch_load_json) is the better choice.

The JSON data is parsed using the Python json library with the `loads` method, and the `kwargs` parameter is passed along to that method.

## Signatures

```python
parse_json(
    serialized_json: Any,  # JSON data object that has been serialized as a string
    **kwargs: dict[str, Any]
) -> Any
```

Updated on March 06, 2023 02:49:26am UTC
