
# 1. **add()**: Adds an element to the set.

set = {1, 2, 3}
set.add(4)
print(set)  # Output: {1, 2, 3, 4}

# 2. **clear()**: Removes all the elements from the set, making it empty.

set = {1, 2, 3}
set.clear()
print(set)  # Output: set()

# 3. **copy()**: Returns a shallow copy of the set.

set = {1, 2, 3}
new_set = set.copy()

# 4. **difference()**: Returns a new set containing the difference between two or more sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}

# 5. **difference_update()**: Removes the items in this set that are also included in another specified set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

# 6. **discard()**: Removes the specified item from the set if it exists; otherwise, does nothing.

set = {1, 2, 3}
set.discard(2)
print(set)  # Output: {1, 3}

# 7. **intersection()**: Returns a new set that is the intersection of two or more sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}

# 8. **intersection_update()**: Removes the items in this set that are not present in other specified set(s).

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3}

# 9. **isdisjoint()**: Returns `True` if two sets have no intersection, i.e., they are disjoint.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

# 10. **issubset()**: Returns `True` if another set contains this set.

set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = set1.issubset(set2)
print(result)  # Output: True

# 11. **issuperset()**: Returns `True` if this set contains another set.
 
set1 = {1, 2, 3, 4}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True
 
# 12. **pop()**: Removes and returns an arbitrary element from the set.


set = {1, 2, 3}
popped_element = set.pop()
 
# 13. **remove()**: Removes the specified element from the set; raises an error if the element is not found.


set = {1, 2, 3}
set.remove(2)
print(set)  # Output: {1, 3}


# 14. **symmetric_difference()**: Returns a new set with the symmetric differences of two sets.
 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 4, 5}


# 15. **symmetric_difference_update()**: Updates the set with the symmetric differences from this set and another.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}

# 16. **union()**: Returns a new set containing the union of sets (all distinct elements from all sets).

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}

# 17. **update()**: Updates the set with elements from another set or any other iterable.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
