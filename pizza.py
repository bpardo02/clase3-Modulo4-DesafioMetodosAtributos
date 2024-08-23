class Pizza:
    """  
    Clase que representa una pizza con ingredientes vegetales y proteicos,   
    tipos de masa, y funcionalidad para realizar un pedido.  

    Atributos:  
    ----------  
    ingredientes_vegetales : list  
        Lista de ingredientes vegetales disponibles.  
    ingredientes_proteicos : list  
        Lista de ingredientes proteicos disponibles.  
    tipos_masa : list  
        Lista de tipos de masa disponibles.  
    precio : float  
        Precio base de la pizza.  
    tamaño : str  
        Tamaño de la pizza.  
    
    Métodos:  
    --------  
    validar_elemento(elemento, opciones):  
        Valida si el elemento está dentro de las opciones permitidas.  
    realizar_pedido():  
        Proceso para realizar un pedido de pizza a través de entradas del usuario.  
    """  
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
        """  
        Inicializa una instancia de la clase Pizza.  
        
        Parámetros:  
        ----------  
        i_vegetal : str  
            Ingrediente vegetal seleccionado.  
        i_proteico : str  
            Ingrediente proteico seleccionado.  
        tipo_masa : str  
            Tipo de masa para la pizza.  
        """  
        self.i_vegetal = i_vegetal
        self.i_proteico = i_proteico
        self.tipo_masa = tipo_masa
        self.validez = False

    @staticmethod
    def validar_elemento(elemento, opciones):
        """  
        Valida si un elemento está en la lista de opciones posibles.  
        
        Parámetros:  
        ----------  
        elemento : str  
            Elemento a validar.  
        opciones : list  
            Lista de opciones válidas.  

        Retorna:  
        --------  
        bool  
            True si el elemento está en opciones, False en caso contrario.  
        """ 
        return elemento in opciones

    def realizar_pedido(self):
        """  
        Solicita al usuario los ingredientes y tipo de masa, valida los  
        ingresos, y establece si la pizza es válida.  
        """
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
