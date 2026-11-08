lst = [[1,2],[3,4]]
a = lst
a[0][0] = 0 # lst also sees the change
print(lst)