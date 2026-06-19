# Manual de usuario

## Introducción

Este manual describe el uso del simulador de mesa de ayuda interna de **Umbrella Corporation**.

El sistema está orientado a empleados internos que necesitan una primera asistencia ante problemas frecuentes de Soporte Técnico Nivel 1.

## Inicio del simulador

Para ejecutar el programa:

1. Abrir una terminal o consola.
2. Ingresar a la carpeta del proyecto:

```bash
cd TPI_Organizacion_Empresarial
```

3. Ejecutar el archivo principal:

```bash
python main.py
```

Al iniciar, el sistema muestra la presentación de la mesa de ayuda y solicita el nombre y apellido del empleado.

## Selección de categoría

Después de ingresar el nombre, el sistema muestra una lista numerada con las categorías disponibles:

```text
1. Internet
2. Correo electrónico
3. Impresoras
4. Contraseñas
5. Acceso a sistemas
```

El empleado debe ingresar el número correspondiente a la categoría de su inconveniente.

Si escribe texto o un número que no pertenece al menú, el sistema muestra un mensaje de error y solicita nuevamente la opción.

## Selección de problema frecuente

Luego de elegir la categoría, el sistema muestra los problemas frecuentes asociados. Por ejemplo, para la categoría Internet pueden aparecer estas opciones:

```text
1. Sin conexión a internet
2. Conexión lenta
3. No accede a la VPN
```

El empleado debe seleccionar el número del problema que mejor represente su situación.

## Confirmación de resolución

Después de seleccionar el problema, el sistema consulta `soluciones.csv` y muestra una solución sugerida.

Luego solicita la confirmación del empleado:

```text
¿La solución resolvió el problema? (sí/no):
```

Las respuestas válidas son:

- `sí`, cuando la solución funcionó.
- `no`, cuando el inconveniente continúa.

Si se ingresa otra respuesta, el sistema vuelve a pedir una confirmación válida.

## Generación de ticket

Cuando el empleado responde `no`, el sistema solicita una descripción breve del problema. Con esa información se genera un ticket en `tickets.csv`.

El ticket incluye:

- número de ticket,
- fecha de creación,
- nombre del empleado,
- categoría,
- problema seleccionado,
- descripción del inconveniente,
- prioridad,
- estado inicial `Abierto`.

La prioridad se obtiene desde el campo `prioridad_sugerida` de `soluciones.csv`.

## Ejemplo de uso

```text
Mesa de Ayuda Interna - Umbrella Corporation
Soporte Técnico Nivel 1
Implementación: simulador local por consola

Ingrese su nombre y apellido: María Gómez

Categorías disponibles:
1. Internet
2. Correo electrónico
3. Impresoras
4. Contraseñas
5. Acceso a sistemas

Seleccione una categoría: 5

Problemas frecuentes de Acceso a sistemas:
1. No puede ingresar al sistema interno
2. No tiene permisos suficientes
3. El sistema muestra error

Seleccione un problema: 1

Solución sugerida:
Confirme que usa el enlace correcto, cierre sesión, borre caché del navegador e intente nuevamente.
Prioridad si se genera ticket: Alta

¿La solución resolvió el problema? (sí/no): no

Se generará un ticket para que Soporte Técnico Nivel 1 revise el caso.
Describa brevemente qué ocurre para registrar el ticket: Probé con otro navegador, pero el sistema sigue rechazando el ingreso.

Ticket generado correctamente.
Número de ticket: 1
Prioridad: Alta
Fecha: 2026-06-17
Estado: Abierto
```

## Cierre del caso

Si la solución sugerida resuelve el inconveniente, el sistema informa que el caso fue cerrado automáticamente. En ese caso no se genera un ticket, ya que no se requiere intervención posterior del área de soporte.
