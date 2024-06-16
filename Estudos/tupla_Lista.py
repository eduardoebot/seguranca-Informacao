#Tuplas são estáticas e não podem ser alteradas. Já listas podem.
tupla = ("t1", "t2", "t3")
lista = ["l1", "l2", "l3"]

lista.append("l4")

print(tupla[:3])
print(lista[:4])

lista[3] = "lista4"

print(lista[:4])