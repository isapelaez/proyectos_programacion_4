from __future__ import annotations
from typing import List, TYPE_CHECKING
from datetime import date
from .producto import Producto

if TYPE_CHECKING:
    from .cliente import Cliente


class Factura:
    def __init__(self, cliente: Cliente):
        self.fecha = date.today()
        self.cliente = cliente
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def calcular_total(self) -> float:
        return sum(p.precio for p in self.productos)

    def to_dict(self):
        return {
            "fecha": str(self.fecha),
            "cliente": self.cliente.nombre,
            "productos": [p.to_dict() for p in self.productos],
            "total": self.calcular_total(),
        }

    def __repr__(self):
        return (
            f"Factura(fecha={self.fecha}, cliente='{self.cliente.nombre}', "
            f"productos={len(self.productos)}, total={self.calcular_total()})"
        )
