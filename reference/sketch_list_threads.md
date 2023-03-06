# list_threads()

List the names of all of the currently running threads.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
def thread1():
    py5.println('thread 1')


def thread2():
    py5.println('thread 2')


def setup():
    py5.frame_rate(10)
    py5.launch_repeating_thread(thread1, name='thread 1', time_delay=1.2)
    py5.launch_repeating_thread(thread2, name='thread 2', time_delay=1.8)


def draw():
    py5.println('running threads:', ', '.join(py5.list_threads()))
    if py5.frame_count == 50:
        py5.stop_all_threads()
```

</div></div>

</div>

## Description

List the names of all of the currently running threads. The names of previously launched threads that have exited will be removed from the list.

## Signatures

```python
list_threads() -> None
```

Updated on March 06, 2023 02:49:26am UTC
