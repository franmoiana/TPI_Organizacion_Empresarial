import csv
import os
from datetime import datetime


# ==============================
# Constantes generales
# ==============================
SEPARADOR_CSV = ";"
ARCHIVO_SOLUCIONES = "soluciones.csv"
ARCHIVO_TICKETS = "tickets.csv"

# Estados principales de la conversación.
# En una implementación real en Telegram, estos estados permitirían recordar
# en qué paso se encuentra cada usuario.
ESTADO_INICIO = "INICIO"
ESTADO_SELECCIONAR_CATEGORIA = "SELECCIONAR_CATEGORIA"
ESTADO_SELECCIONAR_PROBLEMA = "SELECCIONAR_PROBLEMA"
ESTADO_MOSTRAR_SOLUCION = "MOSTRAR_SOLUCION"
ESTADO_CONFIRMAR_RESOLUCION = "CONFIRMAR_RESOLUCION"
ESTADO_SOLICITAR_DESCRIPCION = "SOLICITAR_DESCRIPCION"
ESTADO_CREAR_TICKET = "CREAR_TICKET"
ESTADO_FIN = "FIN"

CATEGORIAS = [
    "Internet",
    "Correo electrónico",
    "Impresoras",
    "Contraseñas",
    "Acceso a sistemas",
]

# Base de conocimientos inicial. Si soluciones.csv no existe, se crea con estos datos.
SOLUCIONES_INICIALES = [
    {
        "id_solucion": "1",
        "categoria": "Internet",
        "problema": "Sin conexión a internet",
        "solucion": "Verifique que el cable de red o la conexión Wi-Fi estén activos. Reinicie el equipo y compruebe si otros usuarios tienen conexión.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "2",
        "categoria": "Internet",
        "problema": "Conexión lenta",
        "solucion": "Cierre aplicaciones que consuman ancho de banda, reinicie la conexión Wi-Fi y pruebe acceder desde otro navegador.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "3",
        "categoria": "Internet",
        "problema": "No accede a la VPN",
        "solucion": "Confirme que tiene conexión a internet, abra nuevamente el cliente VPN e ingrese sus credenciales corporativas.",
        "prioridad_sugerida": "Alta",
    },
    {
        "id_solucion": "4",
        "categoria": "Correo electrónico",
        "problema": "No puede ingresar al correo",
        "solucion": "Verifique usuario y contraseña. Confirme que la cuenta no esté bloqueada e intente restablecer la contraseña desde el portal interno.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "5",
        "categoria": "Correo electrónico",
        "problema": "No recibe correos",
        "solucion": "Revise la carpeta de spam, confirme que el buzón no esté lleno y actualice la bandeja de entrada.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "6",
        "categoria": "Correo electrónico",
        "problema": "No puede enviar correos",
        "solucion": "Revise la conexión a internet, verifique los destinatarios y confirme que no haya adjuntos demasiado grandes.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "7",
        "categoria": "Impresoras",
        "problema": "La impresora no imprime",
        "solucion": "Verifique que la impresora esté encendida, tenga papel, tinta o tóner, y aparezca seleccionada como impresora predeterminada.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "8",
        "categoria": "Impresoras",
        "problema": "Documento trabado en cola de impresión",
        "solucion": "Cancele los documentos pendientes, reinicie la impresora y vuelva a enviar el archivo.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "9",
        "categoria": "Impresoras",
        "problema": "La impresión sale con manchas",
        "solucion": "Ejecute la limpieza de cabezales desde el panel de impresión y verifique el nivel de tóner o tinta.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "10",
        "categoria": "Contraseñas",
        "problema": "Olvido de contraseña",
        "solucion": "Use el portal de autoservicio para restablecer la contraseña con su usuario corporativo y segundo factor de autenticación.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "11",
        "categoria": "Contraseñas",
        "problema": "Cuenta bloqueada",
        "solucion": "Espere el tiempo de desbloqueo automático o solicite al área de soporte la validación de identidad para desbloquear la cuenta.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "12",
        "categoria": "Contraseñas",
        "problema": "Cambio preventivo de contraseña",
        "solucion": "Ingrese al portal corporativo, seleccione Seguridad y luego la opción Cambiar contraseña.",
        "prioridad_sugerida": "Baja",
    },
    {
        "id_solucion": "13",
        "categoria": "Acceso a sistemas",
        "problema": "No puede ingresar al sistema interno",
        "solucion": "Confirme que usa el enlace correcto, cierre sesión, borre caché del navegador e intente nuevamente.",
        "prioridad_sugerida": "Alta",
    },
    {
        "id_solucion": "14",
        "categoria": "Acceso a sistemas",
        "problema": "No tiene permisos suficientes",
        "solucion": "Solicite a su responsable que apruebe el acceso mediante el formulario interno de permisos.",
        "prioridad_sugerida": "Media",
    },
    {
        "id_solucion": "15",
        "categoria": "Acceso a sistemas",
        "problema": "El sistema muestra error",
        "solucion": "Actualice la página, pruebe en otro navegador y tome una captura del mensaje de error si el problema continúa.",
        "prioridad_sugerida": "Media",
    },
]


