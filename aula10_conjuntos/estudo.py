


conjunto1 = {1,2,3}
conjunto2 = {3,4,5,6}

conjunto_uniao = conjunto1 | conjunto2
conjunto_inter = conjunto1 & conjunto2
print(conjunto_uniao)
print(conjunto_inter)



set = {1,2}
set.update([3, 4, 5, 6])
print(f"--> {set}")


set1 = {1,2,3,4}
set2 = {1,1,1,2,3,4}

if set1 == set2:
    print('set1 é igual a set2')