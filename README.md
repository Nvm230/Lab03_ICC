# 🚀 Laboratorio 3 - Aplicación Flask con CRUD y Login

Este repositorio contiene la entrega final del **Laboratorio 3: Desarrollo de aplicación Flask**. La aplicación web ha sido construida con Python (Flask) y MariaDB/MySQL, y cuenta con un sistema de autenticación seguro y un CRUD (Crear, Leer, Actualizar, Eliminar) completo para la gestión de usuarios, todo envuelto en un diseño minimalista y moderno usando Bootstrap 5.

---

## 📂 Estructura de Carpetas

La arquitectura del proyecto sigue las mejores prácticas de Flask, separando la lógica, las vistas y los estilos:

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
    └── style.css           # Estilos personalizados (Diseño minimalista premium)
```

---

## 🗄️ Configuración de la Base de Datos

El proyecto utiliza un archivo SQL (`database.sql`) que contiene toda la estructura necesaria. Para configurarla en tu entorno local, sigue estos pasos:

1. **Inicia tu servicio de base de datos** (si usas MariaDB en Linux):
   ```bash
   sudo systemctl start mariadb
   ```

2. **Carga la estructura y datos por defecto**:
   ```bash
   sudo mariadb < database.sql
   ```
   *(Esto creará la base de datos `lab03_flask`, las tablas de `usuarios` y `administradores`, y poblará datos iniciales de prueba).*

3. **Crea el usuario para la aplicación**:
   Dado que MariaDB en muchos sistemas suele bloquear el acceso externo al usuario `root`, la aplicación está configurada para usar un usuario dedicado. Ejecuta esto en tu terminal para crearlo:
   ```bash
   sudo mariadb -e "CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'flask123'; GRANT ALL PRIVILEGES ON lab03_flask.* TO 'flask_user'@'localhost'; FLUSH PRIVILEGES;"
   ```

---

## 🛠️ Instalación y Ejecución de la Aplicación

Sigue estos pasos en tu terminal para levantar la aplicación:

### 1. Preparar el Entorno
Te recomendamos usar un entorno virtual para no mezclar dependencias:
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar el entorno virtual (Linux/macOS)
source venv/bin/activate
```

### 2. Instalar Dependencias
Instala Flask y el conector de base de datos PyMySQL:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Servidor
Inicia la aplicación de Flask:
```bash
python3 app.py
```

### 4. Ingresar a la App
Abre tu navegador web y entra a [http://localhost:5000](http://localhost:5000).

**Credenciales de acceso por defecto:**
- **Usuario:** `admin`
- **Contraseña:** `admin123`

---

## 🎥 Demostración Funcional

Se ha adjuntado a la entrega un video demostrativo mostrando el cumplimiento de todos los requerimientos de la rúbrica:
1. Intento de login fallido.
2. Login exitoso y redirección al panel.
3. Creación de un nuevo usuario con validación.
4. Actualización de datos de un usuario existente.
5. Eliminación exitosa de un registro.

---
*Desarrollado para el curso de Introducción a las Ciencias de la Computación (ICC).*
