from datetime import date
from .producto_control import ProductoDeControl

class Fertilizante(ProductoDeControl):
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_dias: int, fecha_ultima_aplicacion: date):
        super().__init__(nombre, precio, registro_ica, frecuencia_dias)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "fecha_ultima_aplicacion": str(self.fecha_ultima_aplicacion)
        })
        return data
