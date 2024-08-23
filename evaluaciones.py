"""  
Este archivo permite gestionar y realizar pedidos de pizzas utilizando la clase Pizza.  

Se importan ingredientes vegetales y proteicos, junto con tipos de masa y un precio base.  
Se valida si los elementos elegidos para la pizza son correctos y se permite realizar un pedido.  

Uso:  
1. Se importan las clases y atributos de Pizza.  
2. Se imprimen los ingredientes y características de la pizza por defecto.  
3. Se valida un ingrediente específico.  
4. Se crea una instancia de Pizza con ingredientes y masa.  
5. Se imprime información sobre la pizza personalizada creada.  

Atributos:  
- ingredientes_vegetales: Lista de ingredientes vegetales disponibles.  
- ingredientes_proteicos: Lista de ingredientes proteicos disponibles.  
- tipos_masa: Lista de tipos de masa disponibles.  
- precio: Precio base de la pizza.  
- tamaño: Tamaño de la pizza.  

Métodos:  
- validar_elemento: Valida si un ingrediente está en una lista de ingredientes permitidos.  
- realizar_pedido: Método que ejecuta el proceso de pedido para la pizza elegida.  
""" 
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
