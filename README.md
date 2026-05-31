Automatización de Excel y Login Web con Playwright

Este proyecto automatiza el siguiente flujo:

1. Abre un archivo Excel.
2. Ejecuta una prueba de Login en una página web utilizando Playwright.
3. Obtiene el resultado de la prueba.
4. Escribe el resultado dentro del archivo Excel.
5. Guarda una copia del archivo en una nueva ubicación.
6. Cierra Excel automáticamente.

 Tecnologías utilizadas:
* Python 3.12+
* PDM
* Playwright
* UIAutomation


Instalar dependencias:

powershell/cmd

pdm install


Si las dependencias no existen todavía:

powershell/cmd
pdm add playwright
pdm add uiautomation


Estructura del proyecto

PRUEBA/
│
├── data/
│   ├── input/
│   │   └── prueba.xlsx
│   │
│   └── output/
│
├── src/
│   └── proyecto/
│       └── main.py
│
├── pyproject.toml
└── README.md
(Verificar que en la ruta "data" exista una carpeta llamada "output" , si no se debera crear una para poder ejecutar programa)




Ejecución

Desde la raíz del proyecto:

powershell/cmd/bash
pdm run python src/proyecto/main.py



Resultado esperado

El sistema:

* Abre Excel.
* Realiza Login en la página de pruebas.
* Escribe el resultado en Excel.
* Guarda una copia en: "data/output/modificado1.xlsx" 
* Cierra Excel.
* Finaliza la ejecución.



Credenciales utilizadas

Usuario: student
Contraseña: Password123

Página utilizada para el test login: https://practicetestautomation.com/practice-test-login/
