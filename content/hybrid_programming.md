# Hybrid Programming

Hybrid Programming refers to py5's ability to combine Python and Java code together, getting the best of both worlds.

## Reasons for Hybrid Programming

There are a few reasons why hybrid programming might benefit your work.

First, performance. This is the most important benefit. Although py5 Sketches can be quite performant, you may experience performance problems if you have a large for loop or nested for loops making many calls from Python to Java. There is a small performance penalty for each individual call to Java, and it is better to not do this in a large or nested for loop. Hybrid programming can enable you to pass a large amount of data to Java with one call. In Java, you can then iterate through the data without a performance penalty.

Second, hybrid programming opens a door to incorporating Java libraries into your work. Much like Python, the Java library ecosystem is extensive and backed by a strong community. If you can't find the library you need in the Python world, you can try Java instead.

Third, hybrid programming can help you leverage the simplicity and prototyping strengths of Python into your development process, even if the Sketch will ultimately be 100% Java in the final work.

## Understand JPype

Before exploring hybrid programming in py5, you should first read JPype's documentation. This will help you accomplish more with hybrid programming. Start with the [Java QuickStart Guide](https://jpype.readthedocs.io/en/latest/quickguide.html), and also read the [Working with Numpy](https://jpype.readthedocs.io/en/latest/userguide.html#working-with-numpy) and [Implementing Java interfaces](https://jpype.readthedocs.io/en/latest/userguide.html#implementing-java-interfaces) sections in the [JPype User Guide](https://jpype.readthedocs.io/en/latest/userguide.html).

## Importing Java Classes into Python

Technically you don't really need much from py5 to combine Python and Java code because JPype already provides the needed functionality. As explained in JPype's documentation, you can seamlessly import any Java class and create instances. To do this, you must do two things.

1. Add the necessary jar files to your classpath *before* importing py5. There are a few ways you can do this:
  * Explicitly adding the jars with [](/reference/py5tools_add_jars) and [](/reference/py5tools_add_classpath)
  * Put your jar files in a `jars` directory that is a subdirectory of the current working directory
  * Create an environment variable `PY5_JARS` that points to a directory with jar files
2. Import the Java libraries with the `import` command *after* importing py5. Importing py5 will also start the JVM. Jars cannot be added after the JVM is started.

A simple example might look like this:

```python
from pathlib import Path

import py5_tools

py5_tools.add_jars(Path.home() / 'project_jar_dir')

import py5

from java.lang import String
# import class defined in jar found in `project_jar_dir`
from org.utils import JavaUtilities

test_string = String('test')
# create instance of class defined in jar found in `project_jar_dir`
utils = JavaUtilities()
```

## Hybrid Programming Support in py5

py5utils

py5.utils

simple example

## Java and Python Object Conversion

Py5Image to PImage

Strings

## Performance Testing

Illustrative example using colored points

Show line profiler
