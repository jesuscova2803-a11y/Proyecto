import os
import time
import subprocess
import uiautomation as auto
from playwright.sync_api import sync_playwright


def abrir_excel(ruta_excel):

    ruta_excel = os.path.abspath(ruta_excel)

    print("Abriendo Excel...")

    os.startfile(ruta_excel)

    time.sleep(10)

    ventana = auto.WindowControl(ClassName='XLMAIN')

    ventana.SetActive()

    print("Excel abierto correctamente")

    return ventana


def ejecutar_login():

    print("Ejecutando Login...")

    with sync_playwright() as p:

        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "https://practicetestautomation.com/practice-test-login/"
        )

        page.locator("#username").fill(
            "student"
        )

        page.locator("#password").fill(
            "Password123"
        )

        page.locator("#submit").click()

        page.wait_for_timeout(3000)

        titulo = page.locator("h1").text_content()

        browser.close()

        if titulo == "Logged In Successfully":

            print("LOGIN EXITOSO")

            return "LOGIN EXITOSO"

        else:

            print("LOGIN FALLIDO")

            return "LOGIN FALLIDO"


def escribir_resultado_excel(ventana, resultado):

    print("Escribiendo resultado en Excel...")

    ventana.SetActive()

    time.sleep(2)

    # A1
    auto.SendKeys("Resultado")

    # A2
    auto.SendKeys("{ENTER}")

    auto.SendKeys(resultado)

    print("Resultado escrito")

def guardar_excel():

    print("Guardando copia del Excel...")

    auto.SendKeys("{F12}")

    time.sleep(5)

    nueva_ruta = os.path.abspath(
        "data/output/modificado1.xlsx"
    )

    auto.SendKeys(nueva_ruta)

    time.sleep(2)

    auto.SendKeys("{ENTER}")

    print("Archivo guardado en:")
    print(nueva_ruta)

    # Esperar a que Excel termine de guardar
    time.sleep(3)

    # Cerrar Excel
    auto.SendKeys("{ALT}{F4}")

    print("Excel cerrado")

def main():

    archivo_excel = r"data/input/prueba.xlsx"

    ventana_excel = abrir_excel(
        archivo_excel
    )

    resultado = ejecutar_login()

    escribir_resultado_excel(
        ventana_excel,
        resultado
    )

    guardar_excel()


if __name__ == "__main__":
    main()