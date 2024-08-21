# Manual Detallado del Programa de Gestión de Clientes y Alerta de Vencimientos

Este manual describe el funcionamiento, las funcionalidades y la estructura del código del programa diseñado para gestionar una lista de clientes y alertar sobre los vencimientos de sus declaraciones fiscales, basados en el calendario perpetuo de vencimientos de Paraguay(adaptarlo según necesidad :)

# 1. Descripción General del Programa

Este programa permite registrar clientes, calcular sus fechas de vencimiento de acuerdo con el último dígito de su RUC y generar alertas cuando el vencimiento está próximo (dentro de un número de días especificado, por defecto 7 días). Las fechas de vencimiento se ajustan automáticamente si caen en días inhábiles (fines de semana o feriados nacionales en Paraguay).

El programa consta de dos clases principales:

    * 'Cliente': Esta clase representa a un cliente y contiene sus datos personales y su fecha de vencimiento.
    * 'SistemaClientes': Esta clase administra la lista de clientes y proporciona funcionalidades para agregar clientes, mostrar la lista de clientes ordenada por fechas de vencimiento y generar alertas de vencimientos próximos.
    # VISTA PREVIA DE LA EJECUCIÓN:
    
![python3](https://github.com/user-attachments/assets/a6fffb75-84e9-4c86-b22d-883000d2c0de)

# 2. Requisitos Previos

    Lenguaje: Python 3.xx.x.x
    Librerías: La biblioteca estándar de Python es suficiente. No se requiere ninguna biblioteca externa, pero es necesario que el sistema esté configurado para utilizar fechas y tiempos.

# 3. Estructura del Código

 *feriados_paraguay = [*
    *datetime.date(2024, 1, 1),   # Año Nuevo*
    *datetime.date(2024, 3, 1),   # Día de los Héroes*
    *datetime.date(2024, 3, 29),  # Viernes Santo*
    *datetime.date(2024, 5, 1),   # Día del Trabajador*
    *datetime.date(2024, 5, 14),  # Independencia Nacional
    *datetime.date(2024, 6, 12),  # Paz del Chaco*
    *datetime.date(2024, 8, 15),  # Fundación de Asunción*
    *datetime.date(2024, 9, 29),  # Victoria de Boquerón*
    *datetime.date(2024, 12, 8),  # Virgen de Caacupé*
    *datetime.date(2024, 12, 25)  # Navidad*
]

Este bloque de código contiene una lista de fechas que representan los feriados oficiales de Paraguay en el año 2024. Estas fechas son utilizadas para ajustar las fechas de vencimiento cuando caen en días inhábiles.

# Calendario de Vencimientos según el Último Dígito del RUC
 *vencimientos_ruc = {*
    *0: 7,  1: 9,  2: 11,  3: 13,  4: 15,*
    *5: 17, 6: 19, 7: 21, 8: 23, 9: 25*
*}*

# 4. Clases y Funcionalidades
Clase Cliente

Esta clase define la estructura y comportamiento de un cliente.

    Atributos:
        nombre: Nombre del cliente.
        apellido: Apellido del cliente.
        ultimo_digito_ruc: Último dígito del RUC del cliente.
        fecha_vencimiento: Fecha de vencimiento calculada.

    Métodos:

        __init__(self, nombre, apellido, ultimo_digito_ruc): Constructor que inicializa los atributos del cliente y calcula la fecha de vencimiento llamando al método calcular_fecha_vencimiento().

        calcular_fecha_vencimiento(self): Calcula la fecha de vencimiento en función del último dígito del RUC y ajusta la fecha si ya ha pasado el día de vencimiento en el mes actual.

        ajustar_fecha_a_dia_habil(self, fecha): Ajusta la fecha de vencimiento si esta cae en un fin de semana o en un feriado, trasladándola al siguiente día hábil.

        __str__(self): Método especial que devuelve una representación en cadena del cliente, mostrando su nombre y la fecha de vencimiento.

Clase SistemaClientes

Esta clase gestiona los clientes y las operaciones del sistema.

    Atributos:
        clientes: Lista de objetos Cliente.

    Métodos:

        __init__(self): Inicializa la lista vacía de clientes.

        agregar_cliente(self, nombre, apellido, ultimo_digito_ruc): Crea un nuevo cliente y lo agrega a la lista clientes. También imprime un mensaje de confirmación.

        mostrar_clientes(self): Muestra la lista de clientes, ordenados por fecha de vencimiento en orden ascendente.

        alertar_vencimientos_proximos(self, dias=7): Genera una alerta para los clientes cuya fecha de vencimiento está próxima (en los próximos dias días, por defecto 7 días). También muestra a los clientes en orden ascendente de fechas.

# 5. Flujo de Ejecución

    Inicialización del Sistema: Se crea una instancia de la clase SistemaClientes que contiene una lista de clientes vacía.

    Agregar Clientes: Los clientes se agregan al sistema utilizando el método agregar_cliente(). Esto crea un objeto Cliente, calcula su fecha de vencimiento y lo añade a la lista de clientes.

    Mostrar Clientes: Al llamar al método mostrar_clientes(), se muestran todos los clientes registrados en el sistema ordenados por sus fechas de vencimiento en orden ascendente.

    Alerta de Vencimientos Próximos: El método alertar_vencimientos_proximos() genera una lista de clientes que tienen vencimientos en los próximos X días (por defecto 7 días). Estos clientes se ordenan por su fecha de vencimiento de manera ascendente y se muestran al usuario.

# 6. Ejecución del Programa

Al ejecutar el programa, se llamará a la función ejecutar_sistema(), que realiza las siguientes acciones:

    Agrega un conjunto de clientes de ejemplo al sistema.
    Muestra la lista completa de clientes registrados.
    Genera alertas para los clientes con vencimientos próximos.

# 7. Posibles Mejoras

    - Actualización de Feriados: Se podría implementar un mecanismo para cargar automáticamente los feriados de cada año utilizando una  API o fuente externa.
    - Persistencia de Datos: Se podría agregar funcionalidad para guardar y cargar la lista de clientes desde un archivo para mantener  la información entre ejecuciones del programa.
    - Interfaz Gráfica: El sistema podría ser mejorado agregando una interfaz gráfica para hacerlo más fácil de usar y más visualmente intuitivo.
