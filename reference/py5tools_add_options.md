# py5_tools.add_options()

Provide JVM options to use when the JVM starts.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools
py5_tools.add_options('-Xmx4096m')
import py5
```

</div></div>

</div>

## Description

Provide JVM options to use when the JVM starts. This is useful to set the JVM memory size, for example.

After the JVM has started, new options cannot be added. This function will throw a `RuntimeError` if it is called after the JVM has already started. Use [](py5tools_is_jvm_running) to first determine if the JVM is running.

## Signatures

```python
add_options(
    *options: list[str],
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