# ==============================
# Manejo de archivos CSV
# ==============================
def obtener_ruta_archivo(nombre_archivo):
    """Devuelve la ruta absoluta de un archivo dentro de la carpeta del proyecto."""
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(carpeta_actual, nombre_archivo)


def crear_soluciones_si_no_existen():
    """Crea soluciones.csv si no existe, sin sobrescribir datos existentes."""
    ruta_soluciones = obtener_ruta_archivo(ARCHIVO_SOLUCIONES)

    if os.path.exists(ruta_soluciones):
        return

    campos = ["id_solucion", "categoria", "problema", "solucion", "prioridad_sugerida"]
    with open(ruta_soluciones, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=SEPARADOR_CSV)
        escritor.writeheader()
        escritor.writerows(SOLUCIONES_INICIALES)


def crear_tickets_si_no_existen():
    """Crea tickets.csv si no existe, sin borrar registros anteriores."""
    ruta_tickets = obtener_ruta_archivo(ARCHIVO_TICKETS)

    if os.path.exists(ruta_tickets):
        return

    campos = [
        "id_ticket",
        "fecha_creacion",
        "empleado",
        "categoria",
        "problema",
        "descripcion",
        "prioridad",
        "estado",
    ]
    with open(ruta_tickets, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=SEPARADOR_CSV)
        escritor.writeheader()


def inicializar_archivos():
    """Inicializa la base de datos simulada del proyecto."""
    crear_soluciones_si_no_existen()
    crear_tickets_si_no_existen()


def leer_soluciones():
    """Lee la base de conocimientos desde soluciones.csv."""
    ruta_soluciones = obtener_ruta_archivo(ARCHIVO_SOLUCIONES)

    with open(ruta_soluciones, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter=SEPARADOR_CSV)
        return list(lector)


# ==============================
# Funciones de interacción
# ==============================
def mostrar_opciones(titulo, opciones):
    """Muestra una lista numerada de opciones."""
    print(f"\n{titulo}")
    for indice, opcion in enumerate(opciones, start=1):
        print(f"{indice}. {opcion}")


def pedir_opcion(mensaje, cantidad_opciones):
    """Solicita una opción numérica y valida que esté dentro del rango."""
    while True:
        opcion = input(mensaje).strip()

        if not opcion.isdigit():
            print("Error: ingrese una opción numérica.")
            continue

        numero_opcion = int(opcion)

        if numero_opcion < 1 or numero_opcion > cantidad_opciones:
            print("Error: la opción ingresada no es válida.")
            continue

        return numero_opcion


def pedir_nombre_empleado():
    """Pide el nombre del empleado que inicia el proceso de soporte."""
    while True:
        nombre = input("\nIngrese su nombre y apellido: ").strip()

        if nombre:
            return nombre

        print("Error: el nombre del empleado no puede estar vacío.")


def pedir_respuesta_si_no(mensaje):
    """Valida una respuesta afirmativa o negativa."""
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta in ("si", "sí"):
            return True

        if respuesta == "no":
            return False

        print("Error: responda sí o no.")


def pedir_descripcion():
    """Solicita una descripción del problema para poder generar el ticket."""
    while True:
        descripcion = input("Describa brevemente qué ocurre para registrar el ticket: ").strip()

        if descripcion:
            return descripcion

        print("Error: la descripción no puede estar vacía.")


# ==============================
# Lógica del chatbot
# ==============================
def obtener_problemas_por_categoria(soluciones, categoria):
    """Filtra los problemas frecuentes según la categoría seleccionada."""
    problemas = []

    for solucion in soluciones:
        if solucion["categoria"] == categoria:
            problemas.append(solucion["problema"])

    return problemas


def buscar_solucion(soluciones, categoria, problema):
    """Busca la solución asociada a una categoría y problema."""
    for solucion in soluciones:
        if solucion["categoria"] == categoria and solucion["problema"] == problema:
            return solucion

    return None


