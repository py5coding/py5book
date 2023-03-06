# py5_tools.add_jars()

Add all of the Java jar files contained in a directory and its subdirectories to the classpath.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.add_jars('path/to/project_jars')
py5_tools.add_classpath('path/to/jar/file/java_code.jar')

import py5

py5.println(py5_tools.get_classpath())
```

</div></div>

</div>

## Description

Add all of the Java jar files contained in a directory and its subdirectories to the classpath. The path can be absolute or relative. If the directory does does not exist, it will be ignored.

When `import py5` is executed, `add_jars('jars')` is called for you to automatically add jar files contained in a subdirectory called jars. This is similar to functionality provided by the Processing IDE.

After the JVM has started, the classpath cannot be changed. This function will throw a `RuntimeError` if it is called after the JVM has already started. Use [](py5tools_is_jvm_running) to first determine if the JVM is running.

## Signatures

```python
add_jars(
    path: Union[Path, str]  # path to directory containing jar files
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
