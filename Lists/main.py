
# 1. **append()**: Adds an element at the end of the list.

list = [1, 2, 3]
list.append(4)
print(list)  # Output: [1, 2, 3, 4]


# 2. **clear()**: Removes all the elements from the list, making it empty.

list = [1, 2, 3]
list.clear()
print(list)  # Output: []


# 3. **copy()**: Returns a shallow copy of the list.

list = [1, 2, 3]
new_list = list.copy()


# 4. **count()**: Returns the number of elements with the specified value.

list = [1, 2, 2, 3, 4, 2]
count = list.count(2)
print(count)  # Output: 3


# 5. **extend()**: Add the elements of a list (or any iterable) to the end of the current list.

list = [1, 2, 3]
extension = [4, 5, 6]
list.extend(extension)
print(list)  # Output: [1, 2, 3, 4, 5, 6]


# 6. **index()**: Returns the index of the first element with the specified value.

list = [1, 2, 3, 4, 3]
index = list.index(3)
print(index)  # Output: 2


# 7. **insert()**: Adds an element at the specified position.

list = [1, 2, 3]
list.insert(1, 4)
print(list)  # Output: [1, 4, 2, 3]


# 8. **pop()**: Removes the element at the specified position and returns it.

list = [1, 2, 3, 4]
popped_element = list.pop(2)
print(popped_element)  # Output: 3


# 9. **remove()**: Removes the first item with the specified value.

list = [1, 2, 3, 4, 2]
list.remove(2)
print(list)  # Output: [1, 3, 4, 2]


# 10. **reverse()**: Reverses the order of the list in-place.


list = [1, 2, 3]
list.reverse()
print(list)  # Output: [3, 2, 1]


# 11. **sort()**: Sorts the list in ascending order in-place. It can also take a `key` argument for custom sorting.


list = [4, 1, 3, 2]
list.sort()
print(list)  # Output: [1, 2, 3, 4]
 