def obtener_siguiente_id_ticket():
    """Calcula el siguiente identificador de ticket de manera incremental."""
    ruta_tickets = obtener_ruta_archivo(ARCHIVO_TICKETS)
    ultimo_id = 0

    with open(ruta_tickets, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter=SEPARADOR_CSV)

        for ticket in lector:
            id_ticket = ticket.get("id_ticket", "")

            if id_ticket.isdigit():
                ultimo_id = max(ultimo_id, int(id_ticket))

    return ultimo_id + 1


def generar_ticket(empleado, categoria, problema, descripcion, prioridad):
    """Agrega un nuevo ticket al archivo tickets.csv sin borrar los anteriores."""
    ruta_tickets = obtener_ruta_archivo(ARCHIVO_TICKETS)
    id_ticket = obtener_siguiente_id_ticket()
    fecha_creacion = datetime.now().strftime("%Y-%m-%d")

    nuevo_ticket = {
        "id_ticket": str(id_ticket),
        "fecha_creacion": fecha_creacion,
        "empleado": empleado,
        "categoria": categoria,
        "problema": problema,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Abierto",
    }

    campos = [
        "id_ticket",
        "fecha_creacion",
        "empleado",
        "categoria",
        "problema",
        "descripcion",
        "prioridad",
        "estado",
    ]
    with open(ruta_tickets, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=SEPARADOR_CSV)
        escritor.writerow(nuevo_ticket)

    return nuevo_ticket


def ejecutar_chatbot():
    """Ejecuta el simulador local del chatbot de Soporte Técnico Nivel 1."""
    inicializar_archivos()
    soluciones = leer_soluciones()

    estado_usuario = ESTADO_INICIO

    print("==============================================")
    print("Mesa de Ayuda Interna - Umbrella Corporation")
    print("Soporte Técnico Nivel 1")
    print("Implementación: simulador local por consola")
    print("==============================================")

    # ESTADO_INICIO
    empleado = pedir_nombre_empleado()

    # ESTADO_SELECCIONAR_CATEGORIA
    estado_usuario = ESTADO_SELECCIONAR_CATEGORIA
    mostrar_opciones("Categorías disponibles:", CATEGORIAS)
    numero_categoria = pedir_opcion("Seleccione una categoría: ", len(CATEGORIAS))
    categoria = CATEGORIAS[numero_categoria - 1]

    # ESTADO_SELECCIONAR_PROBLEMA
    estado_usuario = ESTADO_SELECCIONAR_PROBLEMA
    problemas = obtener_problemas_por_categoria(soluciones, categoria)

    if not problemas:
        print("No hay problemas frecuentes cargados para la categoría seleccionada.")
        estado_usuario = ESTADO_FIN
        return

    mostrar_opciones(f"Problemas frecuentes de {categoria}:", problemas)
    numero_problema = pedir_opcion("Seleccione un problema: ", len(problemas))
    problema = problemas[numero_problema - 1]

    # ESTADO_MOSTRAR_SOLUCION
    estado_usuario = ESTADO_MOSTRAR_SOLUCION
    solucion = buscar_solucion(soluciones, categoria, problema)

    if solucion is None:
        print("No se encontró una solución automática para el problema seleccionado.")
        prioridad = "Media"
    else:
        prioridad = solucion["prioridad_sugerida"]
        print("\nSolución sugerida:")
        print(solucion["solucion"])
        print(f"Prioridad si se genera ticket: {prioridad}")

    # ESTADO_CONFIRMAR_RESOLUCION
    estado_usuario = ESTADO_CONFIRMAR_RESOLUCION
    caso_resuelto = pedir_respuesta_si_no("\n¿La solución resolvió el problema? (sí/no): ")

    if caso_resuelto:
        estado_usuario = ESTADO_FIN
        print("\nCaso cerrado automáticamente. No se generó ticket.")
        print("Gracias por usar la mesa de ayuda interna.")
        return

    # ESTADO_SOLICITAR_DESCRIPCION
    estado_usuario = ESTADO_SOLICITAR_DESCRIPCION
    print("\nSe generará un ticket para que Soporte Técnico Nivel 1 revise el caso.")
    descripcion = pedir_descripcion()

    # ESTADO_CREAR_TICKET
    estado_usuario = ESTADO_CREAR_TICKET
    ticket = generar_ticket(empleado, categoria, problema, descripcion, prioridad)

    estado_usuario = ESTADO_FIN
    print("\nTicket generado correctamente.")
    print(f"Número de ticket: {ticket['id_ticket']}")
    print(f"Prioridad: {ticket['prioridad']}")
    print(f"Fecha: {ticket['fecha_creacion']}")
    print("Estado: Abierto")


if __name__ == "__main__":
    ejecutar_chatbot()
