import datetime

# Creamos un Lista de feriados en Paraguay (2024) ----> actualizar para cada año si hace falta
feriados_paraguay = [
    datetime.date(2024, 1, 1),   # Año Nuevo
    datetime.date(2024, 3, 1),   # Día de los Héroes
    datetime.date(2024, 3, 29),  # Viernes Santo
    datetime.date(2024, 5, 1),   # Día del Trabajador
    datetime.date(2024, 5, 14),  # Independencia Nacional
    datetime.date(2024, 6, 12),  # Paz del Chaco
    datetime.date(2024, 8, 15),  # Fundación de Asunción
    datetime.date(2024, 9, 29),  # Victoria de Boquerón
    datetime.date(2024, 12, 8),  # Virgen de Caacupé
    datetime.date(2024, 12, 25), # Navidad
]

# Creamos un Diccionario con fechas de vencimiento fijas para cada último dígito del RUC
# Donde manejamos para cada valor lo siguiente: Eje.: 0:7 Donde el 0 es la CLAVE y el 7 es el VALOR
vencimientos_ruc = {
    0: 7,  1: 9,  2: 11,  3: 13,  4: 15,
    5: 17, 6: 19, 7: 21, 8: 23, 9: 25
}

#Definimos una calse Cliente con las funciones para cada caso( __init__ ,calcular_fecha_vencimiento, ajustar_fecha_a_dia_habil, __str__):
# Aquí creamos los Objetos (Atributos y Métodos)
class Cliente:
    def __init__(self, nombre, apellido, ultimo_digito_ruc):  ## Creamos un constructor para asignar los valores
        self.nombre = nombre
        self.apellido = apellido
        self.ultimo_digito_ruc = ultimo_digito_ruc
        self.fecha_vencimiento = self.calcular_fecha_vencimiento()

    def calcular_fecha_vencimiento(self):
        """Calcula la fecha de vencimiento basándose en el último dígito del RUC."""
        dia_vencimiento = vencimientos_ruc[self.ultimo_digito_ruc]
        hoy = datetime.date.today()
        # Generamos fecha de vencimiento para este mes
        fecha_vencimiento = datetime.date(hoy.year, hoy.month, dia_vencimiento)
    
        # Si ya ha pasado este mes, calculamos para el próximo mes
        if fecha_vencimiento < hoy:
            mes_siguiente = hoy.month + 1 if hoy.month < 12 else 1
            año_siguiente = hoy.year if mes_siguiente > 1 else hoy.year + 1
            fecha_vencimiento = datetime.date(año_siguiente, mes_siguiente, dia_vencimiento)
            
        return self.ajustar_fecha_a_dia_habil(fecha_vencimiento)
    # Ajustamos si la fecha cae en un día inhábil
    def ajustar_fecha_a_dia_habil(self, fecha):
        """Ajustamos la fecha de vencimiento al siguiente día hábil si cae en un día inhábil."""
        while fecha.weekday() >= 5 or fecha in feriados_paraguay:  # 5 y 6 son sábado y domingo
            fecha += datetime.timedelta(days=1)
        return fecha

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Fecha de vencimiento: {self.fecha_vencimiento.strftime('%d/%m/%Y')}"
    
    
# Agregamos una clase SistemaClientes con las funciones:  __init__,agregar_clientes, mostrar_clientes, alertar_vencimientos_proximos.
class SistemaClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre, apellido, ultimo_digito_ruc):
        cliente = Cliente(nombre, apellido, ultimo_digito_ruc)
        self.clientes.append(cliente)
        print(f"Cliente {nombre} {apellido} agregado exitosamente.")

    def mostrar_clientes(self):
        """Muestra la lista de clientes ordenada por fecha de vencimiento."""
        clientes_ordenados = sorted(self.clientes, key=lambda c: c.fecha_vencimiento)
        for cliente in clientes_ordenados:
            print(cliente)

    def alertar_vencimientos_proximos(self, dias=7):
        """Genera una alerta para los clientes cuya fecha de vencimiento esté a X días o menos."""
        hoy = datetime.date.today()
        clientes_con_alerta = [
            cliente for cliente in self.clientes
            if 0 <= (cliente.fecha_vencimiento - hoy).days <= dias
        ]
        
        # Ordenamos los clientes con vencimiento próximo por fecha de vencimiento ascendente
        clientes_con_alerta_ordenados = sorted(clientes_con_alerta, key=lambda c: c.fecha_vencimiento)
        
        print(f"\nClientes con vencimientos próximos (en los próximos {dias} días):")
        if clientes_con_alerta_ordenados:
            for cliente in clientes_con_alerta_ordenados:
                print(cliente)
        else:
            print("No hay cliente con vencimientos próximos.")

# Función para ejecutar el sistema
def ejecutar_sistema():
    sistema = SistemaClientes()
    
    # Ejemplo de clientes para agregar(agregar segun necesidad)
    sistema.agregar_cliente("Juan", "Pérez", 5)
    sistema.agregar_cliente("Ana", "García", 9)
    sistema.agregar_cliente("Luis", "Rodríguez", 1)
    sistema.agregar_cliente("Jose", "Benitez", 0)
    sistema.agregar_cliente("Alberto", "Gomez", 0)
    sistema.agregar_cliente("Patricia", "Romero", 5)
    sistema.agregar_cliente("Felicia", "Gonzalez", 9)
    sistema.agregar_cliente("Reimundo", "Palacios", 9)
    sistema.agregar_cliente("Elena", "Ramirez", 2)
    sistema.agregar_cliente("Jose Alberto", "Rodríguez Gutierrez", 8)
    
    # Mostrar clientes
    print("\nClientes registrados:")
    sistema.mostrar_clientes()

    # Mostrar alertas de vencimientos próximos
    sistema.alertar_vencimientos_proximos()

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_sistema()
    

"""Lo que con mucho trabajo se adquiere, más se ama.
                Aristóteles."""

