# Importing py5 Code

Python projects with moderate to large amounts of code will typically be split
into multiple files. Python libraries or modules are also typically organized
across multiple files. Coders can use the Python `import` command to make code
stored in other files or modules available to be used in their py5 projects.
This page outlines the recommended ways to write importable py5 code, either for
use by the author or to be shared with others.

## General py5 Importing Guidelines

If you make use of py5's Module Mode, you might decide to also write your py5
library code in Module Mode. Your library code might then like this:

```python
# helper_functions.py
import py5


def draw_two_squares():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
    py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
```

If you are writing code for yourself, do whatever works best for you. However,
if you plan to distribute this *helper_functions.py* code to others, you should
be aware that it will only work correctly for users who are also programming in
Module Mode. It can't work for py5 users programming in Class Mode. Imported
Mode users will experience difficulties with the dynamic variables like
`mouse_x` and `mouse_y`.

You should not assume that other py5 users will want to use the same py5 Mode
that you use.

A more universal approach is to modify this code slightly so that it can be
imported by any py5 user, regardless of which py5 Mode they are using:

```python
# helper_functions.py
import py5


def draw_two_squares(*, sketch: py5.Sketch=None):
    s = sketch or py5.get_current_sketch()
    s.rect(s.mouse_x, s.mouse_y, 10, 10)
    s.rect(s.random_int(s.width), s.random_int(s.height), 10, 10)
```

The important thing to observe here is that the function should obtain a
`py5.Sketch` instance and then use that instance to access py5's methods and
variables. Accessing py5's methods through the py5 module (i.e. `py5.rect()`,
`py5.mouse_x`, etc.) is incorrect for Class Mode users and will result in
confusing errors for Imported Mode users because the dynamic variables such as
`py5.mouse_x` and `py5.mouse_y` will not work.

The extra bit of complexity will be transparent to your users, and will make
the library accessible to users programming in any of py5's Modes. For example,
a coder writing py5 code in Module Mode would use `helper_functions.py` like
this:

```python
import py5

import helper_functions


def setup():
    py5.size(500, 500)


def draw():
    helper_functions.draw_two_squares()
```

Coders using Imported Mode would use the library like this:

```python
import helper_functions


def setup():
    size(500, 500)


def draw():
    helper_functions.draw_two_squares()
```

Coders using Class Mode would use the optional keyword argument `sketch` to pass
their `Sketch` instance, like this:

```python
from py5 import Sketch

import helper_functions


class Example(Sketch):

    def settings(self):
        self.size(500, 500)

    def draw(self):
        helper_functions.draw_two_squares(sketch=self)
```

If you decide to ignore Class Mode you can simplify the `helper_functions.py`
code slightly:

```python
# helper_functions.py
import py5


def draw_two_squares():
    s = py5.get_current_sketch()
    s.rect(s.mouse_x, s.mouse_y, 10, 10)
    s.rect(s.random_int(s.width), s.random_int(s.height), 10, 10)
```

To reiterate, your py5 module code should obtain a `py5.Sketch` instance and
then only use that instance to access py5's methods and variables.

## Importing Imported Mode Code

The guidelines for Imported Mode users are simplified so that beginner coders
writing code in Imported Mode can split their code into multiple files without
needing to know about the other py5 Modes. This feature will help educators
introduce the benefits of Python code importing to their students.

Continuing with our `helper_functions.py` example, an Imported Mode coder would
write the following code:

```python
# helper_functions.py

# PY5 IMPORTED MODE CODE

def draw_two_squares():
    rect(mouse_x, mouse_y, 10, 10)
    rect(random_int(width), random_int(height), 10, 10)
```

The extra `# PY5 IMPORTED MODE CODE` comment is important. It is a marker to
signal an import hook added by py5's Imported Mode execution engine that this
module contains py5 code written in Imported Mode. This Python module will be
imported differently, enabling the Imported Mode code to work correctly by an
Import Mode py5 Sketch.

This `helper_functions` library can be imported much like any other Python
module and used in a Sketch:

```python
import helper_functions


def setup():
    size(200, 200)


def draw():
    helper_functions.draw_two_squares()
```

As the `helper_functions.py` module grows, you might want to break it up into
multiple files. In that case, the `# PY5 IMPORTED MODE CODE` comment only
needs to be used once in your library's root `__init__.py` file.

```python
# helper_functions/__init__.py

# PY5 IMPORTED MODE CODE

from . import shape_helpers
from . import line_helpers
```

There's no need to add the `# PY5 IMPORTED MODE CODE` marker to every file in
the module. The marker is case insensitive, so `# py5 Imported Mode code` will
work just as well. If you forget to add this or add it incorrectly, you will
get an error message reminding you.

```txt
File "/tmp/test/helper_functions.py", line 13, in draw_squares
    12   def draw_squares():
--> 13       rect(mouse_x, mouse_y, 10, 10)
    14       rect(random_int(width), random_int(height), 10, 10)

NameError: The name "rect" is not defined. Your Sketch is also running in Imported Mode. If the code throwing this exception was imported into your main py5 Sketch code, please ensure the py5 Imported Mode marker "# PY5 IMPORTED MODE CODE" has been properly added to the module.
```
