# Chatbot de Soporte Técnico Nivel 1 - Umbrella Corporation

## Descripción

Este proyecto es un simulador local por consola de una mesa de ayuda interna para la empresa ficticia **Umbrella Corporation**.

El sistema representa el proceso de **Soporte Técnico Nivel 1**. Su objetivo es asistir a empleados internos ante problemas frecuentes, mostrar una solución sugerida y generar un ticket cuando el inconveniente no puede resolverse automáticamente.

La plataforma propuesta para una implementación futura es **Telegram**. Sin embargo, para esta entrega se implementa una simulación local en Python, lo que permite demostrar la coherencia entre el flujo BPMN y la lógica del sistema sin depender de tokens, APIs externas o conexión a internet.

## Tecnologías utilizadas

- Python 3.
- Librería `csv` para leer y escribir archivos CSV.
- Librería `os` para manejar rutas y verificar archivos.
- Librería `datetime` para registrar la fecha de creación de los tickets.
- Archivos CSV como base de datos simulada.

No se utilizan frameworks ni librerías externas.

## Estructura de archivos

```text
chatbot-soporte-umbrella-corregido/
├── main.py
├── soluciones.csv
├── tickets.csv
├── README.md
└── documentacion/
    ├── diccionario_datos.md
    ├── casos_prueba.md
    ├── manual_usuario.md
    ├── relacion_bpmn.md
    └── texto_para_informe.md
```

## Instrucciones de ejecución

1. Abrir una terminal.
2. Ingresar a la carpeta del proyecto:

```bash
cd chatbot-soporte-umbrella-corregido
```

3. Ejecutar el programa:

```bash
python main.py
```

Si `soluciones.csv` o `tickets.csv` no existen, el sistema los crea automáticamente.

## Flujo del chatbot

El simulador sigue el siguiente flujo:

1. Solicita el nombre del empleado.
2. Muestra las categorías disponibles:
   - Internet.
   - Correo electrónico.
   - Impresoras.
   - Contraseñas.
   - Acceso a sistemas.
3. El usuario selecciona una categoría.
4. El sistema muestra los problemas frecuentes asociados.
5. El usuario selecciona un problema.
6. El sistema busca la solución en `soluciones.csv`.
7. Muestra la solución sugerida.
8. Pregunta si el problema fue resuelto.
9. Si el usuario responde `sí`, el caso se cierra automáticamente y no se genera ticket.
10. Si el usuario responde `no`, se solicita una descripción y se genera un ticket en `tickets.csv`.

## Máquina de estados

El programa utiliza constantes para representar los estados principales del proceso:

- `INICIO`
- `SELECCIONAR_CATEGORIA`
- `SELECCIONAR_PROBLEMA`
- `MOSTRAR_SOLUCION`
- `CONFIRMAR_RESOLUCION`
- `SOLICITAR_DESCRIPCION`
- `CREAR_TICKET`
- `FIN`

En esta versión por consola, la máquina de estados se representa mediante el flujo secuencial del programa y sus validaciones. En una versión real sobre Telegram, estos estados permitirían recordar en qué paso se encuentra cada usuario durante la conversación.

## Relación con BPMN

El proyecto puede representarse mediante un diagrama BPMN porque modela un proceso de negocio con inicio, actividades, decisiones y fin.

En términos de BPMN:

- El evento de inicio es la consulta del empleado.
- Las actividades del empleado son identificarse, seleccionar categoría, seleccionar problema y confirmar si la solución funcionó.
- Las actividades del bot son mostrar el menú, consultar la base de conocimientos, mostrar una solución y generar un ticket si corresponde.
- La compuerta principal aparece cuando el sistema pregunta si la solución resolvió el problema.
- Si la respuesta es afirmativa, el proceso finaliza sin generar ticket.
- Si la respuesta es negativa, se registra un ticket y el caso queda derivado al área de soporte.

## Base de datos simulada

El proyecto utiliza dos archivos CSV:

- `soluciones.csv`: contiene categorías, problemas frecuentes, soluciones sugeridas y prioridad inicial.
- `tickets.csv`: registra los casos que no pudieron resolverse automáticamente.

Los archivos CSV son compatibles con planillas de cálculo como Excel, por lo que cumplen la función de base de datos simulada para el trabajo práctico.

## Ejemplo de uso

```text
Mesa de Ayuda Interna - Umbrella Corporation
Soporte Técnico Nivel 1
Implementación: simulador local por consola
Ingrese su nombre y apellido: Juan Pérez

Categorías disponibles:
1. Internet
2. Correo electrónico
3. Impresoras
4. Contraseñas
5. Acceso a sistemas
Seleccione una categoría: 1

Problemas frecuentes de Internet:
1. Sin conexión a internet
2. Conexión lenta
3. No accede a la VPN
Seleccione un problema: 1

Solución sugerida:
Verifique que el cable de red o la conexión Wi-Fi estén activos. Reinicie el equipo y compruebe si otros usuarios tienen conexión.
Prioridad si se genera ticket: Media

¿La solución resolvió el problema? (sí/no): no

Se generará un ticket para que Soporte Técnico Nivel 1 revise el caso.
Describa brevemente qué ocurre para registrar el ticket: Reinicié el equipo, pero sigo sin conexión.

Ticket generado correctamente.
Número de ticket: 1
Prioridad: Media
Fecha: 2026-06-17
Estado: Abierto
```
