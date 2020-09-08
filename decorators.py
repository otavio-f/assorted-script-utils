#!/usr/bin/env python

"""This method contains decorators for parallelization and testing
"""
__author__ = "Otavio Ferreira"
__version__ = 0.01
__status__ = "Prototype"

import time
import threading

THREAD_UPPER_LIMIT = 32

def bench_out(func):
	"""Decorator to benchmark execution time
		Measures the time a function takes to execute
	"""
	def wrap(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		print(f"Done! Total time:{time.time()-start_time:.2f}s")
		return result
	return wrap

def threaded_load(func):
	"""Decorator for parallelization.
		Executes the method in a separate thread. Keeps the active thread count
		below the value specified in the variable THREAD_UPPER_LIMIT
	"""
	def wrap(*args, **kwargs):
		while threading.active_count()>THREAD_UPPER_LIMIT:
			time.sleep(0.001)
		threading.Thread(target=func, args=args).start()
	return wrap

def wait_all_threads(func):
	"""Decorator for syncronization.
		Waits for all threads to finish before the function exits
	"""
	def wrap(*args, **kwargs):
		result = func(*args, **kwargs)
		#print("\t*Waiting for threads to finish...")
		while threading.active_count()>1:
			time.sleep(0.01)
		return result
	return wrap

def test(pre=None, post=None):
	"""Decorator to execute tests and print useful information
		The method being tested must have an <assert>
		pre is a function without arguments to execute before the test starts
		post is a function without arguments to execute after the test has finished
	"""
	def inner(func):
		def wrap(*args, **kwargs):
			if pre:
				pre()

			print(func.__name__,":", end="")
			try:
				func()
				print("OK!")
			except AssertionError:
				print("ASSERTION ERROR!")
			except Exception as exc:
				print("ERROR!", exc)
				
			if post:
				post()
		return wrap
	return inner