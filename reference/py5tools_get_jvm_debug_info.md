# py5_tools.get_jvm_debug_info()

Get Java Virtual Machine debug information.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

print(py5_tools.get_jvm_debug_info())
```

</div></div>

</div>

## Description

Get Java Virtual Machine debug information. The py5 library requires Java 17 or greater to be installed and the `$JAVA_HOME` environment variable to be properly set. If one or both of these conditions are not true, py5 will not work.

If the Java Virtual Machine cannot start, py5 will include this debug information in the error message. If that doesn't help the user figure out the problem, it will help whomever they go to asking for help.

## Signatures

```python
get_jvm_debug_info() -> dict[str, Any]
```

Updated on March 06, 2023 02:49:26am UTC
