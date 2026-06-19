# Relación entre el chatbot y el modelo BPMN

La lógica del simulador mantiene correspondencia con el modelo BPMN del proceso de **Soporte Técnico Nivel 1**. Cada paso de la conversación se puede asociar con una tarea del empleado, una tarea del sistema, una compuerta de decisión o una derivación al técnico.

## Carriles del diagrama BPMN

El diagrama To-Be se organiza en tres carriles:

| Carril | Función dentro del proceso |
|---|---|
| Empleado interno | Inicia la consulta, selecciona opciones y confirma si el problema fue resuelto. |
| Chatbot / Sistema | Muestra opciones, valida datos, consulta soluciones y registra tickets. |
| Técnico de soporte | Recibe los tickets generados y realiza el seguimiento del caso. |

## Flujo To-Be del proceso automatizado

El flujo To-Be representa el funcionamiento de la mesa de ayuda una vez incorporado el chatbot como primer nivel de atención.

```text
Inicio
↓
Empleado inicia consulta
↓
Bot solicita nombre del empleado
↓
Bot muestra categorías disponibles
↓
Empleado selecciona categoría
↓
¿Categoría válida?
├── No → Bot informa el error y vuelve a mostrar las categorías
└── Sí → Bot muestra problemas frecuentes
        ↓
        Empleado selecciona problema
        ↓
        ¿Problema válido?
        ├── No → Bot informa el error y vuelve a mostrar los problemas frecuentes
        └── Sí → Bot consulta soluciones.csv
                ↓
                Bot muestra solución sugerida
                ↓
                Empleado confirma si la solución resolvió el problema
                ↓
                ¿Problema resuelto?
                ├── Sí → Bot cierra el caso sin generar ticket
                └── No → Bot solicita una descripción del inconveniente
                        ↓
                        ¿Descripción válida?
                        ├── No → Bot solicita nuevamente la descripción
                        └── Sí → Bot genera ticket en tickets.csv
                                ↓
                                Técnico recibe el ticket automático
                                ↓
                                Técnico resuelve y cierra el ticket
                                ↓
                                Fin
```

## Correspondencia entre el diagrama BPMN y el simulador

| Elemento BPMN | Acción en el simulador |
|---|---|
| Evento de inicio | El empleado inicia la consulta. |
| Tarea de usuario | El empleado ingresa su nombre y apellido. |
| Tarea del sistema | El bot muestra las categorías disponibles. |
| Tarea de usuario | El empleado selecciona una categoría. |
| Compuerta exclusiva | El sistema valida si la categoría ingresada existe. |
| Tarea del sistema | El bot muestra los problemas frecuentes de la categoría seleccionada. |
| Tarea de usuario | El empleado selecciona un problema frecuente. |
| Compuerta exclusiva | El sistema valida si el problema ingresado existe. |
| Tarea del sistema | El bot consulta `soluciones.csv`. |
| Tarea del sistema | El bot muestra la solución sugerida. |
| Compuerta exclusiva | El sistema evalúa si la solución resolvió el problema. |
| Tarea del sistema | Si se resolvió, el bot cierra el caso sin generar ticket. |
| Tarea de usuario | Si no se resolvió, el empleado describe el problema. |
| Compuerta exclusiva | El sistema valida que la descripción no esté vacía. |
| Tarea del sistema | El bot registra el ticket en `tickets.csv`. |
| Tarea del técnico | El técnico recibe, revisa y cierra el ticket. |
| Evento de fin | El proceso finaliza con el caso cerrado o con el ticket resuelto. |

## Implementación local e integración futura con Telegram

La plataforma definida para una implementación real es Telegram. Para esta entrega se desarrolló un simulador local por consola, lo que permite probar el flujo sin depender de tokens, conexión externa o configuración de una API.

En una versión integrada con Telegram, las entradas por consola (`input`) serían reemplazadas por mensajes enviados por el usuario, y las salidas por consola (`print`) serían reemplazadas por respuestas del bot. La lógica de estados, la consulta de `soluciones.csv` y la generación de tickets se mantendrían sin cambios importantes.
