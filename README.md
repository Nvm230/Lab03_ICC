# Laboratorio 3 - Aplicación Flask con CRUD y Login

Este repositorio contiene la entrega final del Laboratorio 3: Desarrollo de aplicación Flask. La aplicación web fue construida con Python (Flask) y MariaDB bajo un entorno Arch Linux. Cuenta con un sistema de autenticación seguro y un CRUD (Crear, Leer, Actualizar, Eliminar) completo para la gestión de usuarios, diseñado de manera minimalista con Bootstrap 5.

---

## Estructura de Carpetas

La arquitectura del proyecto separa la lógica, las vistas y los estilos de la siguiente manera:

```text
Lab03-Flask-App/
│
├── app.py                  # Lógica principal del servidor web (Rutas, controladores y conexión a BD)
├── database.sql            # Script de migración y poblado de la base de datos
├── requirements.txt        # Dependencias de Python necesarias para el proyecto
│
├── templates/              # Vistas HTML (Jinja2)
│   ├── base.html           # Plantilla maestra con la estructura general y Navbar
│   ├── login.html          # Pantalla de inicio de sesión
│   ├── index.html          # Panel de administración (Listado Read / Delete)
│   ├── create.html         # Formulario para registrar usuarios (Create)
│   └── edit.html           # Formulario para editar usuarios (Update)
│
└── static/                 # Archivos estáticos de diseño
    └── style.css           # Estilos personalizados
```

---

## Configuración de la Base de Datos

La configuración se realizó en Arch Linux utilizando MariaDB. Para preparar la base de datos, se ejecutan los siguientes comandos:

1. Se inicia el servicio de base de datos:
   ```bash
   sudo systemctl start mariadb
   ```

2. Se carga la estructura y los datos por defecto utilizando el script proporcionado:
   ```bash
   sudo mariadb < database.sql
   ```
   (Este comando crea la base de datos `lab03_flask`, las tablas de `usuarios` y `administradores`, y los datos de prueba).

3. Se crea el usuario dedicado para la aplicación:
   Dado que MariaDB en Arch Linux bloquea el acceso externo al usuario root, la aplicación utiliza un usuario dedicado. Se crea ejecutando:
   ```bash
   sudo mariadb -e "CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'flask123'; GRANT ALL PRIVILEGES ON lab03_flask.* TO 'flask_user'@'localhost'; FLUSH PRIVILEGES;"
   ```

---

## Instalación y Ejecución de la Aplicación

Para desplegar la aplicación, se siguieron estos pasos:

1. Crear y activar el entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar las dependencias (Flask y PyMySQL):
```bash
pip install -r requirements.txt
```

3. Ejecutar el servidor web:
```bash
python3 app.py
```

La aplicación se ejecuta en el puerto local 5000: http://localhost:5000. 

Credenciales de acceso por defecto:
- Usuario: `admin`
- Contraseña: `admin123`

---

## Demostración Funcional

Se adjunta a la entrega un video demostrativo que evidencia el cumplimiento de la rúbrica:
1. Intento de login fallido.
2. Login exitoso y redirección al panel.
3. Creación de un nuevo usuario con validación.
4. Actualización de datos de un usuario existente.
5. Eliminación exitosa de un registro.

---
Desarrollado para el curso de Introducción a las Ciencias de la Computación (ICC).
