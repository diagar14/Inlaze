# Pruebas Automatizadas con Selenium - Registro y Login de Usuario

Este repositorio contiene pruebas automatizadas de registro y login de usuario utilizando **Selenium WebDriver** en **Python**. Las pruebas se ejecutan en un navegador Firefox y verifican diversos aspectos del flujo de registro y login en una plataforma web de ejemplo.

## Requisitos Previos

Para ejecutar las pruebas, asegúrate de tener instalados los siguientes requisitos:

1. **Python** (versión 3.7 o superior)
2. **Selenium WebDriver** para Python
3. **GeckoDriver** (para Firefox)
4. **webdriver_manager** (para gestionar GeckoDriver automáticamente)

## Instalación

### 1. Instalar Python
Si no tienes Python instalado, puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Instalar el webdriver segun el explorador
En este caso use firefox, s epuede descargar desde [https://github.com/mozilla/geckodriver/releases]

### 3. Instalar las dependencias usadas
Ejecutar el comando pip install -r requirements.txt




### Ejecucion de casos de prueba

Los casos de pruebas estan definidos en el archivo automatization2.py

### Ejecutar el script

utilizar el comando python automatization2.py para ejecutar el script de casos de prueba

## Descripción de los Casos de Prueba
    1. Pruebas de Registro de Usuario:
    Verificar que se pueda registrar un usuario con nombre, email y contraseña válidos.
    Validar que el campo de nombre acepte un mínimo de 2 palabras.
    Verificar que el email tenga un formato válido.
    Validar que la contraseña cumpla con los requisitos de longitud y caracteres.
    Verificar que el formulario no se envíe si los campos obligatorios no están completos.
    Verificar que las contraseñas ingresadas coincidan.
    2. Pruebas de Login de Usuario:
    Verificar que el usuario pueda loguearse con el email y la contraseña correctos.
    Validar que el formulario de login no se envíe si los campos no están completos.
    Verificar que al ingresar se muestre el nombre del usuario.
    Verificar que el sistema permita cerrar la sesión correctamente.