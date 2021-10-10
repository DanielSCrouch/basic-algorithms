from functools import wraps, update_wrapper

# Decorator with stateful class cache

class Memoize(object):
  """
  Decorator to cache function responses for lookup on subsequent calls. 
  """

  def __init__(self, f):
    self.f = f
    self.cache = {}
    update_wrapper(self, f)

  def __call__(self, *args, **kwargs):
    if not args in self.cache:
      self.cache[args] = self.f(*args, *kwargs)   
    return self.cache[args]

@Memoize
def fibonacci(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2) 



# # Decorator with global cache

# cache = {}

# def memoize(f):
#   @wraps(f)
#   def wrap(*args, **kwargs):
#     if not args in cache:
#       cache[args] = f(*args, *kwargs)    
#     return cache[args]
#   return wrap

# @memoize
# def fibonacci_memoized(n: int) -> int:
#   return fibonacci(n)

