from .producto import Producto

class ProductoDeControl(Producto):
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_dias: int):
        super().__init__(nombre, precio)
        if not registro_ica:
            raise ValueError("El registro ICA es obligatorio.")
        if frecuencia_dias <= 0:
            raise ValueError("La frecuencia debe ser positiva.")
        self.registro_ica = registro_ica
        self.frecuencia_dias = frecuencia_dias

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "registro_ica": self.registro_ica,
            "frecuencia_dias": self.frecuencia_dias
        })
        return data
