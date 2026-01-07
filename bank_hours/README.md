# Bank Hours (Argentina) - Free Version

Módulo de gestión de banco de horas para Odoo según las nuevas regulaciones laborales de Argentina.

## Descripción

Este módulo implementa el sistema de banco de horas de acuerdo con las nuevas regulaciones laborales en Argentina. Permite gestionar automáticamente las horas extra trabajadas por los empleados y convertirlas en tiempo libre compensatorio según los multiplicadores configurados.

## Características

- **Multiplicador de horas extra configurable** (1.0x, 1.5x, 2.0x)
- **Reglas de expiración** para las horas acumuladas
- **Asignación automática** de tiempo libre desde las horas extra de asistencia
- **Análisis gráfico y reportes** del banco de horas
- **Filtros** por empleado y mes
- **Validación de tiempo mínimo de descanso** entre turnos

## Requisitos

- Odoo 17.0
- Módulo `hr_attendance` (Asistencia)
- Módulo `hr_holidays` (Vacaciones)

## Instalación

1. Copia el módulo en tu directorio de complementos personalizados:
   ```bash
   cp -r bank_hours /ruta/a/tus/addons/
   ```

2. Actualiza la lista de aplicaciones en Odoo:
   - Ve a **Aplicaciones** → **Actualizar lista de aplicaciones**

3. Busca "Bank Hours (Argentina)" e instálalo

4. Activa el modo desarrollador si necesitas ver los menús técnicos

## Configuración

### Configuración de la Compañía

1. Ve a **Configuración** → **Asistencia** → **Bank of Hours (Argentina)**

2. Configura los siguientes parámetros:

   - **Multiplicador de horas extra**: Define cómo se calculan las horas del banco
     - `1.0` = Tiempo igual (1 hora extra = 1 hora de banco)
     - `1.5` = 50% más (1 hora extra = 1.5 horas de banco)
     - `2.0` = Doble tiempo (1 hora extra = 2 horas de banco)
   
   - **Expiración de horas (meses)**: Número de meses antes de que las horas acumuladas expiren
   
   - **Horas mínimas de descanso**: Tiempo mínimo requerido entre turnos

### Tipo de Ausencia

El módulo crea automáticamente un tipo de ausencia llamado "Bank of Hours" que se utiliza para las asignaciones de tiempo libre.

## Uso

### Registro Automático

El módulo registra automáticamente las horas extra cuando un empleado marca su salida:

1. El empleado marca su entrada y salida normalmente en **Asistencia**
2. Si trabaja más horas de las esperadas según su calendario, se calculan las horas extra
3. Se aplica el multiplicador configurado
4. Se crea automáticamente:
   - Un registro en el **Banco de Horas Log**
   - Una asignación de tiempo libre en el tipo "Bank of Hours"

### Visualización del Historial

1. Ve a **Bank Hours** → **Bank Hours Log**
2. Aquí verás todos los registros de horas extra trabajadas
3. Puedes filtrar por:
   - Empleado
   - Fecha
   - Mes/Año
4. Puedes agrupar por:
   - Empleado
   - Mes
   - Año

### Vistas Disponibles

- **Lista**: Vista tabular con todos los registros
- **Formulario**: Detalle de cada registro
- **Gráfico**: Análisis visual de horas trabajadas vs esperadas y banco de horas
- **Pivote**: Tabla dinámica para análisis detallado

### Uso de las Horas Acumuladas

Los empleados pueden solicitar tiempo libre usando las horas acumuladas:

1. Ve a **Vacaciones** → **Solicitudes**
2. Selecciona el tipo "Bank of Hours"
3. El sistema mostrará las horas disponibles según las asignaciones creadas

## Ejemplos de Configuración

### Escenario 1: Multiplicador 1.5x (50% más)

- Empleado trabaja 2 horas extra
- Multiplicador: 1.5
- Resultado: 2 × 1.5 = 3 horas de banco

### Escenario 2: Multiplicador 2.0x (Doble tiempo)

- Empleado trabaja 1 hora extra
- Multiplicador: 2.0
- Resultado: 1 × 2.0 = 2 horas de banco

## Validaciones

### Tiempo Mínimo de Descanso

El módulo valida que entre el fin de un turno y el inicio del siguiente haya al menos el tiempo mínimo de descanso configurado. Si no se cumple, se mostrará un error al intentar marcar la entrada.

## Datos Demo

El módulo incluye datos de demostración que puedes usar para probar las funcionalidades. Para activarlos:

1. Instala el módulo con datos demo habilitados
2. O ve a **Configuración** → **Técnico** → **Base de datos** → **Cargar datos demo**

## Soporte

- **Versión**: Free Version
- **Autor**: Sebastian Martin, Artaza Saade
- **Sitio web**: https://www.sebastianartaza.com/bank_hours.html
- **Licencia**: LGPL-3

## Versión Premium (Próximamente)

La versión Premium incluirá:
- Reportes avanzados
- Notificaciones automáticas
- Flujos de aprobación
- Integración con nómina
- Exportación de datos
- Y más...

## Notas Técnicas

- El módulo requiere que los empleados tengan un calendario de recursos asignado
- Las horas se calculan basándose en el calendario del empleado
- Las asignaciones de tiempo libre se crean automáticamente con estado "confirmado"
- Los registros del log son históricos y no se pueden modificar directamente

## Changelog

### Versión 17.0.1.0
- Versión inicial
- Gestión básica de banco de horas
- Multiplicadores configurables
- Reglas de expiración
- Validación de tiempo de descanso
- Vistas gráficas y de pivote

## Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de seguir las convenciones de código de Odoo.

## Licencia

Este módulo está bajo la licencia LGPL-3.

