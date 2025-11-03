import json
from datetime import date
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.producto import Producto
from modelo.antibiotico import Antibiotico
from modelo.fertilizante import Fertilizante
from modelo.control_plagas import ControlPlagas

class InterfazTienda:
    def __init__(self):
        self.clientes: list[Cliente] = []
        self.productos: list[Producto] = []
        self.facturas: list[Factura] = []
        self.archivo_datos = "datos/historial.json"
        self.cargar_datos()

    # -------------------------------
    # MÉTODOS DE PERSISTENCIA (JSON)
    # -------------------------------
    def guardar_datos(self):
        data = {
            "clientes": [c.to_dict() for c in self.clientes],
            "facturas": [f.to_dict() for f in self.facturas],
        }
        with open(self.archivo_datos, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, "r", encoding="utf-8") as f:
                data = json.load(f)
                print("✅ Datos cargados correctamente.")
        except FileNotFoundError:
            print("ℹ️ No hay datos previos. Se creará un nuevo archivo.")
            with open(self.archivo_datos, "w") as f:
                json.dump({"clientes": [], "facturas": []}, f)

    # -------------------------------
    # FUNCIONALIDADES
    # -------------------------------
    def registrar_cliente(self):
        nombre = input("Nombre del cliente: ")
        cedula = input("Cédula: ")
        cliente = Cliente(nombre, cedula)
        self.clientes.append(cliente)
        print(f"Cliente '{nombre}' registrado con éxito.")

    def registrar_producto(self):
        print("\nTipos de producto:")
        print("1. Fertilizante")
        print("2. Control de Plagas")
        print("3. Antibiótico")
        tipo = input("Seleccione tipo: ")

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))

        if tipo == "1":
            registro = input("Registro ICA: ")
            frecuencia = int(input("Frecuencia (días): "))
            producto = Fertilizante(nombre, precio, registro, frecuencia, date.today())
        elif tipo == "2":
            registro = input("Registro ICA: ")
            frecuencia = int(input("Frecuencia (días): "))
            carencia = int(input("Periodo de carencia (días): "))
            producto = ControlPlagas(nombre, precio, registro, frecuencia, carencia)
        elif tipo == "3":
            dosis = float(input("Dosis (mg/kg): "))
            animal = input("Tipo de animal (Bovinos/Porcinos/Caprinos): ")
            producto = Antibiotico(nombre, precio, dosis, animal)
        else:
            print("Tipo inválido.")
            return

        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado con éxito.")

    def crear_factura(self):
        if not self.clientes:
            print("Primero debes registrar un cliente.")
            return
        if not self.productos:
            print("No hay productos registrados.")
            return

        cedula = input("Cédula del cliente: ")
        cliente = next((c for c in self.clientes if c.cedula == cedula), None)
        if not cliente:
            print("Cliente no encontrado.")
            return

        factura = Factura(cliente)
        while True:
            print("\nLista de productos:")
            for i, p in enumerate(self.productos):
                print(f"{i+1}. {p.nombre} - ${p.precio}")
            opcion = input("Seleccione un producto (0 para terminar): ")
            if opcion == "0":
                break
            try:
                producto = self.productos[int(opcion) - 1]
                factura.agregar_producto(producto)
            except (ValueError, IndexError):
                print("Selección inválida.")

        if factura.productos:
            cliente.agregar_factura(factura)
            self.facturas.append(factura)
            print(f"\nFactura creada con éxito. Total: ${factura.calcular_total()}")
            self.guardar_datos()
        else:
            print("Factura vacía. No se guardó.")

    def mostrar_historial(self):
        if not self.facturas:
            print("No hay facturas registradas.")
            return
        print("\n=== HISTORIAL DE FACTURAS ===")
        for f in self.facturas:
            print(f)

    # -------------------------------
    # MENÚ PRINCIPAL
    # -------------------------------
    def ejecutar(self):
        while True:
            print("\n=== SISTEMA DE FACTURACIÓN AGRÍCOLA ===")
            print("1. Registrar cliente")
            print("2. Registrar producto")
            print("3. Crear factura")
            print("4. Mostrar historial")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.registrar_producto()
            elif opcion == "3":
                self.crear_factura()
            elif opcion == "4":
                self.mostrar_historial()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
