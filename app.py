from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flask_lab'

# Configuración de la base de datos
DB_HOST = 'localhost'
DB_USER = 'flask_user'
DB_PASSWORD = 'flask123'
DB_NAME = 'lab03_flask'

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

# --- SISTEMA DE LOGIN ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # Ojo: En un proyecto real, las contraseñas deberían estar encriptadas (hasheadas)
            cursor.execute('SELECT * FROM administradores WHERE username = %s AND password = %s', (username, password))
            admin = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if admin:
                session['admin_id'] = admin['id']
                session['username'] = admin['username']
                flash('Inicio de sesión exitoso.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Usuario o contraseña incorrectos.', 'danger')
        except Exception as e:
            flash(f'Error de conexión a la base de datos: {str(e)}', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('username', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

# --- OPERACIONES CRUD DE USUARIOS ---

@app.route('/')
def index():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        usuarios = []
        flash(f'Error al cargar usuarios: {str(e)}', 'danger')
        
    return render_template('index.html', usuarios=usuarios)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']
        
        if not nombre or not email or not rol:
            flash('Todos los campos son obligatorios.', 'warning')
            return redirect(url_for('create'))
            
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, email, rol) VALUES (%s, %s, %s)', (nombre, email, rol))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Usuario creado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al crear el usuario (¿Email duplicado?): {str(e)}', 'danger')
            
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']
        
        try:
            cursor.execute('UPDATE usuarios SET nombre = %s, email = %s, rol = %s WHERE id = %s', (nombre, email, rol, id))
            conn.commit()
            flash('Usuario actualizado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al actualizar el usuario: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
    else:
        cursor.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not usuario:
            flash('Usuario no encontrado.', 'warning')
            return redirect(url_for('index'))
            
        return render_template('edit.html', usuario=usuario)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Usuario eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar el usuario: {str(e)}', 'danger')
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
