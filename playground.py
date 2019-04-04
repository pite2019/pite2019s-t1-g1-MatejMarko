import matrix as m

m1 = m.Matrix([[2, 4, 5, 6], [3, 4, 6, 7], [5, 8, 1, 0], [-2, 5, 7, 8]])
m2 = m.Matrix([[1, 4, -5, -2], [1, 5, 6, -4], [7, 1, 0, 8], [4, 0, 4, 5]])

print("m1")
print(m1)

print("m2")
print(m2)

print("m3 = m1 + m2")
m3 = m1 + m2
print(m3)

print("m3 = m1 - m2")
m3 = m1 - m2
print(m3)

print("m4 = m3 @ m1")
m4 = m3 @ m1
print(m4)

print("m3 += m1")
m3 += m1
print(m3)

print("m3 -= m1")
m3 -= m1
print(m3)

print("m3 = m1 + 2")
m3 = m1 + 2
print(m3)

print("m3 = 2 + m1")
m3 = 2 + m1
print(m3)

print("m3 = m2 - 3")
m3 = m2 - 3
print(m3)

print("m3 = 3 - m2")
m3 = 3 - m2
print(m3)
