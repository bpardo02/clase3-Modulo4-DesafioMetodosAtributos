class Pizza:
    ingredientes_vegetales = [
        "tomate",
        "aceitunas",
        "champiñones",
    ]  # Ingredientes vegetales
    ingredientes_proteicos = [
        "pollo",
        "vacuno",
        "carne vegetal",
    ]  # Ingredientes proteicos
    tipos_masa = ["tradicional", "delgada"]  # Tipos de masa
    precio = 10000  # Precio base de la pizza
    tamaño = "familiar"  # Tamaño de la pizza

    def __init__(
        self,
        i_vegetal,
        i_proteico,
        tipo_masa,
    ):
        self.i_vegetal = i_vegetal
        self.i_proteico = i_proteico
        self.tipo_masa = tipo_masa
        self.validez = False

    @staticmethod
    def validar_elemento(elemento, opciones):
        return elemento in opciones

    def realizar_pedido(self):
        self.ingredientes_proteicos = input("Ingrese un ingrediente proteico: ")
        self.ingredientes_vegetales = [
            input("Ingrese el primer ingrediente vegetal: "),
            input("Ingrese el segundo ingrediente vegetal: "),
        ]
        self.tipo_masa = input("Ingrese el tipo de masa: ")

        if (
            Pizza.validar_elemento(
                self.ingredientes_proteicos, Pizza.ingredientes_proteicos
            )
            and all(
                Pizza.validar_elemento(veg, Pizza.ingredientes_vegetales)
                for veg in self.ingredientes_vegetales
            )
            and Pizza.validar_elemento(self.tipo_masa, Pizza.tipos_masa)
        ):
            self.pizza_valida = True
        else:
            self.pizza_valida = False
