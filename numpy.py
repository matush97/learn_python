import numpy as np

# array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print(a)

# 2D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print(a)

# Shape
# print(a.shape)

# 3 × 4
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
# print(a.shape)

# Dimensions
# print(a.ndim)

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# print(a.ndim)

# Indexing
print("Indexing")
a = np.array([10, 20, 30, 40, 50])
# print(a[0])

# 2D indexing
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
# print(a[0, 0])

# Slicing
print("Slicing")
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])

# Od zaciatku
# print(a[:3])
# Do konca
# print(a[2:])
# Kazdy druhy
# print(a[::2])
# Opačne
# print(a[::-1])

# Slicing 2D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Vsetky riadky
print(a[:, :])
# Prvý riadok
print(a[0, :])


# Basic operations
# Array + array
# sum()
# mean()
# min()
# max()
# axis
print("axis")
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a.sum(axis=0)) # Sum podľa stĺpcov
print(a.sum(axis=1)) # Sum podľa riadkov

# mean, min, max s axis
# a.mean(axis=1)
# a.min(axis=0)
# a.min(axis=1)
# a.max(axis=0)
# a.max(axis=1)

# TODO
#  14. Celý mini-ťahák

# Toto by som si reálne odložil:

import numpy as np
# Array
a = np.array([1, 2, 3, 4])
# 2D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Rozmery
# a.shape
# a.ndim

# Index
# a[0]
# a[1]
# a[-1]

# 2D:
# a[0, 1]

# Slicing
# a[1:4]
# a[:3]
# a[2:]
# a[::2]
# a[::-1]

# 2D:

# a[0, :]    # riadok
# a[:, 0]    # stĺpec
# a[1:3, :]  # riadky
# a[:, 1:3]  # stĺpce

# Operácie
# a + 10
# a - 10
# a * 10
# a / 10

# Štatistika
# a.sum()
# a.mean()
# a.min()
# a.max()

# alebo:

# np.sum(a)
# np.mean(a)
# np.min(a)
# np.max(a)

# Podľa riadkov/stĺpcov
# a.sum(axis=0)
# a.sum(axis=1)

# a.mean(axis=0)
# a.mean(axis=1)

# a.min(axis=0)
# a.min(axis=1)

# a.max(axis=0)
# a.max(axis=1)