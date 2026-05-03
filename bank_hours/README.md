# Bank Hours (Argentina) - Free Version

M&oacute;dulo de gesti&oacute;n de banco de horas para Odoo seg&uacute;n las nuevas regulaciones laborales de Argentina.

## Descripci&oacute;n

Este m&oacute;dulo implementa el sistema de banco de horas de acuerdo con las nuevas regulaciones laborales en Argentina. Permite gestionar autom&aacute;ticamente las horas extra trabajadas por los empleados y convertirlas en tiempo libre compensatorio seg&uacute;n los multiplicadores configurados.

## Caracter&iacute;sticas

- **Multiplicador de horas extra configurable** (1.0x, 1.5x, 2.0x)
- **Reglas de expiraci&oacute;n** para las horas acumuladas
- **Asignaci&oacute;n autom&aacute;tica** de tiempo libre desde las horas extra de asistencia
- **An&aacute;lisis gr&aacute;fico y reportes** del banco de horas
- **Filtros** por empleado y mes
- **Validaci&oacute;n de tiempo m&iacute;nimo de descanso** entre turnos

## Requisitos

- Odoo 17.0
- M&oacute;dulo `hr_attendance` (Asistencia)
- M&oacute;dulo `hr_holidays` (Vacaciones)

## Instalaci&oacute;n

1. Copia el m&oacute;dulo en tu directorio de complementos personalizados:
   ```bash
   cp -r bank_hours /ruta/a/tus/addons/
   ```

2. Actualiza la lista de aplicaciones en Odoo:
   - Ve a **Aplicaciones** → **Actualizar lista de aplicaciones**

3. Busca "Bank Hours (Argentina)" e inst&aacute;lalo

4. Activa el modo desarrollador si necesitas ver los men&uacute;s t&eacute;cnicos

## Configuraci&oacute;n

### Configuraci&oacute;n de la Compa&ntilde;&iacute;a

1. Ve a **Configuraci&oacute;n** → **Asistencia** → **Bank of Hours (Argentina)**

2. Configura los siguientes par&aacute;metros:

   - **Multiplicador de horas extra**: Define c&oacute;mo se calculan las horas del banco
     - `1.0` = Tiempo igual (1 hora extra = 1 hora de banco)
     - `1.5` = 50% m&aacute;s (1 hora extra = 1.5 horas de banco)
     - `2.0` = Doble tiempo (1 hora extra = 2 horas de banco)
   
   - **Expiraci&oacute;n de horas (meses)**: N&uacute;mero de meses antes de que las horas acumuladas expiren
   
   - **Horas m&iacute;nimas de descanso**: Tiempo m&iacute;nimo requerido entre turnos

### Tipo de Ausencia

El m&oacute;dulo crea autom&aacute;ticamente un tipo de ausencia llamado "Bank of Hours" que se utiliza para las asignaciones de tiempo libre.

## Uso

### Registro Autom&aacute;tico

El m&oacute;dulo registra autom&aacute;ticamente las horas extra cuando un empleado marca su salida:

1. El empleado marca su entrada y salida normalmente en **Asistencia**
2. Si trabaja m&aacute;s horas de las esperadas seg&uacute;n su calendario, se calculan las horas extra
3. Se aplica el multiplicador configurado
4. Se crea autom&aacute;ticamente:
   - Un registro en el **Banco de Horas Log**
   - Una asignaci&oacute;n de tiempo libre en el tipo "Bank of Hours"

### Visualizaci&oacute;n del Historial

1. Ve a **Bank Hours** → **Bank Hours Log**
2. Aqu&iacute; ver&aacute;s todos los registros de horas extra trabajadas
3. Puedes filtrar por:
   - Empleado
   - Fecha
   - Mes/A&ntilde;o
4. Puedes agrupar por:
   - Empleado
   - Mes
   - A&ntilde;o

### Vistas Disponibles

- **Lista**: Vista tabular con todos los registros
- **Formulario**: Detalle de cada registro
- **Gr&aacute;fico**: An&aacute;lisis visual de horas trabajadas vs esperadas y banco de horas
- **Pivote**: Tabla din&aacute;mica para an&aacute;lisis detallado

### Uso de las Horas Acumuladas

Los empleados pueden solicitar tiempo libre usando las horas acumuladas:

1. Ve a **Vacaciones** → **Solicitudes**
2. Selecciona el tipo "Bank of Hours"
3. El sistema mostrar&aacute; las horas disponibles seg&uacute;n las asignaciones creadas

## Ejemplos de Configuraci&oacute;n

### Escenario 1: Multiplicador 1.5x (50% m&aacute;s)

- Empleado trabaja 2 horas extra
- Multiplicador: 1.5
- Resultado: 2 × 1.5 = 3 horas de banco

### Escenario 2: Multiplicador 2.0x (Doble tiempo)

- Empleado trabaja 1 hora extra
- Multiplicador: 2.0
- Resultado: 1 × 2.0 = 2 horas de banco

## Validaciones

### Tiempo M&iacute;nimo de Descanso

El m&oacute;dulo valida que entre el fin de un turno y el inicio del siguiente haya al menos el tiempo m&iacute;nimo de descanso configurado. Si no se cumple, se mostrar&aacute; un error al intentar marcar la entrada.

## Datos Demo

El m&oacute;dulo incluye datos de demostraci&oacute;n que puedes usar para probar las funcionalidades. Para activarlos:

1. Instala el m&oacute;dulo con datos demo habilitados
2. O ve a **Configuraci&oacute;n** → **T&eacute;cnico** → **Base de datos** → **Cargar datos demo**

## Soporte

- **Versi&oacute;n**: Free Version
- **Autor**: Sebastian Martin, Artaza Saade
- **Sitio web**: https://www.sebastianartaza.com/bank_hours.html
- **Licencia**: LGPL-3

## Versi&oacute;n Premium (Pr&oacute;ximamente)

La versi&oacute;n Premium incluir&aacute;:
- Reportes avanzados
- Notificaciones autom&aacute;ticas
- Flujos de aprobaci&oacute;n
- Integraci&oacute;n con n&oacute;mina
- Exportaci&oacute;n de datos
- Y m&aacute;s...

## Notas T&eacute;cnicas

- El m&oacute;dulo requiere que los empleados tengan un calendario de recursos asignado
- Las horas se calculan bas&aacute;ndose en el calendario del empleado
- Las asignaciones de tiempo libre se crean autom&aacute;ticamente con estado "confirmado"
- Los registros del log son hist&oacute;ricos y no se pueden modificar directamente

## Changelog

### Versi&oacute;n 17.0.1.0
- Versi&oacute;n inicial
- Gesti&oacute;n b&aacute;sica de banco de horas
- Multiplicadores configurables
- Reglas de expiraci&oacute;n
- Validaci&oacute;n de tiempo de descanso
- Vistas gr&aacute;ficas y de pivote

## Contribuciones

Las contribuciones son bienvenidas. Por favor, aseg&uacute;rate de seguir las convenciones de c&oacute;digo de Odoo.

## Licencia

Este m&oacute;dulo est&aacute; bajo la licencia LGPL-3.

