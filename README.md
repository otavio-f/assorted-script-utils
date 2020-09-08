# assorted-utils
Some decorators for python

Construction and learning in progress

> Threading example
- Each method call will execute in a separate thread
- The sync method only returns after all extra threads have finished
```python
from decorators import *

@threaded_load
def manipulate(i):
    do_something_with(i)

@wait_all_threads
def sync_method(large_iterable):
    for i in large_iterable:
        manipulate(i)
```

> Bench example
- Print execution time
```python
@bench_out
def method_i_want_to_measure():
    some_result = do_something()
    some_result.do_another_thing()
    finish()
    return some_result
```

> Test example
- Print some info about assertion success, fail or error
```python
def prepare():
    start_something()

def cleanup():
   undo_something()
   
@test(pre=prepare, post=cleanup)
def test_if_is_true():
    assert is_not_false() == True
    
@test()
def dummy_test():
    assert 3 != None
```
