from .producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, precio: float, dosis: float, tipo_animal: str):
        super().__init__(nombre, precio)
        if dosis <= 0:
            raise ValueError("La dosis debe ser positiva.")
        if tipo_animal not in ["Bovinos", "Porcinos", "Caprinos"]:
            raise ValueError("El tipo de animal debe ser 'Bovinos', 'Porcinos' o 'Caprinos'.")
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "dosis": self.dosis,
            "tipo_animal": self.tipo_animal
        })
        return data
