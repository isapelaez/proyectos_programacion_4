class Producto:
    def __init__(self, nombre: str, precio: float):
        if not nombre:
            raise ValueError("El nombre del producto es obligatorio.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.nombre = nombre
        self.precio = float(precio)

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "precio": self.precio
        }

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre='{self.nombre}', precio={self.precio})"
