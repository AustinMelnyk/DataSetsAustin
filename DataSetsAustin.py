# =========================
# 1. LISTS
# Summary: Ordered, mutable collection of items. Supports indexing, slicing, and many built-in methods.
# =========================

L = [1, 2, 3, 4, 5]  # Create a list with 5 elements
L.append(6)  # Add 6 to the end of the list
print(L)  # Print full list → [1, 2, 3, 4, 5, 6]

print(L[0])  # Access first element (index 0) → 1
print(L[1:4])  # Slice from index 1 up to (not including) 4 → [2, 3, 4]

# Example 2: Removing an element
L.remove(4)  # Removes the value 4 from the list
print(L)  # After removal → [1, 2, 3, 5, 6]

# =========================
# 2. STRINGS
# Summary: Immutable sequence of characters. Supports indexing, slicing, and string methods.
# =========================

s = "Hello World"  # Create a string
print(s[0])  # First character → 'H'
print(s[0:5])  # Slice first 5 characters → 'Hello'
print(s.count('l'))  # Count occurrences of 'l' → 3

# Example 2: Splitting a string
greeting_parts = s.split(' ')  # Splits the string into ['Hello', 'World']
print(greeting_parts)  # → ['Hello', 'World']

# =========================
# 3. DICTIONARIES
# Summary: Key-value mapping. Fast lookup by key. Mutable.
# =========================

d = {'apple': 2, 'pear': 3}  # Create dictionary with two key-value pairs
d['banana'] = 5  # Add new key-value pair

print(d['apple'])  # Access value by key → 2

for k, v in d.items():
    print(k, v)  # Print each key and its value → 'apple 2', 'pear 3', 'banana 5'

# Example 2: Removing a key-value pair
d.pop('pear')  # Removes 'pear' from the dictionary
print(d)  # After removal → {'apple': 2, 'banana': 5}

# =========================
# 4. TUPLES
# Summary: Ordered, immutable collection. Often used for fixed data or unpacking.
# =========================

t = (1, 2, 3)  # Create tuple
print(t[0])  # Access first element → 1

fruit, kind, price = ('apple', 'fruit', 2.99)  # Unpack tuple into variables
print(fruit, kind, price)  # Print unpacked values → 'apple fruit 2.99'

# Example 2: Nested tuples
nested_t = ((1, 2), (3, 4))
print(nested_t[1][0])  # Access element → 3

# =========================
# 5. SETS
# Summary: Unordered collection of unique elements (no duplicates).
# =========================

s = {1, 2, 3, 3}  # Duplicate '3' is automatically removed
print(s)  # → {1, 2, 3}

s.add(4)  # Add element to set
print(s)  # → {1, 2, 3, 4}

s2 = {3, 4, 5}  # Another set
print(s & s2)  # Intersection (common elements) → {3, 4}

# Example 2: Difference between sets
print(s - s2)  # Elements in s but not in s2 → {1, 2}

# =========================
# 6. LIST COMPREHENSIONS
# Summary: Compact way to build lists using a loop + optional condition.
# =========================

L = [1, 2, 3, 4, 5]  # Base list

squared = [x**2 for x in L]  # Square each element
print(squared)  # → [1, 4, 9, 16, 25]

filtered = [x for x in L if x > 3]  # Keep only values > 3
print(filtered)  # → [4, 5]

# Example 2: Nested list comprehension
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)  # → [(0, 0), (0, 1), (1, 0), (1, 1)]

# =========================
# 7. DICTIONARY COMPREHENSIONS
# Summary: Compact way to create dictionaries from iterables.
# =========================

d = {'apple': 2, 'pear': 3}  # Original dictionary

doubled = {k.upper(): v*2 for k, v in d.items()}  # Transform keys and values
print(doubled)  # → {'APPLE': 4, 'PEAR': 6}

# Example 2: Filtering items
filtered_dict = {k: v for k, v in d.items() if v > 2}
print(filtered_dict)  # → {'pear': 3}

# =========================
# 8. ITERATION & MEMBERSHIP
# Summary: Loop through collections and test if a value exists in them.
# =========================

L = [1, 2, 3]  # List to iterate over

for n in L:  # Loop through each element
    print(n)  # Print each value → 1, 2, 3

print(2 in L)  # Check membership → True

# Example 2: Using enumerate to track index
for idx, value in enumerate(L):
    print(idx, value)  # → 0 1, 1 2, 2 3

# =========================
# 9. NESTED DATA STRUCTURES
# Summary: Combining different collections.
# =========================
nested = {'numbers': [1, 2, 3], 'letters': {'a': 1, 'b': 2}}
print(nested['letters']['a'])  # Access nested value → 1

# Example 2: Modifying nested structures
nested['numbers'].append(4)
print(nested)  # → {'numbers': [1, 2, 3, 4], 'letters': {'a': 1, 'b': 2}}