from .producto_control import ProductoDeControl

class ControlPlagas(ProductoDeControl):
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_dias: int, periodo_carencia: int):
        super().__init__(nombre, precio, registro_ica, frecuencia_dias)
        if periodo_carencia < 0:
            raise ValueError("El periodo de carencia no puede ser negativo.")
        self.periodo_carencia = periodo_carencia

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "periodo_carencia": self.periodo_carencia
        })
        return data
