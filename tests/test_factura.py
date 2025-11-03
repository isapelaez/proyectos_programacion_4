import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.producto import Producto


class TestFactura(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Isa", "999")
        self.factura = Factura(self.cliente)

    def test_agregar_producto(self):
        producto = Producto("Insecticida", 8000)
        self.factura.agregar_producto(producto)
        self.assertEqual(len(self.factura.productos), 1)

    def test_calculo_total(self):
        p1 = Producto("Semillas", 3000)
        p2 = Producto("Abono", 7000)
        self.factura.agregar_producto(p1)
        self.factura.agregar_producto(p2)
        self.assertEqual(self.factura.calcular_total(), 10000)

    def test_fecha_automatica(self):
        self.assertIsNotNone(self.factura.fecha)


if __name__ == "__main__":
    unittest.main()
