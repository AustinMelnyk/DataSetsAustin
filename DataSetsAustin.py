# =========================
# 1. LISTS
# Summary: Ordered, mutable collection of items. Supports indexing, slicing, and many built-in methods.
# =========================

L = [1, 2, 3, 4, 5]          # Create a list with 5 elements
L.append(6)                  # Add 6 to the end of the list
print(L)                     # Print full list → [1, 2, 3, 4, 5, 6]

print(L[0])                  # Access first element (index 0) → 1
print(L[1:4])                # Slice from index 1 up to (not including) 4 → [2, 3, 4]


# =========================
# 2. STRINGS
# Summary: Immutable sequence of characters. Supports indexing, slicing, and string methods.
# =========================

s = "Hello World"            # Create a string
print(s[0])                  # First character → 'H'
print(s[0:5])                # Slice first 5 characters → 'Hello'
print(s.count('l'))          # Count occurrences of 'l' → 3


# =========================
# 3. DICTIONARIES
# Summary: Key-value mapping. Fast lookup by key. Mutable.
# =========================

d = {'apple': 2, 'pear': 3}  # Create dictionary with two key-value pairs
d['banana'] = 5              # Add new key-value pair

print(d['apple'])            # Access value by key → 2

for k, v in d.items():       # Loop through key-value pairs
    print(k, v)              # Print each key and its value


# =========================
# 4. TUPLES
# Summary: Ordered, immutable collection. Often used for fixed data or unpacking.
# =========================

t = (1, 2, 3)                # Create tuple
print(t[0])                  # Access first element → 1

fruit, kind, price = ('apple', 'fruit', 2.99)  # Unpack tuple into variables
print(fruit, kind, price)   # Print unpacked values


# =========================
# 5. SETS
# Summary: Unordered collection of unique elements (no duplicates).
# =========================

s = {1, 2, 3, 3}             # Duplicate '3' is automatically removed
print(s)                     # → {1, 2, 3}

s.add(4)                     # Add element to set
print(s)                     # → {1, 2, 3, 4}

s2 = {3, 4, 5}               # Another set
print(s & s2)                # Intersection (common elements) → {3, 4}


# =========================
# 6. LIST COMPREHENSIONS
# Summary: Compact way to build lists using a loop + optional condition.
# =========================

L = [1, 2, 3, 4, 5]          # Base list

squared = [x**2 for x in L]  # Square each element → [1, 4, 9, 16, 25]
print(squared)

filtered = [x for x in L if x > 3]  # Keep only values > 3 → [4, 5]
print(filtered)


# =========================
# 7. DICTIONARY COMPREHENSIONS
# Summary: Compact way to create dictionaries from iterables.
# =========================

d = {'apple': 2, 'pear': 3}  # Original dictionary

doubled = {k.upper(): v*2 for k, v in d.items()}  # Transform keys and values
print(doubled)              # → {'APPLE': 4, 'PEAR': 6}


# =========================
# 8. ITERATION & MEMBERSHIP
# Summary: Loop through collections and test if a value exists in them.
# =========================

L = [1, 2, 3]               # List to iterate over

for n in L:                 # Loop through each element
    print(n)                # Print each value

print(2 in L)               # Check membership → True