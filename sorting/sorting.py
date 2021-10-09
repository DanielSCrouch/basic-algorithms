
from timer import timeit
from random import randrange

# @timeit
  
def bubble_sort(basket: list) -> None:
  """Sorts a list in ascending order, O(n^2)"""
  sorted = False 
  while not sorted:
    sorted = True
    for j in range(1, len(basket)):
      i = j - 1
      if basket[j] < basket[i]:
        value_i = basket[i] 
        basket[i] = basket[j] 
        basket[j] =  value_i
        sorted = False

def selection_sort(basket: list) -> None:
  """Sorts a list in ascending order, O(n^2)"""
  for i in range(0, len(basket)):
    # Itentify smallest for subset of list
    smallest = basket[i] 
    smallest_index = i
    for j in range(i+1, len(basket)):
      if basket[j] < smallest:
        smallest = basket[j]
        smallest_index = j

    # Set smallest to first position of sublist
    if basket[i] != smallest:
      p = basket[i] 
      basket[i] = smallest
      basket[smallest_index] = p


def insertion_sort(basket: list) -> list: 
  """Sorts a list in ascending order, O(n^2)"""
  for i in range(1, len(basket)):

    # If next item is bigger do nothing
    if basket[i] >= basket[i - 1]:
      continue
    
    # Else, insert item into previously sorted sub-list
    for j in range(i - 1, -1, -1):
      if basket[i] < basket[j]:
        # skip if less than next smallest too
        if j != 0:
          if basket[i] < basket[j - 1]:
            continue

        basket = basket[0:j] + basket[i:i+1] + basket[j:i] + basket[i+1:] 

  return basket


def merge_sort(basket: list) -> None:
  """Sorts a list in ascending order, O(n log n)"""
  if len(basket) == 1:
    return basket

  middle_split = int(len(basket) / 2)
  ls = basket[:middle_split]
  rs = basket[middle_split:]

  lss = merge_sort(ls) 
  rss = merge_sort(rs) 

  for i in range(len(rss)):
    i_value = rss[i] 
    if i_value > lss[-1]:
      return lss + rss[i:]
    else: 
      lss = insertion_sort(lss + rss[i:i+1])
  
  return lss

def quick_sort(basket: list) -> None:
  """Sorts a list in ascending order, O(n log n)"""

  # Base cases
  if len(basket) <= 1:
    return basket

  # Choose random element to order around
  divider_index = randrange(0, len(basket) - 1)
  divider_index = len(basket) - 1
  divider_value = basket[divider_index]

  # Adjustment for shifted list to ensure iteration over all values
  adjustment = 0

  # Iterate through all other items, sorting lower or higher than chosen element
  for i in range(len(basket)):
    j = i + adjustment
    if j == divider_index:
      continue

    value = basket[j]
    if value <= divider_value and j < divider_index:
      continue
    elif value >= divider_value and j > divider_index:
      continue
    elif value > divider_value and j < divider_index:
      basket = basket[0:j] + basket[j+1: divider_index] + [divider_value] + [value] + basket[divider_index+1:]
      divider_index -= 1
      adjustment -= 1
    elif value < divider_value and j > divider_index:
      basket = basket[0:divider_index] + [value] + basket[divider_index:j] + basket[j+1:]
      divider_index += 1
      adjustment += 1  

  # Split partially sorted list about chosen element
  ls = basket[0:divider_index] 
  rs = basket[divider_index+1:]
  # Recursively call for each side and then merge
  lss = quick_sort(ls) 
  rss = quick_sort(rs)

  return lss + [divider_value] + rss





      


