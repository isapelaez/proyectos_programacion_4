import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.producto import Producto


class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Isabella", "123")

    def test_creacion_cliente(self):
        self.assertEqual(self.cliente.nombre, "Isabella")
        self.assertEqual(self.cliente.cedula, "123")
        self.assertEqual(len(self.cliente.facturas), 0)

    def test_agregar_factura(self):
        factura = Factura(self.cliente)
        producto = Producto("Semillas", 5000)
        factura.agregar_producto(producto)
        self.cliente.agregar_factura(factura)
        self.assertEqual(len(self.cliente.facturas), 1)

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Cliente("", "123")

    def test_cedula_vacia(self):
        with self.assertRaises(ValueError):
            Cliente("Isabella", "")


if __name__ == "__main__":
    unittest.main()
