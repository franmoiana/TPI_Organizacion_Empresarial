# Casos de prueba

Los siguientes casos se usaron para revisar el funcionamiento del simulador y comprobar que el flujo de Soporte Técnico Nivel 1 coincida con el proceso modelado en BPMN.

## Caso 1: problema resuelto automáticamente

**Objetivo:** comprobar que el sistema muestra una solución y cierra el caso cuando el empleado confirma que funcionó.

**Datos de entrada:**

- Empleado: Juan Pérez.
- Categoría: Internet.
- Problema: Sin conexión a internet.
- Respuesta: `sí`.

**Pasos:**

1. Ejecutar `python main.py`.
2. Ingresar el nombre del empleado.
3. Seleccionar una categoría válida.
4. Seleccionar un problema frecuente.
5. Leer la solución sugerida.
6. Responder `sí` cuando el sistema pregunta si se resolvió.

**Resultado esperado:** el sistema informa que el caso fue cerrado automáticamente y no genera un ticket.

## Caso 2: problema no resuelto y creación de ticket

**Objetivo:** comprobar que el sistema registra un ticket cuando la solución sugerida no resuelve el problema.

**Datos de entrada:**

- Empleado: Ana López.
- Categoría: Impresoras.
- Problema: La impresora no imprime.
- Respuesta: `no`.
- Descripción: La impresora del sector administración sigue sin responder.

**Pasos:**

1. Ejecutar `python main.py`.
2. Ingresar el nombre del empleado.
3. Seleccionar la categoría `Impresoras`.
4. Seleccionar el problema `La impresora no imprime`.
5. Responder `no` cuando el sistema pregunta si se resolvió.
6. Ingresar una descripción del inconveniente.

**Resultado esperado:** el sistema agrega un ticket en `tickets.csv`, conserva los tickets anteriores y muestra número de ticket, prioridad, fecha y estado.

## Caso 3: categoría inválida

**Objetivo:** comprobar que el sistema controle la selección de categoría.

**Datos de entrada:**

- Categoría ingresada: `9`.

**Pasos:**

1. Ejecutar el programa.
2. Ingresar un nombre de empleado válido.
3. En la selección de categoría, ingresar un número fuera del rango mostrado.

**Resultado esperado:** el sistema muestra el mensaje `Error: la opción ingresada no es válida.` y solicita nuevamente la categoría.

## Caso 4: opción no numérica

**Objetivo:** comprobar que el sistema controle los casos en los que el usuario escribe texto cuando se espera un número.

**Datos de entrada:**

- Categoría ingresada: `internet`.

**Pasos:**

1. Ejecutar el programa.
2. Ingresar un nombre de empleado válido.
3. En la selección de categoría, escribir texto en lugar de un número.

**Resultado esperado:** el sistema muestra el mensaje `Error: ingrese una opción numérica.` y vuelve a pedir el dato.

## Caso 5: respuesta inválida al confirmar resolución

**Objetivo:** comprobar que el sistema acepte únicamente respuestas afirmativas o negativas.

**Datos de entrada:**

- Respuesta ingresada: `tal vez`.

**Pasos:**

1. Completar el flujo hasta visualizar una solución sugerida.
2. Cuando el sistema pregunta si se resolvió el problema, ingresar una respuesta distinta de `sí` o `no`.

**Resultado esperado:** el sistema muestra el mensaje `Error: responda sí o no.` y solicita nuevamente la respuesta.

## Caso 6: descripción vacía

**Objetivo:** comprobar que el sistema no genere tickets sin una descripción del inconveniente.

**Datos de entrada:**

- Respuesta a solución: `no`.
- Descripción: vacía.

**Pasos:**

1. Completar el flujo hasta visualizar una solución sugerida.
2. Responder `no`.
3. Presionar Enter sin escribir una descripción.

**Resultado esperado:** el sistema muestra el mensaje `Error: la descripción no puede estar vacía.` y solicita nuevamente la descripción antes de crear el ticket.
