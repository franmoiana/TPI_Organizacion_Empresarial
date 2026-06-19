# Diccionario de datos

Este documento reúne los datos que utiliza el simulador de mesa de ayuda interna de **Umbrella Corporation**.

El proyecto trabaja con archivos CSV como base de datos simulada. Ambos archivos usan el separador `;`, para que puedan abrirse sin problemas desde una planilla de cálculo como Excel.

## Archivo `soluciones.csv`

El archivo `soluciones.csv` funciona como base de conocimientos. Allí se guardan las categorías de soporte, los problemas frecuentes, la respuesta sugerida y la prioridad que se tomará como referencia si el caso termina generando un ticket.

| Campo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| `id_solucion` | Entero | Identificador único de cada solución cargada. | 1 |
| `categoria` | Texto | Tipo general de incidente. | Internet |
| `problema` | Texto | Problema frecuente que puede elegir el empleado. | Sin conexión a internet |
| `solucion` | Texto | Instrucción que muestra el sistema para intentar resolver el incidente. | Verifique el cable de red y reinicie el equipo. |
| `prioridad_sugerida` | Texto | Prioridad que se asignará al ticket si el problema no se resuelve. | Media |

## Archivo `tickets.csv`

El archivo `tickets.csv` registra los casos que no pudieron resolverse con la respuesta automática. Cada registro queda disponible para que el área de soporte pueda revisarlo y hacer seguimiento.

| Campo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| `id_ticket` | Entero | Número único e incremental del ticket. | 1 |
| `fecha_creacion` | Fecha | Fecha en la que se generó el ticket, con formato AAAA-MM-DD. | 2026-06-17 |
| `empleado` | Texto | Nombre y apellido del empleado que realizó la consulta. | Juan Pérez |
| `categoria` | Texto | Categoría seleccionada durante la atención. | Internet |
| `problema` | Texto | Problema frecuente elegido por el empleado. | Sin conexión a internet |
| `descripcion` | Texto | Detalle adicional ingresado por el empleado cuando la solución no funcionó. | Reinicié el equipo, pero sigo sin conexión. |
| `prioridad` | Texto | Prioridad tomada desde la solución seleccionada. | Media |
| `estado` | Texto | Estado inicial del ticket generado. | Abierto |

## Constantes y variables principales

| Nombre | Descripción |
|---|---|
| `SEPARADOR_CSV` | Carácter utilizado para separar los campos de los archivos CSV. |
| `ARCHIVO_SOLUCIONES` | Nombre del archivo que contiene la base de conocimientos. |
| `ARCHIVO_TICKETS` | Nombre del archivo donde se guardan los tickets. |
| `CATEGORIAS` | Lista de categorías disponibles para clasificar la consulta. |
| `SOLUCIONES_INICIALES` | Datos iniciales que se cargan si no existe `soluciones.csv`. |
| `ESTADO_INICIO` | Inicio del flujo de atención. |
| `ESTADO_SELECCIONAR_CATEGORIA` | Etapa en la que el empleado elige la categoría del problema. |
| `ESTADO_SELECCIONAR_PROBLEMA` | Etapa en la que el empleado elige un problema frecuente. |
| `ESTADO_MOSTRAR_SOLUCION` | Etapa en la que el sistema muestra la solución sugerida. |
| `ESTADO_CONFIRMAR_RESOLUCION` | Etapa en la que el empleado indica si la solución funcionó. |
| `ESTADO_SOLICITAR_DESCRIPCION` | Etapa en la que el sistema pide una descripción antes de generar el ticket. |
| `ESTADO_CREAR_TICKET` | Etapa en la que el sistema guarda el ticket en `tickets.csv`. |
| `ESTADO_FIN` | Cierre del proceso, con o sin ticket generado. |
| `empleado` | Nombre y apellido de la persona que solicita soporte. |
| `soluciones` | Lista de registros leídos desde `soluciones.csv`. |
| `categoria` | Categoría elegida por el empleado. |
| `problemas` | Problemas frecuentes asociados a la categoría seleccionada. |
| `problema` | Problema elegido dentro de la categoría. |
| `solucion` | Registro encontrado en `soluciones.csv`, junto con su prioridad sugerida. |
| `caso_resuelto` | Valor que indica si el empleado confirmó que la solución funcionó. |
| `descripcion` | Texto ingresado por el empleado cuando se requiere generar un ticket. |
| `ticket` | Registro creado y guardado en `tickets.csv`. |

Estos datos permiten ordenar el flujo de atención: identificar al empleado, clasificar el incidente, mostrar una posible solución, confirmar el resultado y registrar el ticket cuando corresponde.
