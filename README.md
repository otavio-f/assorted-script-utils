# assorted-script-utils
Some python decorators

***Personal use: ~~Can~~ Will contain bugs***

***Coding and learning in progress***


### ```@threaded_load``` and ```@wait_all_threads```
- Each method call will execute in a separate thread
- ```sync_method``` only returns after all extra threads have finished
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
