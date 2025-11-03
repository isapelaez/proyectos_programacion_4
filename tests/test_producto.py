import unittest
from modelo.producto import Producto


class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        p = Producto("Fertilizante", 12000)
        self.assertEqual(p.nombre, "Fertilizante")
        self.assertEqual(p.precio, 12000)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            Producto("Abono", -5000)

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Producto("", 3000)


if __name__ == "__main__":
    unittest.main()
