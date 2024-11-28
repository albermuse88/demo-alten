import csv
import logging
import os
import shutil
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def before_all(context):
    log_dir = os.path.join(os.path.dirname(__file__), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(
        filename=os.path.join(log_dir, 'log_pruebas.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info('Inicio de la ejecución de pruebas')

    screenshot_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
    if os.path.exists(screenshot_dir):
        shutil.rmtree(screenshot_dir)
        os.makedirs(screenshot_dir)

    context.resultados_pruebas = []


def before_scenario(context, scenario):
    print(f"Escenario: {scenario.name}")
    print(f"Etiquetas: {scenario.tags}")

    chrome_driver_path = os.path.join(
        os.path.dirname(__file__), "../drivers/chromedriver.exe"
    )

    service = Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()


def after_step(context, step):
    if step.status == "failed" or step.status == "passed":
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{step.name.replace(' ', '_')}-{timestamp}.png"
        screenshot_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        context.page.take_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")


def after_scenario(context, scenario):
    resultado = {
        "nombre_prueba": scenario.name,
        "resultado": scenario.status,
        "descripcion_error": str(scenario.error_message) if scenario.status == "failed" else ""}
    context.resultados_pruebas.append(resultado)

    logging.info(f"Resultado de la prueba '{scenario.name}': {scenario.status}")
    if scenario.status == "failed":
        logging.error(f"Descripción del error: {scenario.error_message}")


def after_all(context):
    ruta_csv = os.path.join(os.path.dirname(__file__), 'informes', 'resultado_pruebas.csv')

    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)

    with open(ruta_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["nombre_prueba", "resultado", "descripcion_error"])
        writer.writeheader()
        writer.writerows(context.resultados_pruebas)

    logging.info('Ejecución de pruebas finalizada')
