# java_version_name

Version name of Java currently being used by py5.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def setup():
    py5.println(py5.java_version_name)
```

</div></div>

</div>

## Description

Version name of Java currently being used by py5. Internally the py5 library is using the Processing Java libraries to provide functionality. Those libraries run in a Java Virtual Machine. This field provides the Java version name for that Virtual Machine.

Underlying Processing field: javaVersionName

Updated on March 06, 2023 02:49:26am UTC
