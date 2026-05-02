-- Script para crear la base de datos y las tablas del Lab

CREATE DATABASE IF NOT EXISTS lab03_flask;
USE lab03_flask;

-- Tabla para los administradores (Sistema de Login)
CREATE TABLE IF NOT EXISTS administradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Tabla principal de usuarios (Sistema CRUD)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    rol ENUM('admin', 'usuario') NOT NULL DEFAULT 'usuario'
);

-- Creamos un admin por defecto para poder entrar
-- La contraseña de este admin es 'admin123'
INSERT IGNORE INTO administradores (username, password) VALUES ('admin', 'admin123');

-- Metemos un par de usuarios de prueba para ver el CRUD funcionando
INSERT IGNORE INTO usuarios (nombre, email, rol) VALUES 
('Juan Perez', 'juan@example.com', 'usuario'),
('Maria Garcia', 'maria@example.com', 'admin');
