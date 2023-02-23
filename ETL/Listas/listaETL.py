"""
Adicionando itens na lista com for
"""


lst = [1, 10, 7, 9, 2, 55]

# for elemento in range(4):
#     if elemento != 0:
#         lst.append(elemento)
#     print(lst)

lst2 = ['a', 2, 'dwa']

# print(lst2)

lst3 = [1, [2, 3]]
# print(lst3[1][1])

lst4 = [1, (2, 3)]
# print(lst4)

lst5 = ['a', 2, 3, 'dsdd', [1, 2, 3]]

# print(lst3 + lst4)

# print(lst4 * 3)

# print('a' in lst2)

lst2.pop()
print(lst2)

lst5.remove('dsdd')
print(lst5)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)