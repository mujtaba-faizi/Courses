A = [2, 3, 4, 5, 7, 8, 9, 2, 5]
b=[2]
a = [w*5 for w in A]  # Multiply each element of the list A = {2, 3, 4, 5, 7, 8, 9, 2, 5} with 5
print a
a = [w*5 for w in A if not w in b]  #Multiply each element of the list A = {2, 3, 4, 5, 7, 8, 9, 2, 5}, except 2, with 5
print a
