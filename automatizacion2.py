from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time
import re  

special_characters = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")


firefox_options = Options()


driver = webdriver.Firefox(service=webdriver.firefox.service.Service(GeckoDriverManager().install()), options=firefox_options)

# Registro de usuario
def test_register_user():
    driver.get("https://test-qa.inlaze.com/auth/sign-up")
    print("Página de registro cargada")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "full-name")))
    full_name_field = driver.find_element(By.ID, "full-name")
    email_field = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.XPATH, "//app-password//input[@type='password' and @id='password']")
    confirm_password_input = driver.find_element(By.XPATH, "//app-password//input[@type='password' and @id='confirm-password']")

    full_name_field.send_keys("Diana Garcia")
    email_field.send_keys("diagar14@gmail.com")
    password_input.send_keys("Aguila9999*")
    confirm_password_input.send_keys("Aguila9999*")

    # Verificar que el nombre tiene al menos dos palabras
    name_value = full_name_field.get_attribute("value")
    if len(name_value.split()) < 2:
        print("El campo 'Nombre' debe contener al menos 2 palabras.")
    else:
        print("El campo 'Nombre' es válido.")

    # Verificar que el email tiene un formato válido
    email_value = email_field.get_attribute("value")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
        print("El email no tiene un formato válido.")
    else:
        print("Email válido.")

    # Validar que la contraseña cumple con los requisitos
    password_value = password_input.get_attribute("value")
    if len(password_value) < 8 or not any(char.isupper() for char in password_value) or not any(char.isdigit() for char in password_value) or not special_characters.search(password_value):
        print("La contraseña no cumple con los requisitos de longitud, caracteres y/o caracteres especiales.")
    else:
        print("Contraseña válida.")

    # Verificar que las contraseñas coinciden
    confirm_password_value = confirm_password_input.get_attribute("value")
    if password_value != confirm_password_value:
        print("Las contraseñas no coinciden.")
    else:
        print("Las contraseñas coinciden.")

    sign_up_button = driver.find_element(By.XPATH, "//button[text()=' Sign up ']")
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_up_button)

    WebDriverWait(driver, 20).until(EC.visibility_of(sign_up_button))

    if sign_up_button.get_attribute('disabled') is None:
        print("Botón habilitado, haciendo clic en 'Sign up'.")
        sign_up_button.click()
    else:
        print("El botón de 'Sign up' sigue deshabilitado.")

    time.sleep(3)

# 2. Función para hacer login y verificar el nombre de perfil
def test_login_user():

    driver.get("https://test-qa.inlaze.com/auth/sign-in")
    print("Página de inicio de sesión cargada")

    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//app-password//input[@type='password' and @id='password']")))

    email_field.send_keys("diagar14@gmail.com")
    password_field.send_keys("Aguila9999*")

    if not email_field.get_attribute("value") or not password_field.get_attribute("value"):
        print("Los campos de login no pueden estar vacíos.")
    else:
        sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Sign in ']")))
        sign_in_button.click()
        print("Haciendo clic en 'Sign in' para iniciar sesión.")

    profile_name_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='flex gap-4 items-center']/h2")))

    profile_name = profile_name_element.text.strip()
    print(f"Nombre del perfil encontrado: {profile_name}")

    # Comparar el nombre del perfil con el nombre ingresado
    if profile_name == "DIANA GARCIA":
        print("El nombre del perfil coincide con el ingresado.")
    else:
        print(f"El nombre del perfil no coincide. Esperado: 'DIANA GARCIA', pero encontrado: {profile_name}")

# 3. Función para cerrar sesión
def test_logout():
    profile_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='flex gap-4 items-center']/label"))
    )
    profile_menu.click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@class='menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52']//a[text()='Logout']"))
    )
    logout_button.click()
    print("Haciendo clic en 'Logout' para cerrar sesión.")

    WebDriverWait(driver, 10).until(EC.url_contains("sign-in"))
    print("Usuario cerrado sesión correctamente.")

# 4. Función principal para ejecutar las pruebas
def run_tests():
    try:
        test_register_user()
        test_login_user()
        test_logout()
    except Exception as e:
        print(f"Error durante las pruebas: {e}")
    finally:
        driver.quit()
        print("Navegador cerrado")

if __name__ == "__main__":
    run_tests()
