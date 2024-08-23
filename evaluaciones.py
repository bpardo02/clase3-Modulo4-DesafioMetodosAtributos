from pizza import Pizza

print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Ingredientes proteicos:", Pizza.ingredientes_proteicos)
print("Tipos de masa:", Pizza.tipos_masa)
print("Precio base:", Pizza.precio)
print("Tamaño:", Pizza.tamaño)

print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

mi_pizza = Pizza("tomate", "pollo", "tradicional")
mi_pizza.realizar_pedido()

print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Ingrediente proteico:", mi_pizza.ingredientes_proteicos)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Es una pizza válida?", mi_pizza.pizza_valida)

# print(Pizza.pizza_valida)
