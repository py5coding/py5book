# join_thread()

Join the Python thread associated with the given thread name.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import time


def f():
    py5.println("start f()")
    time.sleep(0.5)
    py5.println("end f()")


def setup():
    py5.println("start setup()")
    py5.launch_thread(f, "f")
    py5.println("thread f() launched")
    stopped = py5.join_thread("f", timeout=0.25)
    msg = "thread f() " + ("has stopped" if stopped else "is still running")
    py5.println(msg)
    py5.println("end setup()")
```

</div></div>

</div>

## Description

Join the Python thread associated with the given thread name. The `join_thread()` method will wait until the named thread has finished executing before returning. Use the `timeout` parameter to set an upper limit for the number of seconds to wait. This method will return right away if the named thread does not exist or the thread has already finished executing. You can get the list of all currently running threads with [](sketch_list_threads).

This method will return `True` if the named thread has completed execution and `False` if the named thread is still executing. It will only return `False` if you use the `timeout` parameter and the method is not able to join with the thread within that time limit.

## Signatures

```python
join_thread(
    name: str,  # name of thread
    *,
    timeout: float = None  # maximum time in seconds to wait for the thread to join
) -> bool
```

Updated on March 06, 2023 02:49:26am UTC
