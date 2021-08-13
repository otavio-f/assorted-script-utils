# assorted-script-utils
Some python utilities

***Warning! Can contain bugs***

***This was made as a exercise on python decorators and development with git***

***Coding and learning in progress***

### ```@threaded_load``` and ```@wait_all_threads```
- Each method call will execute in a separate thread
- ```sync_method``` only returns after all extra threads have finished
- Note: ```@threaded_load``` ***returns None***, so any method using it will return None as well
```python
from decorators import *

@threaded_load
def do_something(i):
    pass #work on i

@wait_all_threads
def sync_method(large_iterable):
    for i in large_iterable:
        process(i)
```


### ```@bench_out```
- Print execution time
```python
@bench_out
def method_i_want_to_measure():
    some_result = do_something()
    some_result.do_another_thing()
    finish()
    return some_result
```


### ```@test```
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
