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

Instalar biblioteca pdm con pipx:

powershell/cmd (como administrador)

pip install pipx
pipx install pdm
pipx ensurepath

Descargar el proyecto:

Descargar el ".zip".
Ubicarse en la carpeta que desea usar para descomprimir el proyecto.
Para ejecutar se debera usar desde la ruta:

cd/ "ruta donde se descomprimio el proyecto"

pdm init

Instalar dependencias:

pdm install

Si las dependencias no existen todavía:

pdm add playwright
pdm add uiautomation

Verificar estructura de carpetas.

Antes de ejecutar el programa, verificar que exista el archivo Excel de entrada:

data/
├── input/
│   └── prueba.xlsx
│
└── output/

Si la carpeta output no existe, debe crearse manualmente.

El archivo:

prueba.xlsx

debe colocarse dentro de:

data/input/

ya que será utilizado por la automatización para registrar el resultado de la prueba.
Se recomienda abrir con anterioriad el archivo excel "prueba.xlsx" para habilitar el editado si este se descargo, de lo contrario se tiene que eliminar y crear otro archivo excel con el mismo nombre para evitar problemas.




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


Si se desean realizar mas pruebas tener en cuenta el archivo "modificado1.xlsx", este se tendra que elimnar o cambiarle el nombre para no tener problemas durante futuras ocasiones.



Credenciales utilizadas

Usuario: student
Contraseña: Password123

Página utilizada para el test login: https://practicetestautomation.com/practice-test-login/
