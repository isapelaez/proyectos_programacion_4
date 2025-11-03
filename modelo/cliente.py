from __future__ import annotations
from typing import TYPE_CHECKING

# Importacion condicional: evita circular imports
if TYPE_CHECKING:
    from .factura import Factura


class Cliente:
    def __init__(self, nombre: str, cedula: str):
        if not nombre or not cedula:
            raise ValueError("Nombre y cedula son obligatorios.")
        self.nombre = nombre
        self.cedula = cedula
        self.facturas: list[Factura] = []

    def agregar_factura(self, factura: Factura):
        self.facturas.append(factura)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "facturas": [f.to_dict() for f in self.facturas],
        }

    def __repr__(self):
        return f"Cliente(nombre='{self.nombre}', cedula='{self.cedula}', facturas={len(self.facturas)})"
