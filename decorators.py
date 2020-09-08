#!/usr/bin/env python

"""This module contains some decorators for parallelization and testing
"""
__author__ = "Otavio Ferreira"
__status__ = "Prototype"

import time
import threading

THREAD_UPPER_LIMIT = 32
WAIT_TIME = 0.02

def bench_out(func):
	"""Measure and print the time a function takes to execute."""
	def wrap(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		print(f"Done! Total time:{time.time()-start_time:.2f}s")
		return result
	return wrap

def threaded_load(func):
	"""Execute in another thread, waits WAIT_TIME secs after THREAD_UPPER_LIMIT threads limit is exceeded."""
	def wrap(*args, **kwargs):
		while threading.active_count()>THREAD_UPPER_LIMIT:
			time.sleep(WAIT_TIME)
		threading.Thread(target=func, args=args).start()
	return wrap

def wait_all_threads(func):
	"""Waits for all threads to finish before the function exits."""
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
